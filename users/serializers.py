from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'first_name', 'last_name', 'email',
                  'password', 'is_staff']

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     return user


class CustomUserModelSerializerOnlyUsername(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', ]
