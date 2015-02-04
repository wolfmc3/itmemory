import datetime
from django.db import models
from django.utils.functional import curry
from objects.models import HardwareObject


class StatusCharField(models.CharField):
    json = None

    def __init__(self, verbose_name=None, json=None, *args, **kwargs):
        kwargs['max_length'] = 20
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
    hardwareobject = models.ForeignKey(HardwareObject, related_name="ilostatuses")
    status = StatusCharField("Stato generale",  json='STATUS_MESSAGE')  # STATUS_MESSAGE
    bios = StatusCharField("Bios",              json="BIOS_HARDWARE_STATUS")  # BIOS_HARDWARE_STATUS
    fans = StatusCharField("Ventole",           json="FANS_STATUS")  # FANS_STATUS
    memory = StatusCharField("Memoria",         json="MEMORY_STATUS")  # MEMORY_STATUS
    network = StatusCharField("Rete",           json="NETWORK_STATUS")  # NETWORK_STATUS
    power = StatusCharField("Alimentazione",    json="POWER_SUPPLIES.STATUS")  # POWER_SUPPLIES.STATUS
    processor = StatusCharField("Processore",   json="PROCESSOR_STATUS")  # PROCESSOR_STATUS
    storage = StatusCharField("Archiviazione",  json="STORAGE_STATUS")  # STORAGE_STATUS
    temperature = StatusCharField("Temperature", json="TEMPERATURE_STATUS")  # TEMPERATURE_STATUS
    time = models.DateTimeField("Rilevamento")



class IloStatusDetail(models.Model):
    ilostatus = models.ForeignKey(IloStatus, related_name="statusdetails")
    item = models.CharField("Oggetto", max_length=255) # TEMP, FANS, STORAGE
    name = models.CharField("Nome", max_length=255, default="", blank=True, null=True) # LABEL
    component = models.CharField("Componente", max_length=255, blank=True, null=True) # LOCATION | ZONE
    value = models.IntegerField("Valore", default=0, blank=True, null=True) # CURRENTREADING | SPEED -> SPLIT(" ")[0]
    um = models.CharField("Unita", max_length=255, default="", null=True) # CURRENTREADING | SPEED -> SPLIT(" ")[1]
    status = StatusCharField("Stato", json="STATUS", blank=True, null=True) # STATUS


def importfromjson(json_file):
    filedata = json_file.split("-")
    objid = filedata[1]
    obj = None
    if objid.isdigit():
        obj = HardwareObject.objects.get(id=objid)

    if obj:
        import json, codecs
        with codecs.open(json_file, 'r', encoding='UTF-16') as json_data:
            json_string = json_data.read()
            status_data = json.loads(json_string)
            status_obj = IloStatus(hardwareobject=obj)
            status_obj.time = datetime.datetime.now()
            status_obj.save()
            for section, data in status_data.iteritems():
                if section == "SUMMARY":
                    status_obj.status = data.get(status_obj.get_status_json(),"ND")
                    status_obj.bios = data.get(status_obj.get_bios_json(),"ND")
                    status_obj.fans = data.get(status_obj.get_fans_json(),"ND")
                    status_obj.memory = data.get(status_obj.get_memory_json(),"ND")
                    status_obj.processor = data.get(status_obj.get_processor_json(),"ND")
                    status_obj.network = data.get(status_obj.get_network_json(),"ND")
                    # TODO: Verificare che il campo power venga correttamente popolato
                    status_obj.power = data.get(status_obj.get_power_json(),"ND")
                    status_obj.storage = data.get(status_obj.get_storage_json(),"ND")
                    status_obj.temperature = data.get(status_obj.get_temperature_json(),"ND")
                    status_obj.save()
                elif section in ["TEMP", "FAN"]:
                    for row in data:
                        status_detail = IloStatusDetail(ilostatus=status_obj)
                        status_detail.item = section
                        status_detail.component = row.get("LOCATION",row.get("ZONE",""))
                        status_detail.value, status_detail.um = row.get("CURRENTREADING",
                                                                        row.get("SPEED","0 Value")).split(" ")
                        status_detail.name = row.get("LABEL","")
                        status_detail.status = row.get(status_detail.get_status_json())
                        status_detail.save()




        # TODO: Remove final
        # os.remove(json_file)
        # TODO: Statuses rotate
        # from django.core.management import call_command
        # call_command('logrotate')


