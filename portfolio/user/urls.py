from django.urls import path, include
from .views import register, Category_inp, Contents_inp, test
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
    path('Category/', Category_inp.as_view()),
    path('test/', test)
]
