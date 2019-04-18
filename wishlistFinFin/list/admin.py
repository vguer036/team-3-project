from django.contrib import admin
from .models import WishList, Book, BookDetails, Product, Cart, CartItems, SavedForLater

admin.site.register(WishList)
admin.site.register(Book)
admin.site.register(BookDetails)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(SavedForLater)
