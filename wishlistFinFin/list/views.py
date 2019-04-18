from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from .models import WishList, Book, BookDetails, CartItems, Product, SavedForLater, Cart
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum, F, Value
# ANDY
from django.db import models
from django.shortcuts import render
from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from .models import Comment_and_Rating
from datetime import date
import random


class IndexView(generic.ListView):
    template_name = 'list/index.html'

    def get_queryset(self):
        return WishList.objects.all()


class DetailView(generic.DetailView):
    model = WishList
    template_name = 'list/detail.html'


class WishListCreate(CreateView):
    model = WishList
    fields = ['wishlist_title']


class WishListDelete(DeleteView):
    model = WishList
    success_url = reverse_lazy('list:index')


def create_book(request, wishlist_id):
    form = BookForm(request.POST or None, request.FILES or None)
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    if form.is_valid():
        wishlist_books = wishlist.book_set.all()
        for b in wishlist_books:
            if b.book_title == form.cleaned_data.get("book_title"):
                context = {
                    'wishlist': wishlist,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'list/create_book.html', context)
        book = form.save(commit=False)
        book.wishlist = wishlist
        book.save()
        return render(request, 'list/detail.html', {'wishlist': wishlist})
    context = {
        'wishlist': wishlist,
        'form': form,
    }
    return render(request, 'list/create_book.html', context)


def delete_book(request, wishlist_id, book_id):
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    song = Book.objects.get(pk=book_id)
    song.delete()
    return render(request, 'list/detail.html', {'wishlist': wishlist})


def index(request):
    all_bookdetails = BookDetails.objects.all()
    template = loader.get_template('list/bookdetails.html')

    info = Comment_and_Rating.objects.all()
    info = info.order_by('-valued', '-pub_date')
    avg = Comment_and_Rating.objects.aggregate(Avg('rating'))
    count = Comment_and_Rating.objects.count()
    average = 0
    if count != 0: average = round((avg.pop('rating__avg')), 2)

    context = {
        'all_bookdetails': all_bookdetails,
        'info': info,
        'average': average,
        'count': count,
    }
    return render(request, 'list/bookdetails.html', context)


# return HttpResponse(template.render(context,request)

def shoppingcart(request):
    all_items = CartItems.objects.filter(cartId=1)  # showing information of Cart #1
    totalItems = list(all_items.aggregate(Sum('quantity')).values())[0]
    primary = all_items.values_list('productId', flat=True)
    total = BookDetails.objects.filter(pk__in=primary).aggregate(
        total=Sum(F('price') * F('cartitems__quantity'),
                  output_field=models.FloatField()))['total']
    saved_items = SavedForLater.objects.filter(cartId=1)
    totalsaveditems = saved_items.count()
    context = {'all_items': all_items,
               'totalItems': totalItems,
               'total': total,
               'saved_items': saved_items,
               'totalsaveditems': totalsaveditems,
               }

    return render(request, 'list/shoppingcart.html', context)


def removesc(request):  # shoppingcart remove
    item = CartItems.objects.get(pk=request.POST['item'])
    item.delete()
    return redirect('list/shoppingcart')


def removesfl(request):  # saved for later remove
    item = SavedForLater.objects.get(pk=request.POST['item'])
    item.delete()
    return redirect('list/shoppingcart')


def saveforlater(request):  # removes item from shopping cart and adds it to saved for later
    item = CartItems.objects.get(pk=request.POST['item'])
    b = SavedForLater(cartId=item.cartId, productId=item.productId)
    b.save()
    item.delete()
    return redirect('list/shoppingcart')


def addtocart(request):  # removes item from Saved for later and adds it to shopping cart
    item = SavedForLater.objects.get(pk=request.POST['item'])
    b = CartItems(cartId=item.cartId, productId=item.productId, quantity=1)
    b.save()
    item.delete()
    return redirect('list/shoppingcart')


def changequantity(request):  # removes item from Saved for later and adds it to shopping cart
    item = CartItems.objects.get(pk=request.POST['item'])
    item.quantity = request.POST['quantity']
    item.save()
    return redirect('list/shoppingcart')


def addtocart2(request):  # removes item from Saved for later and adds it to shopping cart
    selected_book = BookDetails.objects.get(pk=request.POST['item'])
    b = CartItems(cartId=Cart.objects.get(pk=1), productId=selected_book, quantity=1)
    b.save()
    return redirect('list/shoppingcart')

# this is used when a new comment is made and posted
def addComment(request):

    input = request.POST.get('ano', False)
    if (input):
        user = "Anonymous"
    else:
        user = "Testing" + str(random.randint(1,100))

    new_comment = Comment_and_Rating(username=user,
                                     content=request.POST['content'],
                                     rating=request.POST['star_value'],
                                     pub_date=date.today(),
                                     valued=0)
    new_comment.save()
    template = loader.get_template('list/bookdetails.html')
    return redirect ('list/bookdetails')


# Here we can delete the comments
def deleteComment(request, user_id):
    commet_to_delete = Comment_and_Rating.objects.get(username=user_id)
    commet_to_delete.delete()
    return render(request, 'list/bookdetails.html')


# This is for "upvoting" a comment
def helpful(request, user_id):
    new_value = Comment_and_Rating.objects.get(username=user_id)
    new_value.valued += 1
    new_value.save()
    return render(request, 'list/bookdetails.html')