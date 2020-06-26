from django.urls import path, include
from .views import register, Category_inp, Contents_inp, Contents_del ,Category_del ,test, login, logout
from rest_framework.routers import DefaultRouter

# router_register = DefaultRouter()
# router_register.register('post', views.register)

# router_contents = DefaultRouter()
# router_contents.register('post', views.Contents_inp)

# router_category = DefaultRouter()
# router_category.register('post', views.Category_inp)

# roter_test = DefaultRouter()
# roter_test.register('post', views.test)

urlpatterns = [
    path('register/', register.as_view()),
    # path('register/',include(router_register.urls)),
    path('Contents/', Contents_inp.as_view()),
    path('Contents/<int:pk>/', Contents_del.as_view()),
    path('Category/', Category_inp.as_view()),
    path('Category/<int:pk>/', Category_del.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('test/', test),
]
