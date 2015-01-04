import datetime
from django.core.urlresolvers import reverse
from django.forms import HiddenInput
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import UpdateView, CreateView
from objects.models import HardwareObject, SoftwarePassword, Settings
from ittasks.models import TaskTemplate, Task
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


def createtask(request, pk, task):
    if request.user.is_authenticated() and request.is_ajax:
        hwobj = get_object_or_404(HardwareObject, id=pk)
        taskobj = get_object_or_404(TaskTemplate, id=task)
        newtask = Task(template=taskobj, hardwareobject=hwobj)
        newtask.laststart = datetime.datetime.now()
        newtask.laststart = newtask.nextstart
        newtask.save()
    return HttpResponseRedirect(reverse("objects:detail", kwargs={"pk": hwobj.id}))


def getpassword(request, pk):
    if request.user.is_authenticated() and request.is_ajax:
        pwd = get_object_or_404(SoftwarePassword, id=pk)
        return JsonResponse({"password": pwd.plainpassword})
    else:
        return HttpResponse("invalid data or error")


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


class PasswordCreate(CreateView):
    template_name = "objects/password.html"
    model = SoftwarePassword

    def get_initial(self):
        initial = {'hardwareobject': self.kwargs.get('objid')}
        if self.request.GET.get('grp'):
            initial["settingtype"] = self.request.GET.get('grp')
        return initial

    def get_success_url(self):
        return reverse("objects:detail", kwargs={"pk": self.kwargs.get('objid')})

    def get_form(self, form_class):
        form = super(PasswordCreate, self).get_form(form_class=form_class)
        # form.fields['hardwareobject'].widget.attrs['readonly'] = True
        form.fields['hardwareobject'].widget.attrs['disabled'] = True

        # import pdb
        # pdb.set_trace()
        return form


class PasswordUpdate(UpdateView):
    template_name = "objects/password.html"
    model = SoftwarePassword

    def get_initial(self):
        initial = {'hardwareobject': self.kwargs.get('objid')}
        return initial

    def get_success_url(self):
        return reverse("objects:detail", kwargs={"pk": self.kwargs.get('objid')})

    def get_form(self, form_class):
        form = super(PasswordUpdate, self).get_form(form_class=form_class)
        form.fields['hardwareobject'].widget.attrs['readonly'] = True
        form.fields['hardwareobject'].widget.attrs['disabled'] = True

        # import pdb
        # pdb.set_trace()
        return form


class SettingCreate(CreateView):
    template_name = "objects/password.html"
    model = Settings

    def get_initial(self):
        initial = {'hardwareobject': self.kwargs.get('objid')}
        if self.request.GET.get('grp'):
            initial["type"] = self.request.GET.get('grp')
        return initial

    def get_success_url(self):
        return reverse("objects:detail", kwargs={"pk": self.kwargs.get('objid')})

    def get_form(self, form_class):
        form = super(SettingCreate, self).get_form(form_class=form_class)
        form.fields['hardwareobject'].widget.attrs['readonly'] = True
        form.fields['hardwareobject'].widget.attrs['disabled'] = True

        # import pdb
        # pdb.set_trace()
        return form


class SettingUpdate(UpdateView):
    template_name = "objects/password.html"
    model = Settings

    def get_initial(self):
        initial = {'hardwareobject': self.kwargs.get('objid')}
        return initial

    def get_success_url(self):
        return reverse("objects:detail", kwargs={"pk": self.kwargs.get('objid')})

    def get_form(self, form_class):
        form = super(SettingUpdate, self).get_form(form_class=form_class)
        form.fields['hardwareobject'].widget.attrs['readonly'] = True
        form.fields['hardwareobject'].widget.attrs['disabled'] = True

        # import pdb
        # pdb.set_trace()
        return form

