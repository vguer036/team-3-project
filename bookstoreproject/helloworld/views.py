from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myView(request):
	return render(request, 'helloworld/bookdetails.html') #sprint2 helloworld