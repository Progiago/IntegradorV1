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
        profile = User.objects.all()
        serializer = UserSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Detail_profile(APIView):
    def get_profile(self, pk):
        profile = User.objects.filter(pk=pk).first()
        return profile
    
    def get(self, request, pk):
        profile = self.get_profile(pk)
        serializer = UserSerializer(instance=profile, many=False)
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


class ProjectToTask(APIView):
    def get_task(self, project):
        task = Task.objects.filter(project=project)
        return task
    
    def get(self, request, project):
        task = self.get_task(project)
        serializer = TaskSerializer(instance=task, many=True)
        return Response(serializer.data)


class UserToProject(APIView):
    def get_user(self, profile):
        user = Project.objects.filter(profile=profile)
        return user

    def get(self, request, profile):
        users = self.get_user(profile)
        serializer = ProjectSerializer(instance=users, many=True)
        return Response(serializer.data)
