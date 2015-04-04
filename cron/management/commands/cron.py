# coding=utf-8
from django.core.management.base import BaseCommand


class CronRegisterHelper(object):
    _commandlist = []

    def register(self, func):
        self._commandlist.append(func)

    def execute(self, *args, **options):
        for func in self._commandlist:
            # print func.__module__

            try:
                func.execute(*args, **options)
            except Exception as err:
                print func.__module__
                print "\nError!!:"
                print err
            ''' else:
                print "\nOK!"
            print "END %s" % func.__module__
            '''


cronregistry = CronRegisterHelper()


class Command(BaseCommand):
    def handle(self, *args, **options):
        cronregistry.execute()


