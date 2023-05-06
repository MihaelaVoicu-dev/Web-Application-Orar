from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render


def homepage(request):
    # objects = An.objects.filter(an_nume_id =request.user.id)
    #context = {'objects': objects}
    #return render(request, 'homepage.html', context)
     return render(request, 'homepage.html', {
         "name": "DJANGO"
     })


def index(request):
    return render(request, 'index.html',{
        "name": "DJANGO"
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class SemestruViewSet(viewsets.ModelViewSet):
    queryset = Semestru.objects.all()
    serializer_class = SemestruSerializer
    permission_classes = [permissions.IsAuthenticated]


class An_StudiuViewSet(viewsets.ModelViewSet):
    queryset = An_Studiu.objects.all()
    serializer_class = An_StudiuSerializer
    permission_classes = [permissions.IsAuthenticated]

class Materiile_ProfesoruluiViewSet(viewsets.ModelViewSet):
    queryset = Materiile_Profesorului.objects.all()
    serializer_class = Materiile_ProfesoruluiSerializer
    permission_classes = [permissions.IsAuthenticated]
class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [permissions.IsAuthenticated]
