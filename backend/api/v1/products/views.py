from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import (BaseDocumentViewSet,
                                                   SuggestMixin)

from products.es_documents import ProductDocument
from products.models import Category, Product
from utils.paginations import ProductsPagination

from .serializers import (CategorySerializer,
                          ProductDocumentSerializer,
                          ProductSerializer)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class ProductDocumentView(BaseDocumentViewSet,
                          SuggestMixin):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = ('title', 'description')

    filter_fields = {
        'category': 'category.id'
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        'description': {
            'field': 'description.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
