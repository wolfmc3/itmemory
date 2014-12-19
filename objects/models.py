from django.db import models
from customers.models import WorkSite


class HardwareObject(models.Model):
    worksite = models.ForeignKey(WorkSite, related_name='objects')
    name = models.CharField(max_length=300)
    item = models.CharField(max_length=32)
    serial = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    primary_ip = models.IPAddressField(default='0.0.0.0')

    def __str__(self):
        return self.name + "  [" + self.serial + "]"


class SettingGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SettingsType(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(SettingGroup, related_name='settings')

    def __str__(self):
        return self.group.name + "/" + self.name


class Settings(models.Model):
    hardwareobject = models.ForeignKey(HardwareObject)
    type = models.ForeignKey(SettingsType, related_name='settingstype')
    value = models.TextField(max_length=5000)

    def __str__(self):
        return str(self.hardwareobject) + " - " + self.type.name + ": " + self.value
