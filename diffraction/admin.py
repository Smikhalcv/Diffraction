from django.contrib import admin
from .models import AboutCompany, DirectionOfActivity

# Register your models here.
class DirectionInline(admin.TabularInline):
    model = DirectionOfActivity

@admin.register(AboutCompany)
class AdminAboutCompany(admin.ModelAdmin):
    inlines = [
        DirectionInline
    ]

@admin.register(DirectionOfActivity)
class AdminDirectionOfActivity(admin.ModelAdmin):
    ...