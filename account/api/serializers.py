from djoser.serializers import UserCreateSerializer
from account.models import Profile
from product.models import Product
from product.api.serializers import ProductSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_applications = serializers.SerializerMethodField()
    user_username = serializers.SerializerMethodField()
    user_date = serializers.SerializerMethodField()

    def get_user_applications(self, obj):
        queryset = Product.objects.filter(seller=obj.user)
        applications = ProductSerializer(queryset, many=True)
        return applications.data
       
    def get_user_username(self, obj):
        return obj.user.username

    def get_user_date(self, obj):
        return obj.user.created_at

    class Meta:
        model = Profile
        fields = '__all__'
