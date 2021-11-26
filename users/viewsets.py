from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import CustomUser
from .serializers import CustomUserModelSerializer, CustomUserModelSerializerOnlyUsername


# class CustomUserModelViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserModelSerializer


class CustomUserGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return CustomUserModelSerializerOnlyUsername
        return CustomUserModelSerializer
