from django.urls import path
from .views import HomeView, check, ItemDetailView

app_name = 'core' 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', check, name='check'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
