from django.db import models
from customers.models import WorkSite


class HardwareObject(models.Model):
    class Meta():
        verbose_name = "Dispositivo hardware"
        verbose_name_plural = "Dispositivi hardware"

    worksite = models.ForeignKey(WorkSite, related_name='hardwareobjects', verbose_name="Luogo di installazione")
    name = models.CharField(max_length=300, verbose_name="Nome del prodotto")
    item = models.CharField(max_length=32, verbose_name="Codice del prodotto")
    serial = models.CharField(max_length=50, verbose_name="numero di serie")
    location = models.CharField(max_length=250, verbose_name="Ubicazione")
    primary_ip = models.IPAddressField(default='0.0.0.0', verbose_name="Indirizzo IP primario")
    know_name = models.CharField(max_length=255, default='', verbose_name="Nome breve")

    def __str__(self):
        return self.name + "  [" + self.serial + "]"


class SettingGroup(models.Model):
    class Meta():
        verbose_name = "Gruppo impostazioni"
        verbose_name_plural = "Gruppi impostazioni"

    name = models.CharField(max_length=255, verbose_name="Gruppo impostazioni")

    def __str__(self):
        return self.name


class SettingsType(models.Model):
    class Meta():
        verbose_name = "Tipo impostazione"
        verbose_name_plural = "Tipi impostazione"

    name = models.CharField(max_length=255, verbose_name="Tipo impostazione")
    group = models.ForeignKey(SettingGroup, related_name='settings', verbose_name="Gruppo impostazioni")

    def __str__(self):
        return self.group.name + "/" + self.name


class Settings(models.Model):
    class Meta():
        verbose_name = "Impostazione"
        verbose_name_plural = "Impostazioni"

    hardwareobject = models.ForeignKey(HardwareObject, verbose_name="Oggetto")
    type = models.ForeignKey(SettingsType, related_name='settingstype', verbose_name="Tipo impostazione")
    value = models.TextField(max_length=5000, verbose_name="Valore impostato")

    def __str__(self):
        return str(self.hardwareobject) + " - " + self.type.name + ": " + self.value
