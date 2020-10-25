from django.contrib.auth.models import User
from rest_framework import serializers
from app_user.models import Project, Profile, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Project,
        fields = ("url", "description", 'title', 'user', 'image', 'CREATED_AT', 'UPDATED_AT',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'user', 'CREATED_AT', 'UPDATED_AT',)


class RatingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=False, read_only=True)

    class Meta:
        model = Rating
        fields = ('usability', 'design', 'content', 'project', 'CREATED_AT', 'UPDATED_AT',)
