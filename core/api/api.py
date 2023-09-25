from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from usuario.models import Profile
from core.models import *
from rest_framework import status
from ..models import Projeto


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
    project = Projeto.objects.all()
    serializer = ProjetoSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_project(request, pk):
    profile = Projeto.objects.filter(pk=pk).first()
    if profile:
        serializer = ProjetoSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def equipe_list(request):
    project = Equipe.objects.all()
    serializer = EquipeSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_equipe(request, pk):
    profile = Equipe.objects.filter(pk=pk).first()
    if profile:
        serializer = EquipeSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )


@api_view()
def tarefa_list(request):
    project = Tarefa.objects.all()
    serializer = TarefaSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_tarefa(request, pk):
    profile = Tarefa.objects.filter(pk=pk).first()
    if profile:
        serializer = TarefaSerializer(instance=profile, many=False)
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
    project = Comentario.objects.all()
    serializer = ComentarioSerializer(instance=project, many=True)
    return Response(serializer.data)


@api_view()
def detail_comentario(request, pk):
    profile = Comentario.objects.filter(pk=pk).first()
    if profile:
        serializer = ComentarioSerializer(instance=profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'EITA:NÂO DEU CERTO'},
                        status=status.HTTP_404_NOT_FOUND
                        )