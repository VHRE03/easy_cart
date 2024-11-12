from django.urls import include, path
from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
