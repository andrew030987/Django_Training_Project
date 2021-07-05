from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Slider


class CmsAdmin(admin.ModelAdmin):
    list_display = ('slider_name', 'slider_text', 'slider_css_class', 'get_img')
    list_display_links = ('slider_name',)
    list_editable = ('slider_css_class',)
    fields = ('slider_name', 'slider_text', 'slider_css_class', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.slider_img:
            return mark_safe(f'<img src="{obj.slider_img.url}" width=80px')
        else:
            return 'No image'

    get_img.short_description = 'Picture'

admin.site.register(Slider, CmsAdmin)
