from django.conf.urls import patterns, include, url
from forms import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # visitor pages
    url(r'^$', views.index, name='index'),
    url(r'^visitor/$', views.all_visitor),
    url(r'^visitor/(?P<visitor_id>\d+)/$', views.visitor, name='visitor'),

    # saveUpdate, saveNew, delete
    url(r'^visitor/(?P<visitor_id>\d+)/event', views.event, name='event'),
)

 # url(r'^calendar/(?P<visitor_id>\d+)/$', 'forms.views.visitor_calendar'),    
    # url(r'^calendar/$', 'forms.views.calendar'),

