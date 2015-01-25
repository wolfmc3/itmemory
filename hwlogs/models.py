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
        ('0',	'Emergency'),
        ('1',	'Alert'),
        ('2',	'Critical'),
        ('3',	'Error'),
        ('4',	'Warning'),
        ('5',	'Notice'),
        ('6',	'Informational'),
        ('7',	'Debug'),
    ]
    ERROR_LEVELS_ICONS = {
        0:	'exclamation-sign',
        1:	'exclamation-sign',
        2:	'warning-sign',
        3:	'warning-sign',
        4:	'warning-sign',
        5:	'info-sign',
        6:	'info-sign',
        7:	'question-sign'
    }
    hardwareobject = models.ForeignKey(HardwareObject, related_name="systemlogs")
    message = models.TextField("Messaggio")
    event_id = models.IntegerField("Id evento")
    level = models.CharField("Livello", max_length=10, choices=ERROR_LEVELS)
    record_id = models.IntegerField("Id record", null=True, blank=True)
    log_name = models.CharField("Nome log", max_length=255)
    time = models.DateTimeField("Ora")

    def _short_message(self):
        return self.message[:45]

    short_message = property(_short_message)

    def _level_icon(self):
        return self.ERROR_LEVELS_ICONS[int(self.level)]

    level_icon = property(_level_icon)