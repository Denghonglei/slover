from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()

router.register(r'goods_for', views.GoodsForIndexViewSet)
router.register(r'goods', views.GoodsViewSet)   #
router.register(r'urls', views.UrlsViewSet)
router.register(r'category',views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
