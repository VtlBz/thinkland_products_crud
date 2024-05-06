import os

ES_HOST: str = os.getenv('ES_HOST', 'localhost')
ES_PORT: str = os.getenv('ES_PORT', '9200')

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': f'http://{ES_HOST}:{ES_PORT}',
        'verify_certs': False
    },
}

ELASTICSEARCH_INDEX_NAMES = {
    'products.product': 'product_index',
}
