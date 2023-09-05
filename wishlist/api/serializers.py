from rest_framework import serializers
from product.api.serializers import ProductSerializer
from wishlist.models import WishList
from account.api.serializers import UserSerializer


class WishListSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    product_info = serializers.SerializerMethodField()

    def get_user_info(self, obj):
        return UserSerializer(obj.user).data

    def get_product_info(self, obj):
        return ProductSerializer(obj.product).data

    class Meta:
        model = WishList
        fields = '__all__'
