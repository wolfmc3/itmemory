# coding=utf-8
from django.core.management.base import BaseCommand
from hwlogs.models import LogFilter, HwLog


class Command(BaseCommand):
    def handle(self, *args, **options):
        for slog in LogFilter.objects.filter(operation=1).all():
            slog.apply_filter(HwLog.objects).delete()