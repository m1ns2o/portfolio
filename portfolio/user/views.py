from django.shortcuts import render,HttpResponse
from user.models import user, Category, Contents
from rest_framework import viewsets
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

class register(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class Category_inp(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Contents_inp(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer

# @api_view(['POST'])
# def test(request):
#     # id = request.POST.get('id')
#     return Response({
#         'id':id
#     })

@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        print(request.data)
        # inp = json.dumps(request.data)
        # print(inp)
        print(type)
        print(request.data["data"])
        print(type(inp))
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})