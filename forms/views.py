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


	# events = Event.objects.filter(
		start__gte=start, end=request.end, title= request.title).values('visitor', 'start', 'end', 'title')
	# data = simplejson.dumps(list(events), cls=DjangoJSONEncoder)
	# 


	return render_to_response ('forms/visitorPage.html', {'latest_visitor_list': latest_visitor_list, 'visitor':visitor})
	# t = loader.get_template('forms/visitorPage.html')
	# c = Context({
	# 	'latest_visitor_list': latest_visitor_list
	# 	})
	# return HttpResponse(t.render(c))
