from django.urls import include, path
from rest_framework import routers
from .views import PaymentViewSet

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
