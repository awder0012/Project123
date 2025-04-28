from django.contrib import admin
from .models import Order
from django.utils.html import format_html

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "address", "short_cart", "payment", "total_price", "created_at")
    readonly_fields = ("created_at", "cart_pretty", "address", "total_price")

    fieldsets = (
        (None, {
            'fields': ("fullname", "phone", "payment", "address", "cart_pretty", "total_price", "created_at")
        }),
    )

    def cart_pretty(self, obj):
        try:
            items = obj.cart
            html = "<ul>"
            for item in items:
                html += f"<li>{item['title']} - {item['price']} บาท</li>"
            html += "</ul>"
            return format_html(html)
        except Exception as e:
            return f"❌ Error in cart: {e}"

    cart_pretty.short_description = "รายการสินค้า"

    def short_cart(self, obj):
        try:
            return ", ".join(item['title'] for item in obj.cart)
        except:
            return "-"
    short_cart.short_description = "เมนู"

    def total_price(self, obj):
        try:
            total = sum(item['price'] for item in obj.cart)
            return f"{total} บาท"
        except:
            return "-"
    total_price.short_description = "ราคารวม"
