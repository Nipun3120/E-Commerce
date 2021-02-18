from django.http import HttpResponseRedirect, request, HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import RequestContext

from django.views.generic import ListView, DetailView, View
from .models import Item, Order, OrderItem, BillingAddress
# from .forms import CheckoutForm
from .forms import CheckoutForm

class HomeView(ListView):
    model = Item
    paginate_by = 4
    template_name = 'home-page.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        try:
            order = Order.objects.get(user = self.request.user, ordered=False)
            context = {
                'object': order, 
            }
            return render(self.request, 'order_summary.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request, 'checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user = self.request.user, ordered=False)
            context = {
                'object': order, 
            }

            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zipcode = form.cleaned_data.get('zipcode')

                # same_shipping_address = form.cleaned_data.get('same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                # payment_option = form.cleaned_data.get('payment_option')

                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zipcode = zipcode,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                
                
                return redirect('core:check')
        

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
        messages.warning(self.request, 'invalid form')

        return redirect('core:check')



class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'product.html'
    

@login_required
def add_to_cart(request, slug):    
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():

            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The item was updated in your cart")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added into your cart")
    else:
        order_date = timezone.now()
        order = Order.objects.create(
            user=request.user, 
            order_date=order_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added into your cart")
        
    return redirect('core:order_summary')


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            return redirect("core:order_summary")

        else:
            messages.info(request, "You do not have this item in your cart")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

@login_required
def decrease_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
            else:
                order.items.remove(order_item)
            order_item.save()
            return redirect('core:order_summary')
            

@login_required
def increase_item_in_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity += 1
            order_item.save()
            return redirect('core:order_summary')

