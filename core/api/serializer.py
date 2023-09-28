from rest_framework import serializers
from usuario.models import Profile
from core.models import *
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = '__all__'
        
        username = serializers.CharField(source=User.username)
        email = serializers.EmailField(source=User.email)
        first_name = serializers.CharField(source=User.first_name)
        last_name = serializers.CharField(source=User.last_name)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
