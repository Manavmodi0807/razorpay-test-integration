import razorpay
from django.conf import settings
from django.shortcuts import render

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def index(request):
    amount = 50000  # = ₹500 (paise)

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "order": order,
        "key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "payments/index.html", context)


def success(request):
    return render(request, "payments/success.html")