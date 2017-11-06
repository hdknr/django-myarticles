# coding: utf-8
from django.apps import AppConfig as DjAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(DjAppConfig):
    name = 'myarticles'
    verbose_name = _('My Articles')

    def ready(self):
        from . import tasks     # NOQA
