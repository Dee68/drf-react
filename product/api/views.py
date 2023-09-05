from rest_framework import (
    views,
    generics,
    status)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    )
from product.models import Category, Product


class CategoryApiView(views.APIView):

    def get(self, request):
        queryset = Category.objects.viewable()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategorySingleApiView(views.APIView):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)


class ProductApiView(generics.ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
