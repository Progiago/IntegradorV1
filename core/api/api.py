from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from usuario.models import Profile
from core.models import *
from rest_framework import status


@api_view()
def list_profile_api(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(instance=profile, many=True)
    return Response(serializer.data)


@api_view()
def detail_profile_api(request, pk):
    profile = Profile.objects.filter(pk=pk).first()
    if profile:
        serializer = ProfileSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def project_list(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_project(request, pk):
    profile = Project.objects.filter(pk=pk).first()
    if profile:
        serializer = ProjectSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def equipe_list(request):
    project = Team.objects.all()
    serializer = TeamSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_equipe(request, pk):
    profile = Team.objects.filter(pk=pk).first()
    if profile:
        serializer = TeamSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def tarefa_list(request):
    project = Task.objects.all()
    serializer = TaskSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_tarefa(request, pk):
    profile = Task.objects.filter(pk=pk).first()
    if profile:
        serializer = TaskSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def checklist_list(request):
    project = Checklist.objects.all()
    serializer = ChecklistSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_checklist(request, pk):
    profile = Checklist.objects.filter(pk=pk).first()
    if profile:
        serializer = ChecklistSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def comentario_list(request):
    project = Comment.objects.all()
    serializer = CommentSerializer(instance=project, many=True)
    return Response(serializer.data)


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
