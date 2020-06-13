from django.shortcuts import render,HttpResponse
from user.models import user, Category, Contents
from rest_framework import viewsets
from user.serializers import UserSerializer, CategorySerializer, ContentsSerializer
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.

class register(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class Category_inp(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Contents_inp(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer