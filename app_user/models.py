from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
import math


# Create your models here.
class Project(models.Model):
    url = models.URLField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField("image")
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    bio = models.CharField(max_length=255)
    profile_picture = CloudinaryField("image")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class Rating(models.Model):
    usability, design, content = models.IntegerField(), models.IntegerField(), models.IntegerField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return math.fsum([self.usability, self.design, self.content])/3
