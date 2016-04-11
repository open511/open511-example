from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [

    url(r'^api/', include('open511_server.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'open511_example.hello.simple_index_page'),
    
]

try:
    import django_open511_ui
    urlpatterns += [
        url(r'^map/', include('django_open511_ui.urls')),
        url(r'^accounts/', include('django_open511_ui.auth_urls')),
    ]
except ImportError:
    pass
