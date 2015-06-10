# coding=utf-8
import calendar
from datetime import datetime, date
from django.db.models.query_utils import Q
from django.views import generic
from docutils.nodes import field_name
from ittasks.models import Task
from django.db.models.loading import get_model
from django.db import models

SEARCH_MODELS = [
    ("objects.HardwareObject", ["remote_token"], "/objects/{0}/"),
    ("customers.Customer", [], "/customers/{0}/"),
]

REPLACES = {
    "[": "<strong>",
    "]": "</strong>",
    "(": """<br><small><span class="text-muted">""",
    ")": "</span></small>",
    }


class Search(generic.TemplateView):
    template_name = "home/search.html"

    def get_context_data(self, **kwargs):
        res = list()
        search_text = self.request.GET["q"]
        if search_text == "":
            search_text = "£$%&"
        for sitem in SEARCH_MODELS:
            model = get_model(sitem[0])
            query = Q()
            for field in model._meta.fields:

                if field.name not in sitem[1] and isinstance(field, (models.CharField, models.TextField)):
                    query |= Q(**{'{0}__icontains'.format(field.name): search_text})

            search_result = model.objects.filter(query).all()
            for model_item in search_result:
                label = unicode(model_item)
                for i, j in REPLACES.iteritems():
                    label = label.replace(i, j)
                res.append({
                    "model": model._meta.verbose_name_plural,
                    "label": label,
                    "url": sitem[2].format(model_item.id)
                })
        return {"results": res}


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'tasks_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        now = datetime.now()
        void, dayend = calendar.monthrange(now.year, now.month)
        monthstart = date(day=1, month=now.month, year=now.year)
        monthend = date(day=dayend, month=now.month, year=now.year)
        openedthismonth = Task.objects.filter(laststart__gte=monthstart, laststart__lte=monthend, done=False).count()
        closedthismonth = Task.objects.filter(laststart__gte=monthstart, laststart__lte=monthend, done=True).count()
        userdone_count = Task.objects.filter(user=self.request.user, done=True).count()
        context['openedtasks'] = Task.objects.filter(done=False).exclude(user=self.request.user).order_by("laststart")
        context['usertasks'] = Task.objects.filter(user=self.request.user, done=False).order_by("laststart")
        context['recentclosedtasks'] = Task.objects.filter(done=True).order_by("laststart")[:10]

        stats = [
            {
                'label': 'Le tue verfiche da eseguire',
                'value': str(context['usertasks'].count()),
                'icon': 'user',
                'color': 'red'
            },
            {
                'label': 'Verifiche eseguite da te',
                'value': str(userdone_count),
                'icon': 'ok',
                'color': 'green'
            },
            {
                'label': 'Verifiche nel mese',
                'value': str(openedthismonth),
                'icon': 'dashboard',
                'color': 'red'
            },
            {
                'label': 'Verifiche eseguite nel mese',
                'value': str(closedthismonth),
                'icon': 'ok',
                'color': 'green'
            },
        ]
        context['stats'] = stats
        return context

    def get_queryset(self):
        return Task.objects.all()