from django.core.management.base import BaseCommand
from ittasks.models import Task


class Command(BaseCommand):
    args = ''
    help = 'Esegue il cron'

    def handle(self, *args, **options):
        tasks = Task.objects.filter(done=False)
        for task in tasks:
                task.reminder_send_date = None
                task.expired_send_date = None
                task.save()
