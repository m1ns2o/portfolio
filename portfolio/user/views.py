from django.shortcuts import render,HttpResponse, get_object_or_404
from user.models import user, Category, Contents
from rest_framework import viewsets, generics
from user.serializers import UserSerializer, CategorySerializer, ContentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

class register(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

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
def test(request):
    user_id = request.data['id']
    password = request.data['password'] 
    print(user_id)
    print(password)
    user = User.objects.create_user(username=user_id, password=password)
    return Response('asdfas')

# @csrf_exempt
# @api_view(['POST'])
# def test(request):
#     if request.method == 'POST':
#         print(request.data)
#         # inp = json.dumps(request.data)
#         # print(inp)
#         print(request.session.get('user_id'))
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user_id = request.data['id']
        password = request.data['password']
        # db_user = user.objects.get(username=user_id)
        db_user = get_object_or_404(user, username=user_id)
        request.session['user_pk'] = db_user.id
        print(db_user.id)
        print(db_user.username) 
        print(db_user.password)
        if user_id == db_user.username and password == db_user:
            return Response({
                    "id" : db_user.usename 
                }) 
        # return Response({"session":request.session['user_pk']})
        else :
            return Response("ERROR")

@csrf_exempt
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        print(request.session)
        del request.session['user_pk']
        return Response({'sess':request.session})



     


