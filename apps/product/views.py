from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.product.filters import CategoryCreatedFilterSet
from apps.product.models import Category
from apps.product.serializers import CategoryModelSerializer


@extend_schema(tags=['category'])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = IsAuthenticated,
    filter_backends = [DjangoFilterBackend , SearchFilter]
    filterset_class = CategoryCreatedFilterSet
    # filterset_fields = ['name']
    search_fields = "name",