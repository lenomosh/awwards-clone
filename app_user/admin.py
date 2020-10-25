from django.contrib import admin
from app_user.models import Project,Rating,Profile
# Register your models here.
admin.register(Project,Rating,Profile)
