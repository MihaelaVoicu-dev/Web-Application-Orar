from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render


def homepage(request):
    # objects = An.objects.filter(an_nume_id =request.user.id)
    # context = {'objects': objects}
    # return render(request, 'homepage.html', context)
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
    permission_classes = [permissions.IsAuthenticated]


class Date_PersonaleViewSet(viewsets.ModelViewSet):
    queryset = Date_Personale.objects.all()
    serializer_class = Date_PersonaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoutatiViewSet(viewsets.ModelViewSet):
    queryset = Noutati.objects.all()
    serializer_class = NoutatiSerializer
    permission_classes = [permissions.IsAuthenticated]
