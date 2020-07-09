from django.shortcuts import HttpResponse, get_object_or_404
from user.models import Category, Contents
from rest_framework import viewsets, generics
from user.serializers import CategorySerializer, ContentsSerializer, ReturnCategory, ReturnContents
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

class Category_inp(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Contents_inp(generics.ListCreateAPIView):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer

class Contents_del(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer

class Category_del(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@csrf_exempt
@api_view(['POST'])
def register(request):
    user_id = request.data['username']
    password = request.data['password'] 
    user = User.objects.create_user(username=user_id, password=password)
    return Response('user_created')

@csrf_exempt
@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response('login')
    else:
        return Response('Error')

def logout_view(request):
    logout(request)
    return JsonResponse({'logout': 'ok'}, status=401)

def return_category(request):
    user_pk = get_object_or_404(User,username=request.user).id
    category_list = Category.objects.filter(owner=user_pk).values('id', 'category_text')
    serialized_data = ReturnCategory(category_list, many=True)
    return JsonResponse(serialized_data.data, safe=False)

def return_contents(request, category_key):
    contents_list = Contents.objects.filter(category=category_key).values('id', 'title') # 썸네일 추가?
    serialized_data = ReturnContents(contents_list, many=True)
    return JsonResponse(serialized_data.data, safe=False)

    




 


