from rest_framework.serializers import HyperlinkedModelSerializer

from .models import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
