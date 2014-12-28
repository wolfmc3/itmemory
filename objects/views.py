from django.views import generic
from objects.models import HardwareObject
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'objects/index.html'
    context_object_name = 'objects_list'

    def post(self, request, *args, **kwargs):

        kwargs['obj_name'] = request.POST['obj_name']
        return self.get(self, request, *args, **kwargs)

    def get_queryset(self):
        # import pdb
        # pdb.set_trace()
        items = HardwareObject.objects.all()
        if 'obj_name' in self.request.POST.keys() and self.request.POST['obj_name']:
            return items.filter(name__icontains=self.request.POST['obj_name'])
        if 'obj_serial' in self.request.POST.keys() and self.request.POST['obj_serial']:
            return items.filter(serial__icontains=self.request.POST['obj_serial'])
        if 'cust_name' in self.request.POST.keys() and self.request.POST['cust_name']:
            return items.filter(
                Q(worksite__customer__name__icontains=self.request.POST['cust_name']) |
                Q(worksite__name__icontains=self.request.POST['cust_name'])
            )
        return items


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