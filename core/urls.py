from django.urls import path
from .views import HomeView, check, ItemDetailView, add_to_cart, remove_from_cart, OrderSummaryView

app_name = 'core' 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', check, name='check'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('order_summary/', OrderSummaryView.as_view(), name='order_summary'),
]
 