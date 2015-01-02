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
    return html
