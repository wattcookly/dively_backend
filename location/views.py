from django.http import HttpResponse

from location.models import Country, City
import json


def get_all_countries(request):
    if request.method == 'GET':
        result = []
        for country in Country.objects.all():
            result.append({
                'key': country.pk,
                'name': country.name,
                'slug': country.slug
            })
        response = HttpResponse(
            json.dumps(result),
            content_type='application/json'
        )
        return response
    else:
        return HttpResponse(
            'Bad request',
            status_code=400,
            content_type='application/json')


def get_all_cities(request):
    if request.method == 'GET':
        result = []
        for city in City.objects.all():
            result.append({
                'key': city.pk,
                'name': city.name,
                'slug': city.slug
            })
        response = HttpResponse(
            json.dumps(result),
            content_type='application/json'
        )
        return response
    else:
        return HttpResponse(
            'Bad request',
            status_code=400,
            content_type='application/json')
