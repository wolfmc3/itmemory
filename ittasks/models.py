# coding=utf-8
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from templated_email import send_templated_mail
from objects.models import HardwareObject
from dateutil.relativedelta import relativedelta
from django.db.models.signals import pre_save



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

    send_reminder = models.BooleanField(default=True, verbose_name="Invia promemoria")
    send_expiration = models.BooleanField(default=True, verbose_name="Invia promemoria scadenza")

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

    template = models.ForeignKey(TaskTemplate, related_name='tasks', verbose_name="Modello di task")
    hardwareobject = models.ForeignKey(HardwareObject, related_name='tasks',
                                       verbose_name="Hardware associato")

    enabled = models.BooleanField(default=True, verbose_name="Abilitato")
    done = models.BooleanField(default=False, verbose_name="Completato")
    laststart = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo avvio/esecuzione")
    user = models.ForeignKey(User, null=True, blank=True,related_name="assigned_tasks", verbose_name="Utente assegnato")
    reminder_send_date = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo invio promemoria")
    expired_send_date = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo invio scadenza")

    def _send_reminder(self, check_date=datetime.now().date()):
        if self.done:
            return False
        r_date = (self.laststart - relativedelta(days=settings.TASK_REMIND_DAYS)).date()
        if not self.reminder_send_date is None:
            if check_date <= self.reminder_send_date.date():
                return False
        print( "r_date " + str(r_date))
        print( "check_date " + str(check_date))
        return r_date < check_date


    def _send_expiration(self, check_date=datetime.now().date()):
        if self.done:
            return False
        e_date = (self.laststart + relativedelta(days=settings.TASK_EXPIRED_DAYS)).date()
        if not self.expired_send_date is None:
            if check_date <= self.expired_send_date.date():
                return False
        print( "r_date " + str(e_date))
        print( "check_date " + str(check_date))
        return e_date < check_date

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
        return chkstmpl


    to_past = property(_to_past)
    nextstart = property(_nextstart)
    createnext = property(_createnext)
    updatechecks = property(_updatechecks)
    send_reminder = property(_send_reminder)
    send_expiration = property(_send_expiration)

    def has_changed(instance, field):
        if not instance.pk:
            return False
        old_value = instance.__class__._default_manager.filter(pk=instance.pk).values(field).get()[field]
        return not getattr(instance, field) == old_value

    def get_original(instance, field):
        if not instance.pk:
            return getattr(instance, field)
        old_value = instance.__class__._default_manager.filter(pk=instance.pk).values(field).get()[field]
        return old_value

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
        (4, 'Passato con errori (WARN)'),
        (2, 'Fallito (NG)'),
        (3, 'Non applicabile (NA)'),
    )
    RESULT_VALUES_CLASS = {
        0: 'warning',
        1: 'primary',
        2: 'danger',
        3: 'info',
        4: 'warning',
    }
    result = models.IntegerField(default=0,
                                 choices=RESULT_VALUES,
                                 verbose_name="Risultato")

    def _cssresult(self):
        return self.RESULT_VALUES_CLASS[self.result]

    cssresult = property(_cssresult)
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Note sul controllo")

    def __str__(self):
        return str(self.task) + " " + self.checktemplate.name + " " + (self.get_result_display())

def send_mail_user(task, user, template):
    send_templated_mail(
        template_name=template,
        from_email='itmemory@globit.it',
        recipient_list=[user.email],
        context={
            'username':user.username,
            'full_name':user.get_full_name(),
            'task': task
        },
    )


def pre_save_task(sender, **kwargs):
    task = kwargs['instance']
    if task.has_changed('user'):
        origUserId = task.get_original('user')
        print "Task change from {0} to {1} ".format(task.get_original('user'),task.user)
        if task.user is not None:
            try:
                send_mail_user(task, task.user, "assign_task")
            except ValueError:
                print ValueError.message
            print("Assign task: send mail to user: {0} ({1})".format(
                task.user,
                task.user.email
            ))
        if origUserId is not None:
            old_tasks = Task.objects.filter(user_id=origUserId)
            if old_tasks.count > 0:
                old_task = old_tasks[0]
                print("Assign task: send cancellation mail to user: {0} ({1})".format(
                    old_task.user,
                    old_task.user.email
                ))
                try:
                    send_mail_user(old_task, old_task.user, "cancel_task")
                except ValueError:
                    print ValueError.message

pre_save.connect(pre_save_task, sender=Task)