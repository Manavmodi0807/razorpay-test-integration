from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    signature = models.CharField(max_length=500)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default="created")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id