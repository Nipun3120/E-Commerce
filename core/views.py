from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
from django.shortcuts import reverse

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

def check(request):
    context = {}
    return render(request, 'checkout-page.html', context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
    



