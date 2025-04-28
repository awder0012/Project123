from django.urls import path
from .views import submit_order

urlpatterns = [
    path("submit_order/", submit_order, name="submit_order"),
]
