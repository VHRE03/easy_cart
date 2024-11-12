from django.db import models
from employee.models import Employee

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
        ('PARTIALLY_REFUNDED', 'Partially Refunded'),
        ('PROCESSING', 'Processing'),
        ('ON_HOLD', 'On Hold'),
    ]
    
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    created_at = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.id} - {self.total_amount} - {self.payment_status} - {self.created_at} - {self.employee}'