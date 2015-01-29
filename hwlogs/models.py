import os
from stat import ST_SIZE
from django.contrib.auth.models import User, Group
from django.db import models
from objects.models import HardwareObject

# Windows Event Columns
# Message,Id,Level,RecordId,ProviderName,LogName,TimeCreated


class HwLog(models.Model):
    class Meta():
        verbose_name = "Log dispositivo"
        verbose_name_plural = "Logs dispositivo"
        ordering = ['-time']

    ERROR_LEVELS = [
        ('0',	'Undefinited'),
        ('1',	'Critical'),
        ('2',	'Error'),
        ('3',	'Warning'),
        ('4',	'Informational'),
        ('5',	'Verbose'),
    ]
    ERROR_LEVELS_ICONS = {
        0:	'exclamation-sign',
        1:	'exclamation-sign',
        2:	'exclamation-sign',
        3:	'warning-sign',
        4:	'info-sign',
        5:	'info-sign',
    }
    hardwareobject = models.ForeignKey(HardwareObject, related_name="systemlogs")
    message = models.TextField("Messaggio")
    event_id = models.IntegerField("Id evento")
    level = models.CharField("Livello", max_length=10, choices=ERROR_LEVELS)
    record_id = models.IntegerField("Id record", null=True, blank=True)
    log_name = models.CharField("Nome log", max_length=255)
    time = models.DateTimeField("Ora")

    def _short_message(self):
        return self.message[:60]

    short_message = property(_short_message)

    def _level_icon(self):
        return self.ERROR_LEVELS_ICONS[int(self.level)]

    level_icon = property(_level_icon)


class LogFilter(models.Model):
    class Meta():
        verbose_name = "Filtro log"
        verbose_name_plural = "Filtri log"
        ordering = ['-name']

    name = models.CharField("Nome", max_length=25)
    OPERATION_CHOICE = (
        (0, "Visualizza"),
        (1, "Non importare, cancella"),
        (2, "Notifica via email"),
        (3, "Segna come importante"),
    )
    user = models.ForeignKey(User, null=True, blank=True, related_name="logfilters", verbose_name="Destinatario mail")
    group = models.ForeignKey(Group, null=True, blank=True, related_name="logfilters", verbose_name="Destinatari mail")
    operation = models.IntegerField("Operazione", choices=OPERATION_CHOICE)

    def __str__(self):
        return self.name

    def apply_filter(self, queryset):
        vals = self.filters.all()
        for val in vals:
            kwargs = {val.value_field+val.val_op: val.value}
            if val.exclude_value == 0:
                queryset = queryset.filter(**kwargs)
            else:
                queryset = queryset.exclude(**kwargs)
        return queryset


class LogFilterValues(models.Model):
    class Meta():
        verbose_name = "Valore di filtro"
        verbose_name_plural = "Valori di filtro"
        ordering = ['weight']

    logfilter = models.ForeignKey(LogFilter, related_name="filters", verbose_name="Filtro")

    VALUEFIELD_CHOICES = (
        ('event_id', 'Id evento'),
        ('level', 'Livello'),
        ('log_name', 'Nome log'),
        ('message', 'Messaggio'),
        ('record_id', 'Id record'),
        ('time', 'Ora')
    )
    value_field = models.CharField(max_length=255, choices=VALUEFIELD_CHOICES)

    COMPARE_OPERATIONS = (
        (0, 'uguale'),
        (1, 'contiene'),
        (2, 'maggiore di'),
        (3, 'minore di'),
        (4, 'uguale o maggiore di'),
        (5, 'uguale o minore di'),
    )

    COMPARE_OPERATIONS_SUFFIX = {
        0: '__exact',
        1: '__icontains',
        2: '__gt',
        3: '__lt',
        5: '__gte',
        6: '__lte',
    }
    operation = models.IntegerField("Confronto", choices=COMPARE_OPERATIONS)

    value = models.TextField("Valore")

    def _val_op(self):
        return self.COMPARE_OPERATIONS_SUFFIX[int(self.operation)]

    val_op = property(_val_op)

    weight = models.IntegerField("Ordine",default=1)

    INCLUDE_CHOICES = (
        (0, "Includi"),
        (1, "Escludi")
    )

    exclude_value = models.IntegerField("Escludi valori", default=0, choices=INCLUDE_CHOICES)

def LogsFromFile(receivedfile):
        print ("Ricevuto il file %s" % receivedfile)
        info = os.stat(receivedfile)
        print ("Dimensione file %s" % info[ST_SIZE])

        filedata = receivedfile.split("-")
        objid = filedata[1]
        obj = None
        if objid.isdigit():
            obj = HardwareObject.objects.get(id=objid)

        if obj:
            import csv
            with open(receivedfile, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                colnames = spamreader.next()
                colindex = dict(zip(colnames, range(0, len(colnames))))
                for row in spamreader:
                    log = HwLog(hardwareobject=obj)
                    log.message = row[colindex["Message"]]
                    log.record_id = row[colindex["RecordId"]]
                    log.event_id = row[colindex["Id"]]
                    log.level = row[colindex["Level"]]
                    log.log_name = row[colindex["ProviderName"]]
                    log.time = row[colindex["TimeCreated"]].replace('.',':')
                    log.save()
        os.remove(receivedfile)
        print ("Elaborazione completata %s" % receivedfile)
