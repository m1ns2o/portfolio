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