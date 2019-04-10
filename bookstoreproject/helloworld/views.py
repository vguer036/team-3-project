from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import BookDetails
from django.template import loader


# Create your views here.
#def myView(request):
	#return render(request, 'helloworld/bookdetails.html') #sprint2 helloworld

#3/23
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Vicky G'
	args = {'myName': name}
	return render(request, 'helloworld/bookdetails.html', args) #got html from under templates

def get(self, request):
	bookdetails = BookDetails.objects.all()
	return render(request, 'helloworld/bookdetails.html', args)

def bookdetails_view(request):
	obj = BookDetails.objects.get(id=1)
	context = {
		'object': obj
	}
	return render(request, 'helloworld/bookdetails.html', {})

def index(request):
	all_bookdetails = BookDetails.objects.all()
	template = loader.get_template('helloworld/bookdetails.html')
	context = { 
		'all_bookdetails': all_bookdetails,
	}
	return HttpResponse(template.render(context,request))
