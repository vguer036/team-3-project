"""bookstoreproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from helloworld.views import home
from helloworld.views import index, bookdetails_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #image
#from bookdetails.views import myView #sprint2 bookdetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdetails/', index),
   # path('bookdetails/', bookdetails_view), #idk about this one
   # path('bookdetails/', index ) #3/23
   #3/22 path('sayHello/', myView), #sprint2 helloworld
 #   path('bookdetails/', myView),#sprint2 bookdetails
]

#urlpatterns += staticfiles_urlpatterns() #image


