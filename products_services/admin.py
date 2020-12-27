from django.contrib import admin


from .models import JsonTable, Table, LineTable, Products, Image


# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ...


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    ...


@admin.register(JsonTable)
class JsonTableAdmin(admin.ModelAdmin):
    ...


class LineTableInline(admin.TabularInline):
    model = LineTable

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    inlines = [
        LineTableInline,
    ]

@admin.register(LineTable)
class LineTableAdmin(admin.ModelAdmin):
    ...