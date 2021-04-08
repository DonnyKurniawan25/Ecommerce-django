from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Items, Order, Orderitem

# Create your views here.

class IndexView(ListView):
	model = Items
	template_name = 'user/index.html'

def shop(request):
	return render(request, "user/shop.html")
