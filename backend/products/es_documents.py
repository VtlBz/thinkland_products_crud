from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product


@registry.register_document
class ProductDocument(Document):
    title = fields.TextField(
        attr='title',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    description = fields.TextField(
        attr='description',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    category = fields.ObjectField(
        attr='category',
        properties={
            'id': fields.IntegerField(),
            'title': fields.TextField(
                attr='title',
                fields={
                    'raw': fields.KeywordField(),
                }
            )
        }
    )

    class Index:
        name = 'product_index'

    class Django:
        model = Product
