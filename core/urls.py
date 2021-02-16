from django.urls import path
from .views import HomeView, ItemDetailView, add_to_cart, remove_from_cart, OrderSummaryView, decrease_item_from_cart, increase_item_in_cart, CheckoutView

app_name = 'core' 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('checkout/', check, name='check'),
    path('checkout', CheckoutView.as_view(), name='check'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('order_summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('decrease_item_from_cart/<slug>', decrease_item_from_cart, name='decrease_item_from_cart'),
    path('increase_item_in_cart/<slug>', increase_item_in_cart, name='increase_item_in_cart'),
    # path('add_to_whishlist/<slug>', add_to_whishlist, name='add_to_whishlist'),
    # path('wishist/', WishList.as_view(), name='wishlist')

]
 