from django.views import generic
from ittasks.models import Task


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'tasks_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        from ittasks.models import Task

        context['openedtasks'] = Task.objects.filter(done=False).order_by("laststart")
        context['usertasks'] = Task.objects.filter(user=self.request.user, done=False).order_by("laststart")
        return context

    def get_queryset(self):
        return Task.objects.all()