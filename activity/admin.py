from django.contrib import admin
from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'city', 'ordering', 'visible')
    prepopulated_fields = {'slug': ('name',), }
    search_fields = ['name']


admin.site.register(Activity, ActivityAdmin)
