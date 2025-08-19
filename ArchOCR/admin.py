from django.contrib import admin
from .models import ScanPage, Translation


@admin.register(ScanPage)
class ScanPageAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "uploaded_at", "image")
    search_fields = ("owner__username",)
    list_filter = ("uploaded_at",)


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "page", "model_name", "created_at")
    list_filter = ("model_name", "created_at")
    search_fields = ("model_name", "page__id")
