from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router_register = DefaultRouter()
router_register.register('post', views.register)

router_contents = DefaultRouter()
router_contents.register('post', views.Contents_inp)

router_category = DefaultRouter()
router_category.register('post', views.Category_inp)

# roter_test = DefaultRouter()
# roter_test.register('post', views.test)

urlpatterns = [
    # path('register/', register),
    path('register/',include(router_register.urls)),
    path('Contents/',include(router_contents.urls)),
    path('Category/',include(router_category.urls)),
    path('test/', views.test)
]
