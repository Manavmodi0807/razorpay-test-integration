import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Payment

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def index(request):
    amount = 50000

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    Payment.objects.create(
        order_id=order["id"],
        amount=amount,
        status="created"
    )

    return render(request, "payments/index.html", {
        "order": order,
        "key": settings.RAZORPAY_KEY_ID
    })


@csrf_exempt
def success(request):
    if request.method == "POST":
        payment_id = request.POST.get("razorpay_payment_id")
        order_id = request.POST.get("razorpay_order_id")
        signature = request.POST.get("razorpay_signature")

        params_dict = {
            "razorpay_payment_id": payment_id,
            "razorpay_order_id": order_id,
            "razorpay_signature": signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)

            payment = Payment.objects.get(order_id=order_id)
            payment.payment_id = payment_id
            payment.signature = signature
            payment.status = "paid"
            payment.save()

            return render(request, "payments/success.html")

        except:
            return render(request, "payments/failure.html")

    return render(request, "payments/failure.html")