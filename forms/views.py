# Create your views here.
from django.http import HttpResponse
from forms.models import Visitor, Event
# from django.template import Context, loader
from django.shortcuts import render_to_response

# serialize events for calendar
import json
from django.core.serializers.json import DjangoJSONEncoder



def visitor(request, visitor_id):
	latest_visitor_list = Visitor.objects.all()
	visitor = Visitor.objects.get(pk=visitor_id)

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

	return render_to_response ('forms/visitorPage.html', {'latest_visitor_list': latest_visitor_list, 'visitor':visitor, "event_data":event_data})

def saveUpdate(request, visitor_id):
	return HttpResponse("You are updating visitor id %s" %visitor_id)

def saveNew(request, visitor_id):
	return HttpResponse("You are adding a new event for visitor id %s" %visitor_id)

def saveDelete(request, visitor_id):
	return HttpResponse("You are deleting an event for visitor id %s" %visitor_id)

# def visitor_calendar(request, visitor_id):
# 	return HttpResponse("You're at the page for visitor %s's calendar" %visitor_id)	


# def calendar(request):
# 	return HttpResponse("You're at the main calendar.")



# def index(request):
# 	return HttpResponse("Hello, world. You're at the index")

# 	return HttpResponse("You're at the page for visitor id %s's forms" %visitor_id)

