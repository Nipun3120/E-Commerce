from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField


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
    image = models.ImageField(blank=True, null=True)
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
        return f"{self.quantity} of {self.item.title}, user: {self.user}"

    def get_total_price(self):
        return self.quantity * self.item.price
    def get_total_price_discount(self):
        return self.quantity * self.item.discounted_price
    def get_price_saved(self):
        return self.get_total_price() - self.get_total_price()

    def get_final_price(self):
        if self.item.discounted_price:
            return self.get_total_price_discount()
        return self.get_total_price()

    def get_total_actual_price(self):
        return self.get_total_price()




class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)    
    start_date=models.DateTimeField(auto_now_add=True)
    order_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total_price = 0
        for item_price in self.items.all():
            total_price += item_price.get_final_price()
        return total_price

    def get_total_actual(self):
        total_price = 0
        for item_price in self.items.all():
            total_price += item_price.get_total_actual_price()
        return total_price - self.get_total()

    # def get_extra_discount(self):
    #     final_price = self.get_total()
    #     if final_price > 5000:
    #         return final_price - (final_price*10/100)

    
class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=256)
    apartment_address = models.CharField(max_length=256)
    country = CountryField(multiple=False)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return self.user.username
