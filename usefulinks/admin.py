from django.contrib import admin
from .models import UsefulLink
from django.utils.html import format_html

@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description', 'image_preview')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "Немає зображення"
    image_preview.short_description = 'Попередній перегляд'
