from django.db import models

from users.models import CustomUser


class Project(models.Model):
    users = models.ManyToManyField(CustomUser)
    name = models.CharField(max_length=100, unique=True)
    repository = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    """Заметка"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    active = models.BooleanField(default=True)  # default=True не срабатывает в DRF
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description}'
