from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


# Make sure to sync up with database after adding attributes
# python manage.py makemigrations list
# then python manage.py migrate
class WishList(models.Model):
    wishlist_title = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('list:index')

    def __str__(self):
        return self.wishlist_title


class Book(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=250)

    def __str__(self):
        return self.book_title


class BookDetails(models.Model):
    author = models.CharField(max_length=200)
    authorbio = models.CharField(max_length=200)
    authorhyperlink = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    publisherinfo = models.CharField(max_length=200)
    coverphotourl = models.CharField(max_length=1000,
                                     default='https://upload.wikimedia.org/wikipedia/commons/b/b9/No_Cover.jpg')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99)



class Product(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.CharField(max_length=1000,
                             default='https://upload.wikimedia.org/wikipedia/commons/b/b9/No_Cover.jpg')

    def __unicode__(self):
        return unicode(self.pk)


class Cart(models.Model):
    userId = models.IntegerField()


class CartItems(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(BookDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class SavedForLater(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(BookDetails, on_delete=models.CASCADE)

# ANDY
class Comment_and_Rating(models.Model):
	username = models.CharField(max_length=20, primary_key=True, blank=True, null=False)
	content = models.TextField(db_column='User_Comment', blank=True, null=True)
	rating = models.IntegerField(db_column='User_Rating', blank=True, null=True)
	pub_date = models.DateField(db_column='Date_Posted', blank=True, null=True)
	valued = models.IntegerField(db_column='Helpfulness', blank=True, null=True)

# wishlistname = WishList.objects.get(pk=1)
# wishlistname.book_set.all() reveals the set of books within the wishlist
# Create new books with wishlistname.book_set.create(set all attributes here)
