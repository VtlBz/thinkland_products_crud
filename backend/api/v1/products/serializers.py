from rest_framework import serializers

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from products.models import Category, Product
from products.es_documents import ProductDocument


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument

        fields = (
            'title',
            'description',
            'category',
        )
