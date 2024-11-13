from django.db import models
from order.models import Order

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('MOBILE_PAYMENT', 'Mobile Payment'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('ONLINE_PAYMENT', 'Online Payment'),
        ('GIFT_CARD', 'Gift Card'),
    ]
    
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    