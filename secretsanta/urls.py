from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'people.views.home'),
    url(r'^pick/(\d+)/$', 'people.views.show_pick'),
    url(r'^admin/', include(admin.site.urls)),
)
