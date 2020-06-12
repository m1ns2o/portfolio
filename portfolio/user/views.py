from django.shortcuts import render
from user.models import user
from rest_framework import viewsets
from user.serializers import UserSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        # useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            user_data = user(
                username=username,
                # useremail=useremail,
                password=make_password(password) 
            )

            user_data.save()

        return render(request, 'register.html', res_data)

# @api_view('POST')
# def DRF_login(self,request):
class DRF_login(viewsets.ModelViewSet):
    # authentication_classes = (
    #     CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = user.objects.all()
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # print(username)
    # print(password)
    serializer_class = UserSerializer
