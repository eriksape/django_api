from django.contrib import admin

from api.models import Scraper


@admin.register(Scraper)
class ScraperAdmin(admin.ModelAdmin):
    list_display = (
        'currency',
        'frequency',
        'value',
        'created_at',
        'value_updated_at',
    )
    ordering = ('currency', 'frequency', 'value', 'created_at', 'value_updated_at',)
    readonly_fields = ('created_at', 'value_updated_at',)
    search_fields = ('currency', 'frequency', 'value',)
