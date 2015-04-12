from django.core.urlresolvers import reverse
from django.db.models import Q
from django.views import generic
from django.http import HttpResponseRedirect
from customers.models import Customer


class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    context_object_name = 'objects_list'
    paginate_by = 15

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


class ImportCustomer(generic.TemplateView):
    template_name = "customers/import.html"

    def get_context_data(self, **kwargs):
        context = super(ImportCustomer, self).get_context_data(**kwargs)
        if 'searchin' in self.request.POST.keys() and self.request.POST['searchin']:
            from magonet.connector import MagoNet
            conn = MagoNet()
            conn.connect()
            req_type = self.request.POST['searchin']
            context['searchin'] = self.request.POST['searchin']
            data = context['searchdata'] = self.request.POST['searchdata']
            rows = None
            if req_type == "name":
                rows = conn.getcustomer_byname(data)
            if req_type == "code":
                rows = conn.getcustomer_byid(data)
            context["rows"] = rows
            conn.disconnect()
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


def import_add(request):
    from magonet.connector import MagoNet
    conn = MagoNet()
    conn.connect()
    rows = conn.getcustomer_byid(str(request.GET['code']))
    conn.disconnect()
    row = rows[0]
    cust_list = Customer.objects.filter(origin_code=row['CustSupp'])
    if cust_list:
        newcust = cust_list[0]
    else:
        newcust = Customer()
    newcust.address = row['Address']
    newcust.city = row['City']
    newcust.email = row['EMail']
    newcust.name = row['CompanyName']
    newcust.origin_code = row['CustSupp']
    newcust.telephone = row['Telephone1'] + " " + row['Telephone2'] + " " + row['Fax']
    newcust.save()
    return HttpResponseRedirect(reverse("customers:detail", kwargs={"pk": newcust.id}))

