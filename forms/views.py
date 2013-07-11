# Create your views here.
from django.http import HttpResponse
from forms.models import Visitor
from django.shortcuts import render_to_response, get_object_or_404


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
	visitor = get_object_or_404(Visitor, pk=visitor_id)

	return render_to_response('forms/visitorPage.html', {'latest_visitor_list': latest_visitor_list, 'visitor': visitor})
#  


