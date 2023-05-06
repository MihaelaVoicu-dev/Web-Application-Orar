from django.contrib import admin
# from .models import Employee, Employer
from .models import *

@admin.register(An_Studiu)
class An_StudiuAdmin(admin.ModelAdmin):
    list_display = ["an"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset
@admin.register(Semestru)
class SemestruAdmin(admin.ModelAdmin):
    list_display = ["nr_semestru"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset

@admin.register(Materiile_Profesorului)
class Materiile_ProfesoruluiAdmin(admin.ModelAdmin):
    list_display = ["materie", "cnp_profesor"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ["url", "titlu", " r_adresa_mail", "e_adresa_mail", "continut"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset

