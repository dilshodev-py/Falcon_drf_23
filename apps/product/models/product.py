from django.db.models import CharField, DecimalField, SmallIntegerField, JSONField, ForeignKey, CASCADE
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared import SlugBaseModel


class Product(SlugBaseModel):
    description = CKEditor5Field(config_name='extends')
    price = DecimalField(decimal_places=2, max_digits=9)
    shipping_cost = SmallIntegerField()
    quantity = SmallIntegerField(default=1)
    discount = SmallIntegerField()

    created_by = ForeignKey('users.User', CASCADE, related_name='products')
    category = ForeignKey('product.Category', CASCADE, related_name='products')

    spec = JSONField()
