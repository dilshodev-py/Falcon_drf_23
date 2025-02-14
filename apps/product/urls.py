from django.urls import path, include
from rest_framework import routers

from apps.product.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
urlpatterns = [
    path('' , include(router.urls))
]
