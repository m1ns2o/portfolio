from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.DRF_login)

urlpatterns = [
    # path('register/', register),
    path('drfregister/',include(router.urls))
]
