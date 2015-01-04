# coding=utf-8
from django.db import models
from django.utils.datetime_safe import datetime
from customers.models import WorkSite
from simplecrypt import encrypt, decrypt
from itmemory import settings as django_setting


class HardwareObject(models.Model):
    class Meta():
        verbose_name = "Dispositivo hardware"
        verbose_name_plural = "Dispositivi hardware"
        ordering = ['worksite']

    worksite = models.ForeignKey(WorkSite, related_name='hardwareobjects', verbose_name="Luogo di installazione")
    name = models.CharField(max_length=300, verbose_name="Nome del prodotto")
    item = models.CharField(max_length=32, verbose_name="Codice del prodotto")
    serial = models.CharField(max_length=50, verbose_name="numero di serie")
    location = models.CharField(max_length=250, verbose_name="Ubicazione")
    primary_ip = models.IPAddressField(default='0.0.0.0', verbose_name="Indirizzo IP primario")
    know_name = models.CharField(max_length=255, default='', verbose_name="Nome breve")
    image = models.ImageField(null=True, blank=True)

    def _taskstodo(self):
        return self.tasks.filter(done=False, laststart__lte=datetime.now)

    taskstodo = property(_taskstodo)

    def __str__(self):
        return self.name + "  [" + self.serial + "]"


class SettingGroup(models.Model):
    from ittasks.models import TaskTemplate

    class Meta():
        verbose_name = "Gruppo impostazioni"
        verbose_name_plural = "Gruppi impostazioni"
        ordering = ['name']

    name = models.CharField(max_length=255, verbose_name="Gruppo impostazioni")
    activatetask = models.ForeignKey(TaskTemplate, null=True, blank=True, verbose_name="Task da attivare")

    def _firstsetting(self):
        return self.settings.first()

    firstsetting = property(_firstsetting)

    def __str__(self):
        return self.name


class SettingsType(models.Model):
    from ittasks.models import TaskTemplate

    class Meta():
        verbose_name = "Tipo impostazione"
        verbose_name_plural = "Tipi impostazione"
        ordering = ['group']

    name = models.CharField(max_length=255, verbose_name="Tipo impostazione")
    group = models.ForeignKey(SettingGroup, related_name='settings', verbose_name="Gruppo impostazioni")
    activatetask = models.ForeignKey(TaskTemplate, null=True, blank=True, verbose_name="Task da attivare")

    def __str__(self):
        return self.group.name + "/" + self.name


class Settings(models.Model):
    class Meta():
        verbose_name = "Impostazione"
        verbose_name_plural = "Impostazioni"
        ordering = ['type']

    hardwareobject = models.ForeignKey(HardwareObject, related_name="settings", verbose_name="Oggetto")
    type = models.ForeignKey(SettingsType, related_name='settings', verbose_name="Tipo impostazione")
    value = models.TextField(max_length=5000, verbose_name="Valore impostato")

    def _activatetask(self):
        return [self.type.activatetask, self.type.group.activatetask]

    activatetask = property(_activatetask)

    def __str__(self):
        return str(self.hardwareobject) + " - " + self.type.name + ": " + str(self.value)


class SoftwarePassword(models.Model):
    class Meta():
        verbose_name = "Password"
        verbose_name_plural = "Passwords"
        ordering = ['settingtype']

    hardwareobject = models.ForeignKey(HardwareObject, related_name='softwarepasswords', verbose_name="Oggetto")
    settingtype = models.ForeignKey(SettingsType, related_name='softwarepasswords', verbose_name="Tipo impostazione")
    url = models.URLField(null=True, blank=True, verbose_name="Indirizzo web")
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome utente")
    password = models.CharField(max_length=50, null=True, blank=True, verbose_name="Password")
    passwd = models.BinaryField(max_length=250, null=True, blank=True)

    def _plainpassword(self):
        return decrypt(django_setting.SECRET_KEY, self.passwd)

    plainpassword = property(_plainpassword)

    def _activatetask(self):
        return [self.settingtype.activatetask, self.settingtype.group.activatetask]

    activatetask = property(_activatetask)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not (self.password == "{encrypted}"):
            self.passwd = encrypt(django_setting.SECRET_KEY, self.password)
            self.password = "{encrypted}"
        super(SoftwarePassword, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.hardwareobject) + " - " + self.settingtype.name + ": " + str(self.username)

