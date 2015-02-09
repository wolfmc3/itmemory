# coding=utf-8
import datetime
from django.db import models
from objects.models import HardwareObject


class StatusCharField(models.CharField):
    json = None

    def __init__(self, verbose_name=None, json=None, *args, **kwargs):
        kwargs['max_length'] = 125
        self.json = json
        super(StatusCharField, self).__init__(*args, **kwargs)

    def _get_FIELD_status(self):
        return self == "OK"

    def _get_FIELD_json(self):
        return self.json

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(StatusCharField, self).contribute_to_class(cls, name, virtual_only)

        if self._get_FIELD_status:
            setattr(cls, 'get_%s_status' % self.name, self._get_FIELD_status)

        if self.json:
            setattr(cls, 'get_%s_json' % self.name, self._get_FIELD_json)


class IloStatus(models.Model):
    class Meta():
        verbose_name = "Stato HP Ilo"
        verbose_name_plural = "Stati HP Ilo"
        ordering = ['-time']

    hardwareobject = models.ForeignKey(HardwareObject, related_name="ilostatuses")
    status = StatusCharField("Stato generale", json='STATUS_MESSAGE')  # STATUS_MESSAGE
    bios = StatusCharField("Bios", json="BIOS_HARDWARE_STATUS")  # BIOS_HARDWARE_STATUS
    fans = StatusCharField("Ventole", json=["FANS_STATUS", "FANS.STATUS"])  # FANS_STATUS
    memory = StatusCharField("Memoria", json="MEMORY_STATUS")  # MEMORY_STATUS
    network = StatusCharField("Rete", json="NETWORK_STATUS")  # NETWORK_STATUS
    power = StatusCharField("Alimentazione", json=["POWER_SUPPLIES.STATUS", "POWER_STATUS"])  # POWER_SUPPLIES.STATUS
    processor = StatusCharField("Processore", json="PROCESSOR_STATUS")  # PROCESSOR_STATUS
    storage = StatusCharField("Archiviazione", json="STORAGE_STATUS")  # STORAGE_STATUS
    temperature = StatusCharField("Temperature", json="TEMPERATURE_STATUS")  # TEMPERATURE_STATUS
    source = models.CharField("Sorgente", max_length=255, default="", null=True, blank=True)
    time = models.DateTimeField("Rilevamento")


class IloStatusDetail(models.Model):
    class Meta():
        verbose_name = "Dettaglio Stato HP Ilo"
        verbose_name_plural = "Dettagli Stato HP Ilo"
        ordering = ['item', 'component']
    ilostatus = models.ForeignKey(IloStatus, related_name="statusdetails")
    item = models.CharField("Oggetto", max_length=255)  # TEMP, FANS, STORAGE
    name = models.CharField("Nome", max_length=255, default="", blank=True, null=True)  # LABEL
    component = models.CharField("Componente", max_length=255, blank=True, null=True)  # LOCATION | ZONE
    value = models.IntegerField("Valore", default=0, blank=True, null=True)  # CURRENTREADING | SPEED -> SPLIT(" ")[0]
    um = models.CharField("Unita", max_length=255, default="", null=True)  # CURRENTREADING | SPEED -> SPLIT(" ")[1]
    status = StatusCharField("Stato", json="STATUS", blank=True, null=True)  # STATUS

    def __str__(self):
        return self.name


def importfromjson(json_file):
    filedata = json_file.split("-")
    objid = filedata[1]
    obj = None
    if objid.isdigit():
        obj = HardwareObject.objects.get(id=objid)

    if obj:
        import json
        import codecs

        with codecs.open(json_file, 'r', encoding='UTF-16') as json_data:
            json_string = json_data.read()
            status_data = json.loads(json_string)
            status_obj = IloStatus(hardwareobject=obj)
            status_obj.source = "File:%s" % json_file
            status_obj.time = datetime.datetime.now()
            status_obj.save()
            for section, data in status_data.iteritems():
                if section == "SUMMARY":
                    status_obj.status = _finditem(status_obj.get_status_json(), data)
                    status_obj.bios = _finditem(status_obj.get_bios_json(), data)
                    status_obj.fans = _finditem(status_obj.get_fans_json(), data)
                    status_obj.memory = _finditem(status_obj.get_memory_json(), data)
                    status_obj.processor = _finditem(status_obj.get_processor_json(), data)
                    status_obj.network = _finditem(status_obj.get_network_json(), data)
                    status_obj.power = _finditem(status_obj.get_power_json(), data)
                    status_obj.storage = _finditem(status_obj.get_storage_json(), data)
                    status_obj.temperature = _finditem(status_obj.get_temperature_json(), data)
                    status_obj.save()
                elif section in ["TEMP", "FAN"]:
                    if data is not None:
                        for row in data:
                            status_detail = IloStatusDetail(ilostatus=status_obj)
                            status_detail.item = section
                            status_detail.component = _finditem(["LOCATION", "ZONE"], row, "")
                            status_detail.value, status_detail.um = _finditem(
                                ["CURRENTREADING", "SPEED"],
                                row,
                                "0 Value"
                            ).split(" ")
                            status_detail.name = row.get("LABEL", "")
                            status_detail.status = _finditem(status_detail.get_status_json(), row)
                            status_detail.save()
                elif section in ["LOGICAL_DRIVE"]:
                    if data is not None:
                        for row in data:
                            status_detail = IloStatusDetail(ilostatus=status_obj)
                            status_detail.item = section
                            status_detail.component = "LV" + _finditem("LABEL", row, "")
                            status_detail.value, status_detail.um = _finditem(
                                "CAPACITY",
                                row,
                                "0 GB"
                            ).split(" ")
                            status_detail.name = "Volume " + row.get("LABEL", "X")
                            status_detail.status = _finditem(status_detail.get_status_json(), row)
                            status_detail.save()
                            if row.get("PHYSICAL_DRIVE"):
                                for subrow in row.get("PHYSICAL_DRIVE"):
                                    status_detail = IloStatusDetail(ilostatus=status_obj)
                                    status_detail.item = "PHYSICAL_DRIVE"
                                    status_detail.component = _finditem("LOCATION", subrow, "") + \
                                        "( LV" + _finditem("LABEL", row, "") + ")"
                                    status_detail.value, status_detail.um = _finditem(
                                        "CAPACITY",
                                        subrow,
                                        "0 GB"
                                    ).split(" ")
                                    status_detail.name = "DISK (" + subrow.get("SERIAL_NUMBER", "X") + ")"
                                    status_detail.status = _finditem(status_detail.get_status_json(), subrow)
                                    status_detail.save()

                                    # TODO: Remove final
                                    # os.remove(json_file)
                                    # TODO: Statuses rotate
                                    # from django.core.management import call_command
                                    # call_command('logrotate')


def _finditem(key, obj, notfound="ND"):
    """
    Ritorna il valore delle chiavi specificate
    es. "SENSOR"
    es. ["SENSOR1","OBJECT1.SENSOR2"]
    :param key: string | list
    :param obj: dict
    :param notfound: return value if not found
    :return: key value | notfound
    """
    resdict = dict()
    if not isinstance(key, list):
        key = [key]
    for k in key:  # scorre le chiavi da cercare e si ferma alla prima trovata
        kex = k.split(".")  # esplode la chiave per cercare nelle sottochiavi
        kexobj = obj
        for kexk in kex:
            kexobj = kexobj.get(kexk, None)
            if kexobj is None:
                break
        if kexobj is not None:
            resdict[k] = kexobj
    if len(resdict) == 1:
        # c'è un solo valore e ritorna quello
        return resdict.values()[0]
    if len(resdict) > 1:
        res = list(set(resdict.items().values()))
        if len(res) == 1:
            return res[0]
        else:
            res = [x for x in res if x != "OK"]
            return " ".join(res)
    return notfound
