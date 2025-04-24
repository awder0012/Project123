from django.shortcuts import render
from .models import CoffeeItem

# Create your views here.
def index(request):
    items = CoffeeItem.objects.all()
    return render(request, 'menu/index.html', {'items': items})
