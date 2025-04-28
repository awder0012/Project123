from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Order

@csrf_exempt
def submit_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            order = Order.objects.create(
                fullname=data.get("fullname"),
                address=data.get("address"),
                phone=data.get("phone"),
                payment=data.get("payment"),
                cart=data.get("cart"),
            )
            return JsonResponse({"success": True, "order_id": order.id})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    elif request.method == "GET":
        orders = Order.objects.all().values()
        return JsonResponse(list(orders), safe=False)

    return JsonResponse({"success": False, "message": "Method not allowed"}, status=405)
