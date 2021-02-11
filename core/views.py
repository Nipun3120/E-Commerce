from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"

def check(request):
    context = {}
    return render(request, "checkout-page.html", context)

def products(request):
    context = {}
    return render(request, "product-page.html", context)
