from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from usuario.models import Profile
from core.models import *
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def list_profile_api(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(instance=profile, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_profile_api(request, pk):
    profile = get_object_or_404(Profile.objects.filter(pk=pk).first())
    if request.method == 'GET':
        serializer = ProfileSerializer(instance=profile, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ProfileSerializer(
            instance=profile, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(instance=project, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_project(request, pk):
    project = get_object_or_404(Profile.objects.filter(pk=pk).first())
    if request.method == 'GET':
        serializer = ProjectSerializer(instance=project, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ProjectSerializer(
            instance=project, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view(['GET', 'POST'])
def equipe_list(request):
    if request.method == 'GET':
        team = Team.objects.all()
        serializer = TeamSerializer(instance=team, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_equipe(request, pk):
    team = get_object_or_404(Team.objects.filter(pk=pk).first())
    if request.method == 'GET':
        serializer = TeamSerializer(instance=team, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TeamSerializer(
            instance=team, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view(['GET', 'POST'])
def tarefa_list(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(instance=task, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_tarefa(request, pk):
    task = get_object_or_404(Task.objects.filter(pk=pk).first())
    if request.method == 'GET':
        serializer = TaskSerializer(instance=task, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TaskSerializer(
            instance=task, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view(['GET', 'POST'])
def checklist_list(request):
    if request.method == 'GET':
        checklist = Checklist.objects.all()
        serializer = ChecklistSerializer(instance=checklist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_checklist(request, pk):
    checklist = get_object_or_404(Checklist.objects.filter(pk=pk).first())
    if request.method == 'GET':
        serializer = ChecklistSerializer(instance=checklist, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ChecklistSerializer(
            instance=checklist, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view(['GET', 'POST'])
def comentario_list(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(instance=comment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response('POST', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def detail_comentario(request, pk):
    profile = Comment.objects.filter(pk=pk).first()
    if profile:
        serializer = CommentSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )
