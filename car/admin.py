from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
                    f'<a href="{object.car_photo.url}" target="_blank"><img src="{object.car_photo.url}" width="60" style="border-radius: 5px"/></a>'
                )

    thumbnail.shot_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'model', 'year','features', 'created_date','is_featured', 'price')
    list_display_links = ['id', 'thumbnail', 'car_title']
    list_filter = ['created_date', 'car_title', 'model', 'year']
    search_fields = [ 'car_title', 'features', 'state', 'year', 'model']
    list_editable = ['is_featured']

admin.site.register(Car, CarAdmin)


