from datetime import datetime
from django.core.management.base import BaseCommand
from ittasks.models import Task, send_mail_user


class Command(BaseCommand):
    args = ''
    help = 'Esegue il cron per i task'

    def handle(self, *args, **options):
        tasks = Task.objects.filter(done=False)
        for task in tasks:
            '''
            self.stdout.write("Task {0}:\tR:{1}\tE:{2}\t".format(
                task.id,
                str(task.send_reminder),
                str(task.send_expiration),
                ), ending=' '
            )
            '''
            if task.send_reminder:
                user_list = []

                if task.user is not None:
                    user_list.append(task.user)
                elif task.template.send_reminder_group is not None:
                    user_list.extend(task.template.send_reminder_group.user_set.all())
                for mail_user in user_list:
                    # self.stdout.write("\tSended reminder to " + mail_user.email)
                    send_mail_user(task, mail_user, "reminder_task")
                # self.stdout.write("Sended reminder", ending='\t')
                task.reminder_send_date = datetime.now()
                task.save()
            if task.send_expiration:
                user_list = []
                if task.template.send_reminder_group is not None:
                    user_list.extend(task.template.send_reminder_group.user_set.all())
                if task.user is not None and task.user not in user_list:
                    user_list.append(task.user)
                for mail_user in user_list:
                    send_mail_user(task, mail_user, "expired_task")
                    self.stdout.write("\tSended expiration reminder to " + mail_user.email)
                # self.stdout.write("Sended expiration reminder", ending='')
                task.expired_send_date = datetime.now()
                task.save()
            # self.stdout.write(".")

