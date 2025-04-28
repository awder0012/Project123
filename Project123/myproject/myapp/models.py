from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    order_items = models.TextField()  # จะเก็บเป็น JSON text
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.total_price} บาท"
    
class ContactInfo(models.Model):
    address = models.TextField(verbose_name="ที่อยู่")
    phone = models.CharField(max_length=50, verbose_name="เบอร์โทร")
    email = models.EmailField(verbose_name="อีเมล")

    def __str__(self):
        return "ข้อมูลติดต่อร้าน"
