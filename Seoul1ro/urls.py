from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main import views

router = routers.DefaultRouter()

router.register('', views.SendtoAIView, 'main')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
