# coding=utf-8
from django.core.management.base import BaseCommand
from django.db.models.query_utils import Q

from hwlogs.models import LogFilter, HwLog, send_mail_log
from cron.management.commands.cron import cronregistry


class Command(BaseCommand):
    def handle(self, *args, **options):
        maildests = dict()

        for slog in LogFilter.objects.filter(operation=2).filter(Q(user__isnull=False) | Q(group__isnull=False)).all():
            self.stdout.write("Processing {0} filter".format(slog.name))
            objects = slog.apply_filter(HwLog.objects).filter(notify_count=0)
            objectlist = objects.all()[:]

            if objectlist:
                dests = set()
                if slog.user:
                    dests = dests | {slog.user}
                if slog.group:
                    dests = dests | set(list(slog.group.user_set.all()))
                for dest in dests:
                    if dest.email not in maildests:
                        maildests[dest.email] = {'user': dest, 'objects': [], 'filters': []}
                    maildests[dest.email]['objects'] += objectlist
                    maildests[dest.email]['filters'] += [slog.name]
                objects.update(notify_count=1)

        for mail, data in maildests.iteritems():
            self.stdout.write("Send logs to " + mail + " {0} log".format(len(data['objects'])))
            subject = "Nuovi log: " + (', '.join(data['filters']))
            send_mail_log(data['objects'], subject, data['user'], "notify_logs")



