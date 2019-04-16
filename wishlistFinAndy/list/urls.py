from django.conf.urls import url
from . import views
from django.contrib import admin

# from django.urls import path
# from list.views import index, bookdetails_view
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns #image
# Each URL is connected to an HTML response
app_name = 'list'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'list/add/$', views.WishListCreate.as_view(), name='wishlist-add'),

    url(r'list/(?P<pk>[0-9]+)/delete/$', views.WishListDelete.as_view(), name='wishlist-delete'),

    url(r'^(?P<wishlist_id>[0-9]+)/create_book/$', views.create_book, name='create_book'),

    url(r'^(?P<wishlist_id>[0-9]+)/delete_book/(?P<book_id>[0-9]+)/$', views.delete_book, name='delete_book'),

    url(r'bookdetails/$', views.index, name='bookdetails'),

    url(r'shoppingcart$', views.shoppingcart, name='shoppingcart'),

    url(r'removesc/', views.removesc, name='removesc'),  # remove shoppingcart

    url(r'removesfl/', views.removesfl, name='removesfl'),  # remove saved for later

    url(r'saveforlater/$', views.saveforlater, name='saveforlater'),  # save for later from cart

    url(r'addtocart/$', views.addtocart, name='addtocart'),  # add to cart from SFL

    url(r'changequantity/$', views.changequantity, name='changequantity'),

    url(r'addtocart2/$', views.addtocart2, name='addtocart2'),  # add to cart from bookdetails
\
    url(r'addComment/$', views.addComment, name='addComment'),

    url(r'deleteComment/<str:user_id>/$', views.deleteComment, name='deleteComment'),

    url(r'helpful/<str:user_id>/$', views.helpful, name='helpful'),

]
