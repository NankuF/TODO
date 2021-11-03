from django.db import models
from django.contrib.auth.models import AbstractUser

from project.models import Project


class CustomUser(AbstractUser):
    project = models.ManyToManyField(Project)
    email = models.EmailField(unique=True)
