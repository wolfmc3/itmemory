from django.db.models import Q
from django.views import generic
from customers.models import Customer


class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    context_object_name = 'objects_list'

    def post(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)

    def get_queryset(self):
        # import pdb
        # pdb.set_trace()
        items = Customer.objects.all()
        if 'obj_name' in self.request.POST.keys() and self.request.POST['obj_name']:
            return items.filter(Worksites__hardwareobjects__name__icontains=self.request.POST['obj_name'])
        if 'obj_serial' in self.request.POST.keys() and self.request.POST['obj_serial']:
            return items.filter(Worksites__hardwareobjects__serial__icontains=self.request.POST['obj_serial'])
        if 'cust_name' in self.request.POST.keys() and self.request.POST['cust_name']:
            return items.filter(
                Q(name__icontains=self.request.POST['cust_name']) |
                Q(Worksites__name__icontains=self.request.POST['cust_name'])
            )
        return items


class DetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/detail.html'
    context_object_name = 'obj'

    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        from ittasks.models import Task

        context['openedtasks'] = Task.objects.filter(
            hardwareobject__worksite__customer_id=context['obj'].id,
            done=False
        )
        context['closedtasks'] = Task.objects.filter(
            hardwareobject__worksite__customer_id=context['obj'].id,
            done=True
        )
        return context