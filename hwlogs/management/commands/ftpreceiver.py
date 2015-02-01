# coding=utf-8
import os
from stat import ST_SIZE
from django_ftpserver import utils
from django_ftpserver.management.commands import ftpserver
from pyftpdlib.handlers import FTPHandler
from hwlogs.models import logsfromfile


class Command(ftpserver.Command):
    def make_server(
            self,
            server_class,
            handler_class,
            authorizer_class,
            host_port,
            file_access_user=None, **handler_options
    ):
        directory = "/tmp/receiver/"
        if not os.path.exists(directory):
            os.makedirs(directory)

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
        logsfromfile(receivedfile)
