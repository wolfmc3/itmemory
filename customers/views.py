from django.views import generic
from customers.models import Customer


class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return Customer.objects.all()


class DetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/detail.html'
    context_object_name = 'obj'

    def get_queryset(self):
        return Customer.objects.all()