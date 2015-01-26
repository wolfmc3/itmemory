from django import template
from django.template.loader import render_to_string
from hwlogs.models import LogFilter


register = template.Library()


@register.simple_tag(takes_context=True)
def toactivatetask(context, hwobject):
    tasktoactivate = dict()
    for settingitem in hwobject.settings.all():
        tsktype, tskgroup = settingitem.activatetask
        if tsktype:
            tasktoactivate[tsktype.id] = tsktype
        if tskgroup:
            tasktoactivate[tskgroup.id] = tskgroup
    for settingitem in hwobject.softwarepasswords.all():
        tsktype, tskgroup = settingitem.activatetask
        if tsktype:
            tasktoactivate[tsktype.id] = tsktype
        if tskgroup:
            tasktoactivate[tskgroup.id] = tskgroup
    html = ""
    for stask in tasktoactivate.itervalues():
        if stask.tasks.filter(hardwareobject=hwobject).count() == 0:
            html += "<p><a class='btn btn-xs btn-success' href='act_task/{0}'>{2} Attiva {1}</a></p>".format(
                stask.id,
                str(stask),
                render_to_string("icon.html", {'iconname': "plus-sign"})
            )
    if not html:
        html = "<p>" + render_to_string("icon.html", {'iconname': "info-sign"}) + "Nessun controllo da attivare</p>"
    return html


@register.inclusion_tag("objects/logs_table.html", takes_context=True)
def hwlogs(context, hwobject, limit=10):
    active = int(context['request'].GET.get("filter_log", -1))
    mainqueryset = hwobject.systemlogs.order_by("-time")
    if active != -1:
        flt = LogFilter.objects.get(id=active)
        mainqueryset = flt.apply_filter(mainqueryset)
        limit = 50
    retcontext = {
        'logs': mainqueryset.all()[:limit],
        'group_logs': [],
        'active_filter': active
    }
    for flt in LogFilter.objects.filter(operation=0):
        retcontext['group_logs'].append(
            {
                'id': flt.id,
                'name': flt.name,
                'active': flt.id == active,
                'logs': flt.apply_filter(hwobject.systemlogs.order_by("-time")),
                'count': flt.apply_filter(hwobject.systemlogs.order_by("-time")).count
            }
        )
    return retcontext
