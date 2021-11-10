from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .paginations import ProjectPageNumberPagination, ToDoPageNumberPagination


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # pagination_class = ProjectPageNumberPagination

    def get_queryset(self):
        """
        С фильтрацией по частичному названию проекта через параметры запроса
        Example: http://127.0.0.1:8000/api/projects/?name=newproj
        """
        name = self.request.query_params.get('name', '')

        if name:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset


class ToDoModelViewSet(ModelViewSet):
    """
        С фильтрацией по точному названию проекта через параметры запроса
        Example: http://127.0.0.1:8000/api/todo/?project=fullnameproject
        C филтрацией по дате
        Example http://127.0.0.1:8000/api/todo/?date_qt=2021-11-07T17:56:56.929096Z&date_lt=2021-11-07T17:57:00.929709Z
        or date
        Example http://127.0.0.1:8000/api/todo/?date_qt=2021-11-07&date_lt=2021-11-07
        or date and time
        Example http://127.0.0.1:8000/api/todo/?date_qt=2021-11-08T06:46&date_lt=2021-11-08T08:53
        or etc
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    # pagination_class = ToDoPageNumberPagination

    def get_queryset(self):
        project = self.request.query_params.get('project', '')
        date_qt = self.request.query_params.get('date_qt', '')
        date_lt = self.request.query_params.get('date_lt', '')
        if project:
            self.queryset = self.queryset.filter(project__name=project)
        if date_qt and date_lt:
            self.queryset = self.queryset.filter(created__gt=date_qt, created__lt=date_lt)

        return self.queryset

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

# https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination
# from rest_framework.pagination import LimitOffsetPagination
# class ToDoLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#
#
# class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoModelSerializer
#     pagination_class = ToDoLimitOffsetPagination
