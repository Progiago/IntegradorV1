from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from usuario.models import Profile
from core.models import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class List_profile(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['GET', 'POST'])
# def list_profile_api(request):
#     if request.method == 'GET':
#         profile = Profile.objects.all()
#         serializer = ProfileSerializer(instance=profile, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Detail_profile(APIView):
    def get_profile(self, pk):
        profile = Profile.objects.filter(pk=pk).first()
        return profile
    
    def get(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(instance=profile, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(
            instance=profile, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PATCH', 'DELETE'])
# def detail_profile_api(request, pk):
#     profile = Profile.objects.filter(pk=pk).first()
#     if request.method == 'GET':
#         serializer = ProfileSerializer(instance=profile, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = ProfileSerializer(
#             instance=profile, data=request.data, many=False)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )


class Project_List(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def project_list(request):
#     if request.method == 'GET':
#         project = Project.objects.all()
#         serializer = Project(instance=project, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Detail_project(APIView):
    def get_profile(self, pk):
        project = Project.objects.filter(pk=pk).first()
        return project
    
    def get(self, request, pk):
        project = self.get_profile(pk)
        serializer = ProjectSerializer(instance=project, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        project = self.get_profile(pk)
        serializer = ProjectSerializer(
            instance=project, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        project = self.get_profile(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# @api_view(['GET', 'PATCH', 'DELETE'])
# def detail_project(request, pk):
#     project = get_object_or_404(Profile.objects.filter(pk=pk).first())
#     if request.method == 'GET':
#         serializer = ProjectSerializer(instance=project, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = ProjectSerializer(
#             instance=project, data=request.data, many=False)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )
class Team_List(APIView):
    def get(self, request, format=None):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def equipe_list(request):
#     if request.method == 'GET':
#         team = Team.objects.all()
#         serializer = TeamSerializer(instance=team, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TeamSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Detail_Team(APIView):
    def get_profile(self, pk):
        project = Team.objects.filter(pk=pk).first()
        return project
    
    def get(self, request, pk):
        team = self.get_profile(pk)
        serializer = TeamSerializer(instance=team, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        team = self.get_profile(pk)
        serializer = TeamSerializer(
            instance=team, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        team = self.get_profile(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'PATCH', 'DELETE'])
# def detail_equipe(request, pk):
#     team = get_object_or_404(Team.objects.filter(pk=pk).first())
#     if request.method == 'GET':
#         serializer = TeamSerializer(instance=team, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = TeamSerializer(
#             instance=team, data=request.data, many=False)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )
class Task_List(APIView):
    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def tarefa_list(request):
#     if request.method == 'GET':
#         task = Task.objects.all()
#         serializer = TaskSerializer(instance=task, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Detail_Task(APIView):
    def get_profile(self, pk):
        task = Task.objects.filter(pk=pk).first()
        return task
    
    def get(self, request, pk):
        task = self.get_profile(pk)
        serializer = TaskSerializer(instance=task, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = self.get_profile(pk)
        serializer = TaskSerializer(
            instance=task, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        team = self.get_profile(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# @api_view(['GET', 'PATCH', 'DELETE'])
# def detail_tarefa(request, pk):
#     task = get_object_or_404(Task.objects.filter(pk=pk).first())
#     if request.method == 'GET':
#         serializer = TaskSerializer(instance=task, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = TaskSerializer(
#             instance=task, data=request.data, many=False)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )
class Checklist_List(APIView):
    def get(self, request, format=None):
        checklist = Checklist.objects.all()
        serializer = ChecklistSerializer(checklist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def checklist_list(request):
#     if request.method == 'GET':
#         checklist = Checklist.objects.all()
#         serializer = ChecklistSerializer(instance=checklist, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ChecklistSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Detail_Checklist(APIView):
    def get_profile(self, pk):
        checklist = Checklist.objects.filter(pk=pk).first()
        return checklist
    
    def get(self, request, pk):
        checklist = self.get_profile(pk)
        serializer = ChecklistSerializer(instance=checklist, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        checklist = self.get_profile(pk)
        serializer = ChecklistSerializer(
            instance=checklist, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        checklist = self.get_profile(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PATCH', 'DELETE'])
# def detail_checklist(request, pk):
#     checklist = get_object_or_404(Checklist.objects.filter(pk=pk).first())
#     if request.method == 'GET':
#         serializer = ChecklistSerializer(instance=checklist, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = ChecklistSerializer(
#             instance=checklist, data=request.data, many=False)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         checklist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )
class Comment_List(APIView):
    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def comentario_list(request):
#     if request.method == 'GET':
#         comment = Comment.objects.all()
#         serializer = CommentSerializer(instance=comment, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response('POST', status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Detail_Comment(APIView):
    def get_profile(self, pk):
        comment = Comment.objects.filter(pk=pk).first()
        return comment
    
    def get(self, request, pk):
        comment = self.get_profile(pk)
        serializer = CommentSerializer(instance=comment, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        comment = self.get_profile(pk)
        serializer = CommentSerializer(
            instance=comment, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = self.get_profile(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def detail_comentario(request, pk):
#     profile = Comment.objects.filter(pk=pk).first()
#     if profile:
#         serializer = CommentSerializer(instance=profile, many=False)
#         return Response(serializer.data)
#     else:
#         return Response({'EITA:NÂO DEU CERTO'},
#                         status=status.HTTP_404_NOT_FOUND
#                         )
class ProjectToTask(APIView):
    def get_profile(self, project):
        task = Task.objects.filter(project=project)
        return task
    
    def get(self, request, project):
        task = self.get_profile(project)
        serializer = TaskSerializer(instance=task, many=True)
        return Response(serializer.data)
        
