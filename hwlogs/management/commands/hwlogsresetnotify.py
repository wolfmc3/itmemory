# coding=utf-8
import datetime
from django.core.management.base import BaseCommand
from hwlogs.models import HwLog


class Command(BaseCommand):
    args = '<days>'
    help = 'Azzera il flag notify per <days> giorni'

    def handle(self, *args, **options):

        if len(args) == 1 and args[0].isdigit():
            days = int(args[0])
            date = datetime.datetime.now() + datetime.timedelta(days=-days)
            cnt = HwLog.objects.filter(time__gt=date).update(notify_count=0)
            self.stdout.write('Aggiornati %s record' % cnt)
        else:
            self.stdout.write('Errore Specificare il numero di giorni')