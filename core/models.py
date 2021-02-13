from django.conf import settings
from django.db import models
from django.shortcuts import reverse
# Create your models here.

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear'),
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=256)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug':self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={'slug':self.slug})
    
    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={'slug':slug})



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True)
    
    quantity = models.IntegerField(default=1)           #gets the count of the items ordered

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_price(self):
        return self.quantity * self.item.price
    def get_total_price_discount(self):
        return self.quantity * self.item.discounted_price


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)    
    start_date=models.DateTimeField(auto_now_add=True)
    order_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

