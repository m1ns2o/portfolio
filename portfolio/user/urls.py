from django.urls import path, include
from .views import Category_inp, Contents_inp, Contents_del ,Category_del ,register, login_view, logout_view,test, return_category
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register/', register),
    path('Contents/', Contents_inp.as_view()),
    path('Contents/<int:pk>/', Contents_del.as_view()),
    path('Category/', Category_inp.as_view()),
    path('Category/<int:pk>/', Category_del.as_view()),
    path('login/', login_view),
    path('logout/', logout_view),
    path('listcategory/', return_category),
    path('test/', test),
]
