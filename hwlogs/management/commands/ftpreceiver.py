# coding=utf-8
import os
from stat import ST_SIZE
from django_ftpserver import utils
from django_ftpserver.management.commands import ftpserver
from pyftpdlib.handlers import FTPHandler
from hwlogs.models import HwLog
from objects.models import HardwareObject


class Command(ftpserver.Command):
    def make_server(
            self,
            server_class,
            handler_class,
            authorizer_class,
            host_port,
            file_access_user=None, **handler_options
    ):
        handler_class = FtpHandler
        return utils.make_server(
            server_class,
            handler_class,
            authorizer_class,
            host_port,
            file_access_user=file_access_user,
            **handler_options)


class FtpHandler(FTPHandler):
    # def __init__(self):

    def on_file_received(self, receivedfile):
        print ("Ricevuto il file %s" % receivedfile)
        info = os.stat(receivedfile)
        print ("Dimensione file %s" % info[ST_SIZE])

        filedata = receivedfile.split("-")
        objid = filedata[1]
        obj = None
        if objid.isdigit():
            obj = HardwareObject.objects.get(id=objid)

        if obj:
            import csv
            with open(receivedfile, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                colnames = spamreader.next()
                colindex = dict(zip(colnames, range(0, len(colnames))))
                for row in spamreader:
                    log = HwLog(hardwareobject=obj)
                    log.message = row[colindex["Message"]]
                    log.record_id = row[colindex["RecordId"]]
                    log.event_id = row[colindex["Id"]]
                    log.level = row[colindex["Level"]]
                    log.log_name = row[colindex["ProviderName"]]
                    log.time = row[colindex["TimeCreated"]]
                    log.save()
        os.remove(receivedfile)
        print ("Elaborazione completata %s" % receivedfile)
