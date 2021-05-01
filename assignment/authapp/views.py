from authapp.serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.viewsets import ModelViewSet

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# class UserRegisterView(ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = 

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    lookup_field='id'

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    lookup_field='id'

# class UserDestroyView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = RegisterSerializer
#     lookup_field='id'