from django.shortcuts import render
from .serializer import AuthSerial, User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class AuthView(ModelViewSet):
    serializer_class = AuthSerial
    queryset = User.objects.all()
    


