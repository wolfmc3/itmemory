from django.core.management.base import BaseCommand, CommandError
from ittasks.models import Task

class Command(BaseCommand):
    args = ''
    help = 'Esegue il cron'

    def handle(self, *args, **options):
        tasks = Task.objects.filter(done=False)
        for task in tasks:
            self.stdout.write(str(task) + "  R:" + str(task.send_reminder) + "  E:" + str(task.send_expiration))
