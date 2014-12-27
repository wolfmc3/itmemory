from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.datetime_safe import datetime
from django.views import generic
from django.forms.models import modelformset_factory
from ittasks.models import Task
from ittasks.models import TaskCheck, TaskCheckTemplate
from django.forms import HiddenInput, Textarea, RadioSelect
from lib.booleanyesno import HorizRadioRenderer


def updatechecks(request, pk):
    if request.user.is_authenticated() and request.is_ajax:
        tsk = get_object_or_404(Task, id=pk)
        chkstmpl = TaskCheckTemplate.objects.filter(tasktemplate_id=tsk.template_id)
        for checktmpl in chkstmpl:
            if not TaskCheck.objects.filter(task_id=tsk.id, checktemplate_id=checktmpl.id):
                ntaskcheck = TaskCheck(task=tsk, checktemplate=checktmpl)
                ntaskcheck.exectime = datetime.now()
                ntaskcheck.save()
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
        else:
            newtask = tsk
        return JsonResponse({"redirect": reverse('ittasks:detail', args=(newtask.id,))})
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


class IndexView(generic.ListView):
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
            'result': RadioSelect(renderer=HorizRadioRenderer, attrs={'class': 'btnyesno'},
                                  choices=((False, 'Positivo'), (True, 'Negativo')))
        }
        # TODO: form per dati utente
        taskcheckform = modelformset_factory(TaskCheck, widgets=wdg, can_delete=False, extra=0)
        context['formset'] = taskcheckform(queryset=checkslist)
        return context

    def get_queryset(self):
        return Task.objects.all()