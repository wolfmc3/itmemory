# coding=utf-8
import codecs
from datetime import datetime
import unicodedata

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http.response import HttpResponse, HttpResponseNotFound
from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response
import time

from hpilo.models import importfromjson, IloStatusDetail
from itmemory import settings
from objects.models import HardwareObject


class UploadView(generic.TemplateView):
    template_name = 'hpilo/upload.html'

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(HardwareObject, pk=kwargs.get("hwid", 0))
        if obj.remote_token == kwargs.get("hwtoken", "not provided"):
            fl = request.FILES['file']
            path = default_storage.save('upload/' + fl.name, ContentFile(fl.read()))
            path = default_storage.base_location + "/" + path
            importfromjson(path)
            return HttpResponse("True")
        else:
            return HttpResponseNotFound('False')


def sensorchart(request, detailid):
    from chartit import DataPool, Chart
    ref = IloStatusDetail.objects.get(id=detailid)
    sensors = DataPool(
        series=[
            {
                'options': {
                    'source': IloStatusDetail.objects.filter(
                        ilostatus__hardwareobject=ref.ilostatus.hardwareobject,
                        item=ref.item,
                        component=ref.component,
                        name=ref.name
                    ).all()[:40]
                },
                'terms': [
                    ('ilostatus__time', lambda d: time.mktime(d.timetuple())),
                    'value'
                ]
            }
        ])

    # Step 2: Create the Chart object
    cht = Chart(
        datasource=sensors,
        series_options=[{
            'options': {
                'type': 'line',
                'stacking': False
            },
            'terms': {
                'ilostatus__time': [
                    'value'
                ]}
        }],
        chart_options=
        {
            'title': {'text': 'Valori sensore ' + ref.name + " - " + unicode(ref.ilostatus.hardwareobject)},
            'xAxis': {
                'title': {
                    'text': 'Giorno'
                }
            },
            'yAxis': {
                'title': {
                    'text': ref.um
                }
            }
        },
        x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime("%d %b %H:%M"), False)
    )

    return render_to_response('hpilo/sensorgraph.html', {'sensorgraph': cht})


class CreatePack(generic.TemplateView):
    template_name = 'hpilo/createpack.html'

    def post(self, request, *args, **kwargs):
        import zipfile
        import os

        root = os.path.join(settings.BASE_DIR, 'hpilo/static/pack/')
        obj = get_object_or_404(HardwareObject, pk=kwargs.get("hwid", 0))
        postr = request.POST
        zipf = zipfile.ZipFile('/tmp/SendLog%s.zip' % obj.id, 'w')
        sendlog_string = codecs.open(os.path.join(root, 'sendlogs.ps1'), encoding='utf-8').read()
        sendlog_string = unicodedata.normalize('NFKD', sendlog_string).encode('ascii', 'ignore')
        rpl = {
            "ILOIP": postr.get("iloip", ""),
            "ILOUSER": postr.get("ilouser", ""),
            "ILOPASSWORD": postr.get("ilopassword", ""),
            "HWID": obj.id,
            "TOKEN": obj.remote_token,
            "ILOENABLED": "True" if postr.get("iloenabled", False) else "False",
        }
        for k, r in rpl.items():
            sendlog_string = sendlog_string.replace("{%s}" % k, str(r))
        zipf.writestr("sendlogs.ps1", sendlog_string)
        if postr.get("iloenabled"):
            if postr.get("ilosetup"):
                zipf.write(os.path.join(root, 'HPiLOCmdlets-x64.exe'), "Hpilosetup/HPiLOCmdlets-x64.exe")
            getilo_string = codecs.open(os.path.join(root, 'getilostatus.ps1'), encoding='utf-8').read()
            getilo_string = unicodedata.normalize('NFKD', getilo_string).encode('ascii', 'ignore')
            for k, r in rpl.items():
                getilo_string = getilo_string.replace("{%s}" % k, str(r))
            zipf.writestr("getilostatus.ps1", getilo_string)
        if postr.get("scheduler"):
            sh_xml_string = codecs.open(os.path.join(root, 'sendlog.xml'), encoding='utf-16').read()
            sh_xml_string = unicodedata.normalize('NFKD', sh_xml_string).encode('ascii', 'ignore')
            for k, r in rpl.items():
                sh_xml_string = sh_xml_string.replace("{%s}" % k, str(r))
            zipf.writestr("sendlog.xml", sh_xml_string)
        zipf.close()
        response = HttpResponse(open(zipf.filename, "rb"), content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename=sendlogs.zip'
        return response