from datetime import datetime, timedelta

from django.db import models

from objects.models import HardwareObject
from dateutil.relativedelta import relativedelta


class TaskTemplate(models.Model):
    name = models.CharField(max_length=100)

    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)

    hour = models.CharField(max_length=2)
    minute = models.CharField(max_length=2)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskCheckTemplate(models.Model):
    tasktemplate = models.ForeignKey(TaskTemplate, related_name='taskchecktemplates')

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.tasktemplate.name + " " + self.name


class Task(models.Model):
    template = models.ForeignKey(TaskTemplate, related_name='templates')
    hardwareobject = models.ForeignKey(HardwareObject, related_name='hardwareobjects')

    enabled = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    laststart = models.DateTimeField(default="2013-01-01 00:00")

    @property
    def _nextstart(self):
        rd = relativedelta()
        tmpl = self.template
        if tmpl.day != '*': rd += relativedelta(days=int(tmpl.day))
        if tmpl.month != '*': rd += relativedelta(months=int(tmpl.month))
        if tmpl.year != '*': rd += relativedelta(years=int(tmpl.year))
        if tmpl.hour != '*': rd += relativedelta(hours=int(tmpl.hour))
        if tmpl.minute != '*': rd += relativedelta(minutes=int(tmpl.minute))
        return self.laststart + rd

    nextstart = property(_nextstart)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            d = timedelta(days=30)
            self.laststart = datetime.now() - d
        super(Task, self).save()

    def __str__(self):
        return self.hardwareobject.name + " -> " + self.template.name


class TaskCheck(models.Model):
    task = models.ForeignKey(Task, related_name='tasks')
    checktemplate = models.ForeignKey(TaskCheckTemplate, related_name='checktemplates')

    exectime = models.DateTimeField()

    result = models.BooleanField(default=False)
    note = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.task) + " " + self.checktemplate.name + " " + ("OK" if self.result else "NG")