from rest_framework import serializers 
from .models import Category, Contents

# class UserSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = user
#         # fields = ('username', 'password') 
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = '__all__'

class ReturnCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_text']

class ReturnContents(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ['id', 'title', 'contents_thumbnail'] #썸네일 추가할까?