from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from blog.models import Goods, UrlList, Category
from blog.serializers import GoodsSerializer, UrlListSerializer, CategorySerializer, GoodsForIndexSerializer


class GoodsViewSet(ModelViewSet):
    # authentication_classes = []
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("user",)

class UrlsViewSet(ModelViewSet):
    # authentication_classes = []
    queryset = UrlList.objects.all()
    serializer_class = UrlListSerializer
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("user",)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)

# 首页商品详情展示
class GoodsForIndexViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsForIndexSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['detail', ]
    ordering = ['-id',]

