# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.datetime_safe import datetime
from django.views import generic
from django.forms.models import modelformset_factory
from ittasks.models import Task
from ittasks.models import TaskCheck, TaskCheckTemplate
from django.contrib.auth.models import User
from django.forms import HiddenInput, Textarea, RadioSelect
from lib.booleanyesno import HorizRadioRenderer


def updatechecks(request, pk):
    if request.user.is_authenticated() and request.is_ajax:
        tsk = get_object_or_404(Task, id=pk)
        tsk.updatechecks
        return HttpResponseRedirect(reverse('ittasks:detail', args=(tsk.id,)))
    else:
        return HttpResponse("invalid data or error")


def closetask(request, pk):
    if request.user.is_authenticated() and request.is_ajax:
        tsk = get_object_or_404(Task, id=pk)
        tsk.laststart = datetime.now()
        tsk.done = True
        tsk.save()
        if tsk.enabled:
            newtask = tsk.createnext
            newtask.updatechecks
        return JsonResponse({"redirect": reverse('ittasks:detail', args=(tsk.id,))})
    else:
        return HttpResponse("invalid data or error")


def updateuser(request, pk):
    if request.user.is_authenticated() and request.POST and request.is_ajax:
        tsk = get_object_or_404(Task, id=pk)
        if request.POST['new_user'].isdigit():
            tsk.user = User.objects.get(id=request.POST['new_user'])
        else:
            tsk.user = None
        tsk.save()
        return JsonResponse({"success": True})
    else:
        return HttpResponse("invalid data or error")


def setenabledtask(request, pk):
    if request.user.is_authenticated() and request.is_ajax:
        tsk = get_object_or_404(Task, id=pk)
        tsk.enabled = not tsk.enabled
        tsk.save()
        return JsonResponse({"enabled": tsk.enabled})
    else:
        return HttpResponse("invalid data or error")


def calendar(request, month, year):
    if request.user.is_authenticated() :
        return TemplateResponse(request,"ajax_calendar.html",{'month':month,'year': year})
    else:
        return HttpResponse("invalid data or error")


class IndexView(generic.ListView):
    # TODO: Da inserire lista attività e gestione
    template_name = 'ittasks/index.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task
    template_name = 'ittasks/detail.html'
    context_object_name = 'obj'

    def post(self, request, *args, **kwargs):
        taskcheckform = modelformset_factory(TaskCheck)
        frm = taskcheckform(request.POST)
        if frm.is_valid:
            frm.save()
        # import pdb
        # pdb.set_trace()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        checkslist = TaskCheck.objects.filter(task_id=context['obj'].id)
        wdg = {
            'note': Textarea(attrs={'rows': 2, 'cols': 22}),
            'task': HiddenInput,
            'exectime': HiddenInput,
            'checktemplate': HiddenInput,
        }

        taskcheckuser = modelformset_factory(Task, fields=['id', 'user'], can_delete=False, extra=0)
        taskcheckuserform = taskcheckuser(queryset=Task.objects.filter(id=context['obj'].id))
        # import pdb
        #pdb.set_trace()
        context['formsetuser'] = taskcheckuserform
        taskcheckform = modelformset_factory(TaskCheck, widgets=wdg, can_delete=False, extra=0)
        context['formset'] = taskcheckform(queryset=checkslist)
        context['checkstatuscss'] = {
            0: 'warning',
            1: 'info',
            2: 'danger'
        }
        return context

    def get_queryset(self):
        return Task.objects.all()