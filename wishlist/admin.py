from django.contrib import admin
from .models import WishList


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'created_at']


admin.site.register(WishList, WishListAdmin)
