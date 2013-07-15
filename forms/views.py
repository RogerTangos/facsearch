# Create your views here.
from django.http import HttpResponse
from forms.models import Visitor, Event
# from django.template import Context, loader
from django.shortcuts import render_to_response

# serialize events for calendar
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder


# def index(request):
# 	return HttpResponse("Hello, world. You're at the index")

def calendar(request):
	return HttpResponse("You're at the main calendar.")

# def visitor(request, visitor_id):
# 	return HttpResponse("You're at the page for visitor id %s's forms" %visitor_id)

def visitor_calendar(request, visitor_id):
	return HttpResponse("You're at the page for visitor %s's calendar" %visitor_id)

def visitor(request, visitor_id):
	# return HttpResponse("You're at the page for visitor id %s's forms" %visitor_id)

	latest_visitor_list = Visitor.objects.all()
	visitor = Visitor.objects.get(pk=visitor_id)

	event_list = Event.objects.filter(visitor=visitor_id)

	formatted_list = []

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
		}

		formatted_list.append(new_event)

	event_data = simplejson.dumps(formatted_list, cls=DjangoJSONEncoder)
	print event_data
	return render_to_response ('forms/visitorPage.html', {'latest_visitor_list': latest_visitor_list, 'visitor':visitor, 'event_data':event_data})
	# t = loader.get_template('forms/visitorPage.html')
	# c = Context({
	# 	'latest_visitor_list': latest_visitor_list
	# 	})
	# return HttpResponse(t.render(c))
