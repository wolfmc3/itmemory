from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from templated_email import send_templated_mail
from hpilo.templatetags.hpilo_tags import iloerrors
from ittasks.models import Task, send_mail_user


class Command(BaseCommand):
    args = ''
    help = 'Esegue il cron per i task'

    def handle(self, *args, **options):
        objs = iloerrors()
        objs = objs["objs"]
        maildests = dict()

        for slog in objs:
            notify, subset = slog["notifygroup"], slog["subset"]
            # self.stdout.write("Ilo error processing {0} filter".format(notify.name))
            subset = subset.filter(notified=False)
            if subset and (notify.user or notify.group):
                dests = set()
                if notify.user:
                    dests = dests | {notify.user}
                if notify.group:
                    dests = dests | set(list(notify.group.user_set.all()))
                for dest in dests:
                    if dest.email not in maildests:
                        maildests[dest.email] = {'user': dest, 'objects': [], 'filters': []}
                    maildests[dest.email]['objects'] += subset
                    maildests[dest.email]['filters'] += [notify.name]
                subset.update(notified=True)

        for mail, data in maildests.iteritems():
            # self.stdout.write("Send iloerrors to " + mail + " {0} log".format(len(data['objects'])))
            subject = "HP ILO: " + (', '.join(data['filters']))
            send_mail_errors(data['objects'], subject, data['user'], "notify_ilo")


def send_mail_errors(subset, subject, user, template):
    if user.email is None:
        return
    return send_templated_mail(
        template_name=template,
        from_email=settings.EMAIL_SENDER,
        recipient_list=[user.email],
        context={
            'subject': subject,
            'username': user.username,
            'full_name': user.get_full_name(),
            'subset': subset
        },
    )
