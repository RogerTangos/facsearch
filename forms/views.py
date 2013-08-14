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
	print 'event page reached'
	# Process information from event. Add to database.
	# visitor = get_object_or_404(Visitor, pk=visitor_id)
	# print visitor
	print request

	print request.POST
	print request.POST['phone']

	return render_to_response('forms/all_visitor.html')

	# return HttpResponse("You are at the event page.")
