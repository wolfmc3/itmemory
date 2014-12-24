from django.views import generic
from ittasks.models import Task


class IndexView(generic.ListView):
    template_name = 'ittasks/index.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task
    template_name = 'ittasks/detail.html'
    context_object_name = 'obj'

    def get_queryset(self):
        return Task.objects.all()