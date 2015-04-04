# coding=utf-8
from django.core.management.base import BaseCommand

from hwlogs.models import LogFilter, HwLog, send_mail_log
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        maildests = dict()
        dest = User.objects.get(username=args[0])

        maildests[dest.email] = {'user': dest, 'objects': [], 'filters': []}
        maildests[dest.email]['objects'] = HwLog.objects.all()[:25]
        maildests[dest.email]['filters'] = [LogFilter.objects.all()[1].name]

        for mail, data in maildests.iteritems():
            self.stdout.write("Send test logs to " + mail + " {0} log".format(len(data['objects'])))
            subject = "TEST log: " + (', '.join(data['filters']))
            send_mail_log(data['objects'], subject, data['user'], "notify_logs")



