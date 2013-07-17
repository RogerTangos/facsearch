from django.conf.urls import patterns, include, url
from forms import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'facsearch.views.home', name='home'),
    # url(r'^facsearch/', include('facsearch.foo.urls')),

    # visitor page
    url(r'^visitor/(?P<visitor_id>\d+)/$', views.visitor, name='visitor'),

    # saveUpdate, saveNew, delete
    url(r'^visitor/(?P<visitor_id>\d+)/saveUpdate$', views.saveUpdate , name='saveUpdate'),
    url(r'^visitor/(?P<visitor_id>\d+)/saveNew$', views.saveNew, name='saveNew'),
    url(r'^visitor/(?P<visitor_id>\d+)/saveDelete$', views.saveDelete, name='saveDelete'),

    # url(r'^calendar/(?P<visitor_id>\d+)/$', 'forms.views.visitor_calendar'),    
    # url(r'^calendar/$', 'forms.views.calendar'),



    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
