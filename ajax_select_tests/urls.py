from django.conf.urls import patterns, include

from ajax_select import urls as ajax_select_urls

urlpatterns = patterns('',
    # include the lookup urls
    (r'^test/lookups/', include(ajax_select_urls)),
    # (r'^admin/', include(admin.site.urls)),
)
