from django.urls import path
from .viewsets import CustomUserGenericViewSet

app_name = 'users'
urlpatterns = [
    path('', CustomUserGenericViewSet.as_view({'get': 'list'})),
]