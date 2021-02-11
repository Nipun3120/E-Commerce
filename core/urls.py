from django.urls import path
from .views import HomeView, check, products

app_name = 'core' 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', check, name='check'),
    path('products/', products, name='products'),
]
