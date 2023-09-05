from django.db import models
from django.conf import settings
from product.models import Product


class WishList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wish List'

    def __str__(self):
        return f"{self.user.username}'s wishlist"
