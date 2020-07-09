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
# from django.forms.models import model_to_dict
# from rest_framework.renderers import JSONRenderer


# Create your views here.

# class register(generics.ListCreateAPIView):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer

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
    print(user_id)
    print(password)
    user = User.objects.create_user(username=user_id, password=password)
    return Response('user_created')

@csrf_exempt
@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print('login')
        return Response('login')
    else:
        # 실패:에러메시지 전송
        print('Error')
        return Response('Error')

# @api_view(['POST'])
def logout_view(request):
    print(request.user)
    logout(request)
    print(request.user)
    return JsonResponse({'logout': 'ok'}, status=401)

def return_category(request):
    print(request.user)
    user_pk = get_object_or_404(User,username=request.user).id
    print(user_pk)
    category_list = Category.objects.filter(owner=user_pk).values('id', 'category_text')
    serialized_data = ReturnCategory(category_list, many=True)
    print(serialized_data.data)
    return JsonResponse(serialized_data.data, safe=False)

def test(request, category_key):
    # category_key = 3
    contents_list = Contents.objects.filter(category=category_key).values('id', 'title') # 썸네일 추가?
    serialized_data = ReturnContents(contents_list, many=True)
    print(serialized_data)
    return JsonResponse(serialized_data.data, safe=False)


def return_contents(request):
    category_key = 4
    contents_list = Contents.objects.filter(category=category_key).values('id', 'title') # 썸네일 추가?
    serialized_data = ReturnContents(contents_list, many=True)
    print(serialized_data)
    return JsonResponse(serialized_data.data, safe=False)

    





#request.user 유저 세션

'''
@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user_id = request.data['id']
        password = request.data['password']
        db_user = get_object_or_404(user, username=user_id)
        request.session['user_pk'] = db_user.id
        print(db_user.id)
        print(db_user.username) 
        print(db_user.password)
        if user_id == db_user.username and password == db_user:
            return Response({
                    "id" : db_user.usename 
                }) 
        else :
            return Response("ERROR")
'''



'''    
@csrf_exempt
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        print(request.session)
        del request.session['user_pk']
        return Response({'sess':request.session})

'''


     


