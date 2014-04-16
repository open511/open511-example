from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^api/', include('open511_server.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'open511_example.hello.simple_index_page'),
    
)

try:
    import django_open511_ui
    urlpatterns += patterns('',
        url(r'^map/', include('django_open511_ui.urls')),
        url(r'^accounts/', include('django_open511_ui.auth_urls')),
    )
except ImportError:
    pass
