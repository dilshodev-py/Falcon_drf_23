from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug',)