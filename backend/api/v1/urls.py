# /api/v1/

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.products.urls import router_v1_products


router_v1 = DefaultRouter()

router_v1.registry.extend(router_v1_products.registry)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('users/', include('api.v1.users.urls')),
]
