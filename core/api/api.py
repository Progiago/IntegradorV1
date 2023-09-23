from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer, ProjetoSerializer
from usuario.models import Profile
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
