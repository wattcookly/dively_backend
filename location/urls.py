from django.conf.urls import url

from location.views import get_all_countries, get_all_cities

urlpatterns = [
    url(r'^get-all-countries/$', get_all_countries, name='get_all_countries_url'),
    url(r'^get-all-cities/$', get_all_cities, name='get_all_cities_url'),
]
