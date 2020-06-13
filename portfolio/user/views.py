from django.shortcuts import render,HttpResponse
from user.models import user, Category, Contents
from rest_framework import viewsets, generics
from user.serializers import UserSerializer, CategorySerializer, ContentsSerializer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# import urllib.request
#오류나면 모듈 임포트


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

# @api_view(['POST'])
# def test(request):
#     # id = request.POST.get('id')
#     return Response({
#         'id':id
#     })

@api_view(['POST'])
def test(request):
    if request.method == 'POST':
        print(request.data)
        # inp = json.dumps(request.data)
        # print(inp)
        print(type(request.data))
        #print(request.data["data"])
        print(request.data['name'])
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def testres(request):
    return 


