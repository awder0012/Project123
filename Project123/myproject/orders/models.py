from django.db import models

class Order(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    payment = models.CharField(max_length=50)
    cart = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.fullname}"
    

