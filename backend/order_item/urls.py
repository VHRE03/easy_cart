from django.urls import include, path
from rest_framework import routers
from .views import OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
