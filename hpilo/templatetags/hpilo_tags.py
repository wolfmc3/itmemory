from django import template
from hpilo.models import IloStatusDetail


register = template.Library()


@register.inclusion_tag("hpilo/ilostatus.html", takes_context=True)
def ilostatus(context, hwobj):
    ilostatusobj = hwobj.ilostatuses.first()
    retcontext = {
        'obj': ilostatusobj,
    }
    return retcontext


@register.simple_tag()
def iloled(text, status, detail=None, extrainfo=None):
    icon = '/static/' + ("ok" if status == "OK" else "alert") + ".gif"
    extrainfo_html = ""
    if status != "OK":
        text += "&nbsp;<small>(%s)</small>" % status
    if detail:
        detail = """
        <a class='pull-right' href='#' onclick='$("#%s").toggle(); return false;' >
            <span class="badge">
                &nbsp;<span class="caret"></span>&nbsp;&nbsp;
            </span>
        </a>
        """ % detail
    else:
        detail = ""
    if extrainfo:
        assert isinstance(extrainfo, IloStatusDetail)
        if extrainfo.item == "TEMP":
            extrainfo_html = """
            <div class="progress pull-right" style="display: inline-block; width: 30%; height: 17px; margin:0px; ">
              <div class="progress-bar" role="progressbar" aria-valuenow="{1}" aria-valuemin="0" aria-valuemax="100" style="width: {1}%;">
                <span class="sr-only">{0}% Power</span>
              </div>
            </div>
            <span class="badge pull-right">
                &nbsp;{0} &deg;&nbsp;
            </span>
            """.format(extrainfo.value, long(float(extrainfo.value-15)/70*100))
        if extrainfo.item == "FAN":
            extrainfo_html = """
            <div class="progress pull-right" style="display: inline-block; width: 50%; height: 17px; margin:0px; ">
              <div class="progress-bar {1}" role="progressbar" aria-valuenow="{0}" aria-valuemin="0" aria-valuemax="100" style="width: {0}%;">
                <span class="sr-only">{0}% Power</span>
              </div>
            </div>
            <span class="pull-right">
                &nbsp;{0} %&nbsp;
            </span>
            """.format(extrainfo.value, "progress-bar-info" if extrainfo.value < 80 else "progress-bar-warning")
        if extrainfo.item in ["LOGICAL_DRIVE", "PHYSICAL_DRIVE"]:
            extrainfo_html = """
            <span class="badge pull-right">
                &nbsp;{0} {1}&nbsp;
            </span>
            """.format(extrainfo.value, extrainfo.um)
    html = "<div title='Status: {4}'><img src='{0}' />&nbsp;&nbsp;{1}{2}{3}</div>".format(
        icon,
        text,
        detail,
        extrainfo_html,
        status
    )
    return html


@register.inclusion_tag("hpilo/ilodetail.html")
def ilodetail(ilostatusobj, section):
    ilostatusdetails = ilostatusobj.statusdetails.filter(item=section).all()
    retcontext = {
        'objs': ilostatusdetails,
    }
    return retcontext
