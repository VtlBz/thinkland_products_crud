from django.core.validators import (MinLengthValidator,
                                    MinValueValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('title',)

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(
                1, _('Title cannot be shorter than 1 character')
            )
        ]
    )

    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='category_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.title)


class Product(models.Model):

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('title',)

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        unique=True,
        db_index=True,
        validators=[
            MinLengthValidator(
                1, _('Title cannot be shorter than 1 character')
            )
        ]
    )

    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='product_images/',
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Price'),
        validators=[
            MinValueValidator(
                0, _('Minimal price cannot be less than zero')
            ),
        ],
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )

    def __str__(self):
        return str(self.title)
