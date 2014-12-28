# coding=utf-8
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models

from objects.models import HardwareObject
from dateutil.relativedelta import relativedelta


class TaskTemplate(models.Model):
    class Meta():
        verbose_name = "Modello attività"
        verbose_name_plural = "Modelli attività"

    name = models.CharField(max_length=100, verbose_name="Nome")

    day = models.CharField(max_length=2, verbose_name="Giorni")
    month = models.CharField(max_length=2, verbose_name="Mesi")
    year = models.CharField(max_length=4, verbose_name="Anni")

    hour = models.CharField(max_length=2, verbose_name="Ore")
    minute = models.CharField(max_length=2, verbose_name="Minuti")
    enabled = models.BooleanField(default=True, verbose_name="Abilitato")

    def __str__(self):
        return self.name


class TaskCheckTemplate(models.Model):
    class Meta():
        verbose_name = "Modello controllo"
        verbose_name_plural = "Modelli controlli"

    tasktemplate = models.ForeignKey(TaskTemplate, related_name='taskchecktemplates', verbose_name="Modello di Task")

    name = models.CharField(max_length=100, verbose_name="Nome del controllo")
    description = models.TextField(max_length=1000, verbose_name="Descrizione dell'operazione da eseguire")

    def __str__(self):
        return self.tasktemplate.name + " " + self.name


class Task(models.Model):
    class Meta():
        verbose_name = "Attività"
        verbose_name_plural = "Attività"

    template = models.ForeignKey(TaskTemplate, related_name='templates', verbose_name="Modello di task")
    hardwareobject = models.ForeignKey(HardwareObject, related_name='hardwareobjects',
                                       verbose_name="Hardware associato")

    enabled = models.BooleanField(default=True, verbose_name="Abilitato")
    done = models.BooleanField(default=False, verbose_name="Completato")
    laststart = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo avvio/esecuzione")
    user = models.ForeignKey(User, null=True, blank=True, verbose_name="Utente assegnato")

    def _createnext(self):
        newtask = Task(
            template=self.template,
            hardwareobject=self.hardwareobject
        )
        newtask.enabled = True
        newtask.done = False
        newtask.laststart = self.nextstart
        newtask.save()
        return newtask

    def _nextstart(self):
        rd = relativedelta()
        tmpl = self.template
        if tmpl.day != '*':
            rd += relativedelta(days=int(tmpl.day))
        if tmpl.month != '*':
            rd += relativedelta(months=int(tmpl.month))
        if tmpl.year != '*':
            rd += relativedelta(years=int(tmpl.year))
        if tmpl.hour != '*':
            rd += relativedelta(hours=int(tmpl.hour))
        if tmpl.minute != '*':
            rd += relativedelta(minutes=int(tmpl.minute))
        return self.laststart + rd

    def _to_past(self):
        return (self.laststart < datetime.now()) and not self.done

    def _updatechecks(self):
        chkstmpl = TaskCheckTemplate.objects.filter(tasktemplate_id=self.template_id)
        for checktmpl in chkstmpl:
            if not TaskCheck.objects.filter(task_id=self.id, checktemplate_id=checktmpl.id):
                ntaskcheck = TaskCheck(task=self, checktemplate=checktmpl)
                ntaskcheck.exectime = datetime.now()
                ntaskcheck.save()
        return checktmpl

    to_past = property(_to_past)
    nextstart = property(_nextstart)
    createnext = property(_createnext)
    updatechecks = property(_updatechecks)

    def __str__(self):
        return self.hardwareobject.name + " -> " + self.template.name


class TaskCheck(models.Model):
    class Meta():
        verbose_name = "Controllo"
        verbose_name_plural = "Controlli"

    task = models.ForeignKey(Task, related_name='tasks', verbose_name="Task")
    checktemplate = models.ForeignKey(TaskCheckTemplate, related_name='checktemplates', verbose_name="Modello di task")

    exectime = models.DateTimeField(verbose_name="Data di esecuzione")
    RESULT_VALUES = (
        (0, 'Non eseguito (NE)'),
        (1, 'Passato (PASS)'),
        (2, 'Fallito (NG)'),
        (3, 'Non applicabile (NA)'),
    )
    RESULT_VALUES_CLASS = {
        0: 'warning',
        1: 'primary',
        2: 'danger',
        3: 'info',
    }
    result = models.IntegerField(default=0,
                                 choices=RESULT_VALUES,
                                 verbose_name="Risultato")

    def _cssresult(self):
        return self.RESULT_VALUES_CLASS[self.result]

    cssresult = property(_cssresult)
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Note sul controllo")

    def __str__(self):
        return str(self.task) + " " + self.checktemplate.name + " " + ("OK" if self.result else "NG")