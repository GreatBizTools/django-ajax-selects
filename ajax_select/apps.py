from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .sites import site


class SimpleAjaxSelectConfig(AppConfig):

    name = 'ajax_select'
    verbose_name = _('AjaxSelects')

    def ready(self):
        site.register(settings.AJAX_LOOKUP_CHANNELS)

class AjaxSelectConfig(SimpleAjaxSelectConfig):

    def ready(self):
        super(AjaxSelectConfig, self).ready()
        self.module.autodiscover()