from django_filters import DateTimeFilter
from django_filters.rest_framework import FilterSet

from apps.product.models import Category


class CategoryCreatedFilterSet(FilterSet):
    date_from = DateTimeFilter('created_at' , lookup_expr='gte')
    date_to = DateTimeFilter('created_at' , lookup_expr='lte')

    class Meta:
        model = Category
        fields = ["date_from", "date_to"]


