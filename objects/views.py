from django.views import generic
from objects.models import HardwareObject, Settings


class IndexView(generic.ListView):
    template_name = 'objects/index.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return HardwareObject.objects.all()


class DetailView(generic.DetailView):
    model = HardwareObject
    template_name = 'objects/detail.html'
    context_object_name = 'obj'

    def get_queryset(self):
        return HardwareObject.objects.all()