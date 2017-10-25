from django.conf.urls import url

from activity.views import get_all_activities

urlpatterns = [
    url(r'^get-all-activities/$', get_all_activities, name='get_all_activities_url'),
]
