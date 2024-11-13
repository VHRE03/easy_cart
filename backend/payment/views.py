from rest_framework import viewsets
from .models import Payment
from .serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('id')
    serializer_class = PaymentSerializer