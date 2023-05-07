from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("http://localhost:8000/send_email/")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'sign-in/index.html')
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect("send_email.html")
#         else:
#             error_message = 'Username or password is incorrect.'
#     else:
#         error_message = ''
#     return render(request, 'login.html', {'error_message': error_message})

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
def casutaPostala(request):
    objects = Mail.objects.filter(receptor__User = request.user.id)
    context = {'objects': objects}
    return render(request, 'mailbox/index.html', context)
def situatie_scolara(request):
    objects = Grupa_Student.objects.filter(Date_Student__User=request.user.id)
    objects1 = Grupa.objects.filter()
    objects2 = Specializare.objects.filter()
    objects3 = Semestru.objects.filter()
    objects4 = Note_Materie_Student.objects.filter(Date_Student__User__email=request.user.email)
    objects5 = Materiile_Grupelor.objects.filter()
    context = {'objects': objects, 'objects1': objects1, 'objects2': objects2,
               'objects3': objects3, 'objects4': objects4, 'objects5': objects5}
    return render(request, 'situatieScolara/index.html', context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class MaterieViewSet(viewsets.ModelViewSet):
    queryset = Materie.objects.all()
    serializer_class = MaterieSerializer
    permission_classes = [permissions.IsAuthenticated]


class Materiile_GrupelorViewSet(viewsets.ModelViewSet):
    queryset = Materiile_Grupelor.objects.all()
    serializer_class = Materiile_GrupelorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GrupaViewSet(viewsets.ModelViewSet):
    queryset = Grupa.objects.all()
    serializer_class = GrupaSerializer
    permission_classes = [permissions.IsAuthenticated]


class Note_Materie_StudentViewSet(viewsets.ModelViewSet):
    queryset = Note_Materie_Student.objects.all()
    serializer_class = Note_Materie_StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class Date_PersonaleViewSet(viewsets.ModelViewSet):
    queryset = Date_Personale.objects.all()
    serializer_class = Date_PersonaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoutatiViewSet(viewsets.ModelViewSet):
    queryset = Noutati.objects.all()
    serializer_class = NoutatiSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecializareViewSet(viewsets.ModelViewSet):
    queryset = Specializare.objects.all()
    serializer_class = SpecializareSerializer
    permission_classes = [permissions.IsAuthenticated]


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
