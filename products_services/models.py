from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()


class JsonTable(models.Model):
    name = models.CharField(max_length=50)
    data = models.JSONField()


class Table(models.Model):
    name = models.CharField(max_length=50)
    column1 = models.CharField(max_length=30)
    column2 = models.CharField(max_length=30)
    column3 = models.CharField(max_length=30, blank=True, null=True)
    column4 = models.CharField(max_length=30, blank=True, null=True)
    column5 = models.CharField(max_length=30, blank=True, null=True)


class LineTable(models.Model):
    column1 = models.CharField(max_length=70)
    column2 = models.CharField(max_length=70)
    column3 = models.CharField(max_length=70, blank=True, null=True)
    column4 = models.CharField(max_length=70, blank=True, null=True)
    column5 = models.CharField(max_length=70, blank=True, null=True)
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='lines'
    )


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Информация о товаре')
    image = models.ManyToManyField(
        Image,
        related_name='product',
    )
    table = models.ManyToManyField(
        Table,
        related_name='product',
    )


class ProductsTable(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
