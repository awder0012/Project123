from django.db import models

class Order(models.Model):
    fullname = models.CharField(max_length=255)     # เพิ่ม fullname
    address = models.TextField()
    phone = models.CharField(max_length=20)          # เพิ่ม phone
    payment = models.CharField(max_length=50)        # เพิ่ม payment
    cart = models.JSONField()                        # เพิ่ม cart เป็น JSONField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
