from django.http import HttpResponse

from activity.models import Activity
import json


def get_all_activities(request):
    if request.method == 'GET':
        result = []
        for activity in Activity.objects.all():
            result.append({
                'key': activity.pk,
                'name': activity.name,
                'slug': activity.slug
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
