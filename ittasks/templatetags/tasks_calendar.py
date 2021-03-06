from datetime import date, timedelta, datetime

from django import template
from ittasks.models import Task


register = template.Library()


@register.inclusion_tag("ctl_calendar.html")
def ctl_calendar():
    pass

MONTHS = [
    "",
    "Gennaio",
    "Febbraio",
    "Marzo",
    "Aprile",
    "Maggio",
    "Giugno",
    "Luglio",
    "Agosto",
    "Settembre",
    "Ottobre",
    "Novembre",
    "Dicembre"
]


@register.inclusion_tag("calendar.html")
def taskcalendar(month=None, year=None):
    import calendar
    if month is None:
        month = datetime.now().month
    if year is None:
        year = datetime.now().year
    month = int(month)
    year = int(year)
    days = []
    first_day = date(year, month, 1)
    start_day = first_day - timedelta(days=first_day.weekday())
    last_day = date(year, month, calendar.monthrange(year, month)[1])
    end_day = last_day + timedelta(days=6 - last_day.weekday())
    curday = start_day
    tasks = Task.objects.filter(laststart__gte=start_day, laststart__lte=end_day).order_by("laststart")
    tasklist = dict()
    for task in tasks:
        dt_str = str(task.laststart.date())
        if tasklist.get(dt_str, False):
            tasklist[dt_str].append(task)
        else:
            tasklist[dt_str] = [task]

    while curday <= end_day:
        days.append({
            'date': curday,
            'events': tasklist.get(str(curday), None),
            'overmonth': curday.month != month
        })
        curday = curday + timedelta(days=1)
    # import pdb; pdb.set_trace()

    return {
        'now': datetime.now(),
        'dates': days,
        'month_name': MONTHS[month] + ' ' + str(year),
        'start_day': start_day - timedelta(days=1),
        'end_day': end_day + timedelta(days=1)
    }


@register.inclusion_tag("personal_task.html", takes_context=True)
def personal_tasks(context):
    user = context['user']
    tasks = user.assigned_tasks.filter(done=False).order_by("laststart")
    return {"user_tasks": tasks}

