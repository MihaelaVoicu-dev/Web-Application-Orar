"""hr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hr import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'materie', views.MaterieViewSet)
router.register(r'zi', views.ZiViewSet)
router.register(r'an', views.AnViewSet)
router.register(r'profesor', views.ProfesorViewSet)
router.register(r'grupa', views.GrupaViewSet)
router.register(r'orar', views.OrarViewSet)
router.register(r'sala', views.SalaViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage),
    path('index/', views.index),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

