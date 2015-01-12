import calendar
from datetime import datetime, date
from django.views import generic
from customers.models import Customer
from ittasks.models import Task
from objects.models import HardwareObject


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'tasks_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        now = datetime.now()
        daystart, dayend = calendar.monthrange(now.year, now.month)
        monthstart = date(day=daystart, month=now.month, year=now.year)
        monthend = date(day=dayend, month=now.month, year=now.year)
        openedthismonth = Task.objects.filter(laststart__gte=monthstart, laststart__lte=monthend, done=False).count()
        closedthismonth = Task.objects.filter(laststart__gte=monthstart, laststart__lte=monthend, done=True).count()
        customers_count = Customer.objects.count()
        hwobjects_count = HardwareObject.objects.count()
        userdone_count = Task.objects.filter(user=self.request.user, done=True).count()
        context['openedtasks'] = Task.objects.filter(done=False).exclude(user=self.request.user).order_by("laststart")
        context['usertasks'] = Task.objects.filter(user=self.request.user, done=False).order_by("laststart")
        context['recentclosedtasks'] = Task.objects.filter(done=True).order_by("laststart")[:10]

        stats = [
            {
                'label': 'Le tue verfiche da eseguire',
                'value': str(context['usertasks'].count()),
                'icon': 'user'
            },
            {
                'label': 'Verifiche eseguite da te',
                'value': str(userdone_count),
                'icon': 'ok'
            },
            {
                'label': 'Clienti registrati',
                'value': str(customers_count),
                'icon': 'info-sign'
            },
            {
                'label': 'Verifiche da eseguire nel mese',
                'value': str(openedthismonth),
                'icon': 'dashboard'
            },
            {
                'label': 'Verifiche eseguite nel mese',
                'value': str(closedthismonth),
                'icon': 'ok'
            },
            {
                'label': 'Dispositivi registrati',
                'value': str(hwobjects_count),
                'icon': 'hdd'
            },
        ]
        context['stats'] = stats
        return context

    def get_queryset(self):
        return Task.objects.all()