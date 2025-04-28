from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),  # เพิ่ม name ให้
    path('menu/', views.menu_view, name='menu'),
    path('pro/', views.pro_view, name='pro'),
    path('re/', views.re_view, name='re'),
    path('contact/', views.contact_view, name='contact'),
    path('cart/', views.cart_view, name='cart'),
    path('order/', views.order_view, name='order'),
    
    path('api/orders/', views.order_list_api, name='order_list_api'),  # ✅ API ดึงข้อมูล
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
]
