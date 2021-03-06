# Create your views here.
from django.http import HttpResponse
# from django.core.exceptions import PermissionDenied
from forms.models import Visitor, Event
from django.shortcuts import render_to_response, get_object_or_404, render

# serialize events for calendar
import json
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
	return HttpResponse("You have reached the forms index.")


def all_visitor(request):
	latest_visitor_list = Visitor.objects.all()

	return render_to_response('forms/all_visitor.html', {'latest_visitor_list': latest_visitor_list})


def visitor(request, visitor_id):
	latest_visitor_list = Visitor.objects.all()
	visitor = get_object_or_404(Visitor, pk=visitor_id)

	event_list = Event.objects.filter(visitor=visitor_id)
	event_data = []

	for event in event_list:
		new_event= {
		"title": event.title,
		"location": event.location,
		"start":event.start,
		"end":event.end,
		"detail":event.detail,
		"creator":event.creator.id,
		"editor":event.editor.id,
		"lastEdit":event.lastEdit,
		"allDay":False,
		"id":event.id
		}
		event_data.append(new_event)

	event_data = json.dumps(event_data, cls=DjangoJSONEncoder)

	return render(request, 'forms/visitorPage.html', {'latest_visitor_list': latest_visitor_list, 'visitor':visitor, "event_data":event_data})


def event(request, visitor_id):

	post = request.POST
	#
	# if post['status'] == 'delete':
	# 	pass
	# # 	write later, once events are in the db.
	# if post['status'] == 'new':
	# 	new_event = Event()
	# 	# new_event.title = post['title']
	# 	# new_event.location = post['location']
	# 	# new_event.detail = post['detail']
	# 	# new_event.phone = post['phone']
	# 	new_event.visitor = get_object_or_404(Visitor, pk=visitor_id)
	# if post['status'] == 'edit':
	# 	pass

# <QueryDict:
# {u'title': [u'sdf'],
#  u'detail': [u'DETAILS'],
#  u'phone': [u'PHONE'],
#  u'location': [u'LOCATION'],
#  u'csrfmiddlewaretoken': [u'y3SlMciee8IgHSc8P4cdDRK49TVsjG53'],
#  u'save': [u'save']}>

	print visitor_id
# 		need start and end time

	print request.POST

	return HttpResponse()