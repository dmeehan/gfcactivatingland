from django.contrib import admin
from django.conf import settings

from flatblocks.models import FlatBlock

class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug',]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')

    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)