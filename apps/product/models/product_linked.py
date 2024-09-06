from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField, TextChoices, ImageField, \
    SmallIntegerField
from mptt.models import MPTTModel, TreeForeignKey

from apps.shared import SlugBaseModel


class Category(MPTTModel , SlugBaseModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Comment(Model):
    class RatingChoose(TextChoices):
        EXCELLENT = 5
        GOOD = 4
        AVERAGE = 3
        BAD = 2
        AWFUL = 1

    name = CharField(max_length=255)
    message = TextField()
    owner = ForeignKey('users.User', CASCADE, related_name='comments')
    rating = SmallIntegerField(default=RatingChoose.EXCELLENT, choices=RatingChoose.choices)
    product = ForeignKey('product.Product', CASCADE, related_name='comments')
    created_at = DateTimeField(auto_now_add=True)


class ProductImage(Model):
    product = ForeignKey('product.Product', CASCADE, related_name='images')
    image = ImageField(upload_to='product/images/')

