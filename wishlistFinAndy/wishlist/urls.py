from django.conf.urls import include, url
from django.contrib import admin
from list import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/', include('list.urls')),
    url(r'addComment/$', views.addComment, name='addComment'),
    url(r'deleteComment/(?P<user_id>[\w\-]+)/$', views.deleteComment, name='deleteComment'),
    url(r'^helpful/(?P<user_id>[\w\-]+)/$', views.helpful, name='helpful'),
]
