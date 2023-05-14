"""hr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add file_backup import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add file_backup import:  from other_app.views import Home
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
router.register(r'materiile_grupelor', views.Materiile_GrupelorViewSet)
router.register(r'note_materie_student', views.Note_Materie_StudentViewSet)
router.register(r'date_personale', views.Date_PersonaleViewSet)
router.register(r'noutati', views.NoutatiViewSet)
router.register(r'specializare', views.SpecializareViewSet)
router.register(r'semestru', views.SemestruViewSet)
router.register(r'an_studiu', views.An_StudiuViewSet)
router.register(r'materiile_profesorului', views.Materiile_ProfesoruluiViewSet)
router.register(r'mail', views.MailViewSet)
router.register(r'grupa_student', views.Grupa_StudentViewSet)
urlpatterns = [
    path('sign_in/', views.user_login),
    path('trimitere_mail/', views.send_email),
    path('casuta_postala/', views.casutaPostala),
    path('orar/', views.other_time_table),
    path('arhiva/', views.arhiva),
    path('situatie_scolara/', views.situatie_scolara),
    path('date_personale/', views.date_personale),
    path('admin/', admin.site.urls),
    path('pagina_principala/', views.pagina_principala),
    path('index/', views.index),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

