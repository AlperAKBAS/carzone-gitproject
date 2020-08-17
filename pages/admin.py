from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            f'<img src="{object.photo.url}" width="60" style="border-radius: 50%"/>'
        )

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ['id', 'thumbnail']
    # list_editable = ['first_name', 'last_name', 'designation']

    list_filter = ['created_date', 'designation']
    search_fields = ['first_name', 'last_name', 'designation']

    
admin.site.register(Team, TeamAdmin)
