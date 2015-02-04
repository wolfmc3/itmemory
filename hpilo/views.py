from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http.response import HttpResponse, HttpResponseNotFound
from django.views import generic
from hpilo.models import importfromjson
from django.shortcuts import get_object_or_404
from objects.models import HardwareObject


class UploadView(generic.TemplateView):
    template_name = 'hpilo/upload.html'

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(HardwareObject, pk=kwargs.get("hwid",0))
        if obj.remote_token == kwargs.get("hwtoken", "not provided"):
            fl = request.FILES['file']
            path = default_storage.save('upload/' + fl.name, ContentFile(fl.read()))
            path = default_storage.base_location + "/" + path
            importfromjson(path)
            return HttpResponse("True")
        else:
            return HttpResponseNotFound('False')