# /api/v1/products/

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductDocumentView, ProductViewSet

router_v1_products = DefaultRouter()

router_v1_products.register(
    'categories',
    CategoryViewSet,
    basename='categories',
)

router_v1_products.register(
    'products',
    ProductViewSet,
    basename='products',
)

router_v1_products.register(
    'products-search',
    ProductDocumentView,
    basename='products-search')
