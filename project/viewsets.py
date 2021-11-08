from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .paginations import ProjectPageNumberPagination, ToDoPageNumberPagination


# from rest_framework.pagination import LimitOffsetPagination


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPageNumberPagination

    def get_queryset(self):
        """
        С фильтрацией по названию проекта через параметры запроса
        Example: http://127.0.0.1:8000/api/projects/?name=newproj
        """
        name = self.request.query_params.get('name', '')
        if name:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoPageNumberPagination

    def get_queryset(self):
        project = self.request.query_params.get('project', '')
        if project:
            self.queryset = self.queryset.filter(project__name=project)
        return self.queryset

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

# https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination
# class ToDoLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#
#
# class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoModelSerializer
#     pagination_class = ToDoLimitOffsetPagination
