from django.urls import path

from core.api import api

app_name = 'recipes'

urlpatterns = [
    path('', api.List_profile.as_view()),

    path('<int:pk>', api.Detail_profile.as_view()),

    path('project/', api.Project_List.as_view()),

    path('project/<int:pk>', api.Detail_project.as_view()),

    path('equipe/', api.Team_List.as_view()),

    path('equipe/<int:pk>', api.Detail_Team.as_view()),

    path('tarefa/', api.Task_List.as_view()),

    path('tarefa/<int:pk>', api.Detail_Task.as_view()),
    
    path('tarefa/<int:task>/tags', api.TagsToTask.as_view()),

    path('checklist/', api.Checklist_List.as_view()),

    path('checklist/<int:pk>', api.Detail_Task.as_view()),

    path('comentarios/', api.Comment_List.as_view()),

    path('comentario/<int:pk>', api.Detail_Comment.as_view()),

    path('project/<int:project>/tarefa', api.ProjectToTask.as_view()),

    path('<int:profile>/project', api.UserToProject.as_view()),
    
    path('tags/', api.Tags_List.as_view()),
    
    path('tags/<int:pk>', api.Detail_Tags.as_view()),
]