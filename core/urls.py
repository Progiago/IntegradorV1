from django.urls import path

from core.api import api

app_name = 'recipes'

urlpatterns = [
    path('', api.List_profile, name="api"),
    path('<int:pk>', api.Detail_profile, name="api"),
    path('project/', api.Project_List, name="api"),
    path('project/<int:pk>', api.Detail_project, name="api"),
    path('equipe/', api.Team_List, name="api"),
    path('equipe/<int:pk>', api.detail_equipe, name="api"),
    path('tarefa/', api.tarefa_list, name="api"),
    path('tarefa/<int:pk>', api.detail_tarefa, name="api"),
    path('checklist/', api.checklist_list, name="api"),
    path('checklist/<int:pk>', api.detail_checklist, name="api"),
    path('comentarios/', api.comentario_list, name="api"),
    path('comentario/<int:pk>', api.detail_comentario, name="api"),
]