from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views import generic


class UploadView(generic.TemplateView):
    template_name = 'hwlogs/upload.html'

    def post(self, request, *args, **kwargs):
        fl = request.FILES['file_load']
        path = default_storage.save('upload/' + fl.name, ContentFile(fl.read()))
        return self.get(self, request, *args, **kwargs)