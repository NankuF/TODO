from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer

# from rest_framework.pagination import LimitOffsetPagination


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


# https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination
# class ToDoLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#
#
# class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoModelSerializer
#     pagination_class = ToDoLimitOffsetPagination
