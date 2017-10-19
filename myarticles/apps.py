# coding: utf-8
from django.apps import AppConfig as DjAppConfig


class AppConfig(DjAppConfig):
    name = 'myarticles'

    def ready(self):
        from . import tasks     # NOQA
