from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # forms
    url(r'^forms/', include('forms.urls', namespace="forms")),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

 # url(r'^calendar/(?P<visitor_id>\d+)/$', 'forms.views.visitor_calendar'),    
    # url(r'^calendar/$', 'forms.views.calendar'),

