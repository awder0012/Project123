from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import OrderForm
from orders.models import Order
import json

# หน้าเพจทั่วไป
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def menu_view(request):
    return render(request, "menu.html")

def pro_view(request):
    return render(request, "pro.html")

def re_view(request):
    return render(request, "re.html")

def contact_view(request):
    return render(request, "contact.html")

def cart_view(request):
    return render(request, "cart.html")

# ฟอร์มการสั่งซื้อ
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order_items = request.POST.get('order_items')
        total_price = request.POST.get('total_price')

        if form.is_valid():
            order = form.save(commit=False)
            order.order_items = order_items
            order.total_price = total_price
            order.save()
            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})

# API ดึงรายการคำสั่งซื้อ
def order_list_api(request):
    orders = Order.objects.all().values('id', 'fullname', 'address', 'order_items', 'payment', 'total_price', 'created_at')
    orders_list = list(orders)

    # แปลง datetime เป็น string เพื่อ JSON ไม่ error
    for order in orders_list:
        order['created_at'] = order['created_at'].strftime('%Y-%m-%d %H:%M:%S')

    return JsonResponse(orders_list, safe=False)

# หน้าแสดงรายการคำสั่งซื้อ (ใหม่)
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')  # เรียงใหม่ล่าสุดก่อน
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    return render(request, 'order_detail.html', {'order': order})