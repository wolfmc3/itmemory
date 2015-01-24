from django import template
from django.template.loader import render_to_string


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


@register.inclusion_tag("objects/logs_table.html")
def hwlogs(hwobject, limit=10):
    return {'logs': hwobject.systemlogs.order_by("-time").all()[:limit]}
