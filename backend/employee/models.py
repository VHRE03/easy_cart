from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Employee(AbstractUser):
    # Opciones de rol
    ROLE_CHOICES = [
        ('BARISTA', 'Barista'),
        ('CASHIER', 'Cajero'),
        ('MANAGER', 'Gerente'),
        ('CHEF', 'Chef'),
        ('SERVER', 'Mesero'),
        ('SUPERVISOR', 'Supervisor'),
    ]
    username = models.CharField(max_length=100, unique=True, blank=None, null=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=100, blank=None, null=False)
    role = models.CharField(max_length=20, blank=True, choices=ROLE_CHOICES)
    hire_date = models.DateField(null=True, blank=True)
    
    last_login          = None
    date_joined         = None
    groups              = None
    user_permissions    = None

    def __str__(self):
        return f'{self.username} - {self.first_name} - {self.last_name} - {self.role}'
