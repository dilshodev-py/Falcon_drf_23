from django.db.models import Model, ForeignKey, CASCADE, SmallIntegerField, DateTimeField, SET_NULL, CharField, \
    TextChoices


class Cart(Model):
    product = ForeignKey('product.Product' , CASCADE , related_name='carts')
    amount = SmallIntegerField()
    order = ForeignKey('orders.Order', SET_NULL, null=True, blank=True)


    created_at = DateTimeField(auto_now_add=True)


class Region(Model):
    name = CharField(max_length=255)

class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('orders.Region', CASCADE, related_name='districts')


class Order(Model):
    class StatusMethod(TextChoices):
        COMPLETED = 'completed', 'Completed'
        PROCESSING = 'processing', 'Processing'
        ON_HOLD = 'on hold', 'On Hold'
        PENDING = 'pending', 'Pending'

    class PaymentMethod(TextChoices):
        PAYPAL = 'paypal', 'Paypal'
        CREDIT_CARD = 'credit_card', 'Credit_card'

    owner = ForeignKey('users.User', CASCADE, related_name='orders')
    status = CharField(max_length=50 , choices=StatusMethod.choices , default=StatusMethod.PROCESSING)
    payment_method = CharField(max_length=50 , choices=PaymentMethod.choices , default=PaymentMethod.PAYPAL)
    address = ForeignKey('orders.District', SET_NULL, null=True, blank=True, related_name='orders')
    created_at = DateTimeField(auto_now_add=True)





