from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'products_in_category')
    list_editable = ('title',)
    fields = ('pk',
              'title',
              'description',
              'image')
    readonly_fields = ('pk',)
    search_fields = ('title', 'description', 'products__product__title',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(
            products_in_category=Count('products'),
        )
        return queryset

    def products_in_category(self, obj):
        return obj.products_in_category

    products_in_category.admin_order_field = 'products_in_category'
    products_in_category.short_description = _('Count of products in category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'category',
                    'price')
    list_editable = ('title', 'price')
    fields = ('pk',
              'title',
              'description',
              'category',
              'image',
              'price')
    autocomplete_fields = ('category',)
    readonly_fields = ('pk',)
    search_fields = ('title', 'description', 'category__title',)
    list_filter = ('category',)
