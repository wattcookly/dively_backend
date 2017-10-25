from django.contrib import admin
from location.models import Country, City


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'ordering', 'visible')
    prepopulated_fields = {'slug': ('name',), }
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'country', 'ordering', 'visible')
    prepopulated_fields = {'slug': ('name',), }
    search_fields = ['name']


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
