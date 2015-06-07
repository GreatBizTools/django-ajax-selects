from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AjaxSelectsConfig(AppConfig):

    name = 'ajax_select'
    verbose_name = _('AjaxSelects')

    def ready(self):
        self.module.autodiscover()