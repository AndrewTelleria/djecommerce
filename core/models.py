from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


# List of items that can be added to an order
# As soon as an item is added to the cart it becomes OrderItem
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })


# Links the item to the order
# Handles specific logic about the order item
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


# Link order items to the order.
# Essentially a shopping cart.
# Every time they login we fetch the order
# and display order as shopping cart item count.
# Define boolean field on order if it has been order.
# If not, this order will be used until it is ordered.
# As soon as it is ordered, the next order is created.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
