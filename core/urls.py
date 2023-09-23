from django.urls import path

from core.api import api

app_name = 'recipes'

urlpatterns = [
    path('', api.list_profile_api, name="api"),
    path('<int:pk>', api.detail_profile_api, name="api"),
    path('project/', api.project_list, name="api")
]