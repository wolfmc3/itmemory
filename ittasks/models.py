# coding=utf-8
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User, Group
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
    send_reminder_group = models.ForeignKey(Group, null=True, blank=True,
                                            related_name="template_to_notify",
                                            verbose_name="Gruppo notifiche")

    send_expiration = models.BooleanField(default=True, verbose_name="Invia promemoria scadenza")
    send_expiration_group = models.ForeignKey(Group, null=True, blank=True,
                                              related_name="template_exp_to_notify",
                                              verbose_name="Gruppo notifiche scadenze")

    def __unicode__(self):
        return self.name


class TaskCheckTemplate(models.Model):
    class Meta():
        verbose_name = "Modello controllo"
        verbose_name_plural = "Modelli controlli"

    tasktemplate = models.ForeignKey(TaskTemplate, related_name='taskchecktemplates', verbose_name="Modello di Task")

    name = models.CharField(max_length=100, verbose_name="Nome del controllo")
    description = models.TextField(max_length=1000, verbose_name="Descrizione dell'operazione da eseguire")

    def __unicode__(self):
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
    user = models.ForeignKey(User, null=True, blank=True, related_name="assigned_tasks", verbose_name="Utente assegnato")
    reminder_send_date = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo invio promemoria")
    expired_send_date = models.DateTimeField(null=True, blank=True, verbose_name="Ultimo invio scadenza")

    def _send_reminder(self):
        check_date = datetime.now().date()
        # print("l_date " + str(self.laststart))

        if self.done or not self.template.send_reminder:
            return False

        e_date = (self.laststart + relativedelta(days=settings.TASK_EXPIRED_DAYS)).date()

        if e_date < check_date:
            return False

        r_date = (self.laststart - relativedelta(days=settings.TASK_REMIND_DAYS)).date()
        if self.reminder_send_date is not None:
            if check_date <= self.reminder_send_date.date():
                return False
        # print("r_date " + str(r_date))
        return r_date < check_date

    def _send_expiration(self):
        check_date = datetime.now().date()
        # print("l_date " + str(self.laststart))
        if self.done or not self.template.send_expiration:
            return False
        e_date = (self.laststart + relativedelta(days=settings.TASK_EXPIRED_DAYS)).date()
        if self.expired_send_date is not None:
            if check_date <= self.expired_send_date.date():
                return False
        # print("e_date " + str(e_date))
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

    def has_changed(self, field):
        if not self.pk:
            return False
        old_value = self.__class__._default_manager.filter(pk=self.pk).values(field).get()[field]
        value = getattr(self, field)
        if value is not None:
            value = value.id
        return not value == old_value

    def get_original(self, field):
        if not self.pk:
            return getattr(instance, field)
        old_value = self.__class__._default_manager.filter(pk=self.pk).values(field).get()[field]
        return old_value

    def __unicode__(self):
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
        return self.RESULT_VALUES_CLASS[int(self.result)]

    cssresult = property(_cssresult)
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Note sul controllo")

    def __unicode__(self):
        return unicode(self.task) + " " + self.checktemplate.name + " " + (self.get_result_display())


def send_mail_user(task, user, template):
    if user.email is None:
        return
    return send_templated_mail(
        template_name=template,
        from_email=settings.EMAIL_SENDER,
        recipient_list=[user.email],
        context={
            'username': user.username,
            'full_name': user.get_full_name(),
            'task': task
        },
    )


def pre_save_task(sender, **kwargs):
    task = kwargs['instance']
    if task.has_changed('user'):
        origuserid = task.get_original('user')
        print "Task change from {0} to {1} ".format(task.get_original('user'), task.user)
        if task.user is not None:
            try:
                send_mail_user(task, task.user, "assign_task")
            except ValueError:
                print ValueError.message
            print("Assign task: send mail to user: {0} ({1})".format(
                task.user,
                task.user.email
            ))
        if origuserid is not None:
            old_tasks = Task.objects.filter(user_id=origuserid)
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