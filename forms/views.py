# Create your views here.
from django.http import HttpResponse
from forms.models import Visitor
from django.template import Context, loader

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
	t = loader.get_template('forms/visitorPage.html')
	c = Context({
		'latest_visitor_list': latest_visitor_list
		})
	return HttpResponse(t.render(c))
