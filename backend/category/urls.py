from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
