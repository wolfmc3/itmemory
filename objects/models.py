# coding=utf-8
from django.db import models
from customers.models import WorkSite
from simplecrypt import encrypt, decrypt
from itmemory import settings as django_setting



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
        return str(self.hardwareobject) + " - " + self.type.name + ": " + str(self.value)


class SoftwarePassword(models.Model):
    class Meta():
        verbose_name = "Password"
        verbose_name_plural = "Passwords"

    hardwareobject = models.ForeignKey(HardwareObject, verbose_name="Oggetto")
    settingtype = models.ForeignKey(SettingsType, related_name='softwarepasswords', verbose_name="Tipo impostazione")
    url = models.URLField()
    username = models.CharField(max_length=100, null=True, blank=True)
    passwd = models.BinaryField(max_length=250, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not str(self.passwd).startswith("sc\x00"):
            self.passwd = encrypt(django_setting.SECRET_KEY, self.passwd).decode('string_escape')
        super(SoftwarePassword, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.hardwareobject) + " - " + self.settingtype.name + ": " + str(self.username)
