from django.views import generic
from objects.models import HardwareObject


class IndexView(generic.ListView):
    template_name = 'objects/index.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return HardwareObject.objects.all()


class DetailView(generic.DetailView):
    model = HardwareObject
    template_name = 'objects/detail.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        from ittasks.models import Task

        context['openedtasks'] = Task.objects.filter(hardwareobject_id=context['obj'].id, done=False)
        context['closedtasks'] = Task.objects.filter(hardwareobject_id=context['obj'].id, done=True)
        return context

    def get_queryset(self):
        return HardwareObject.objects.all()