from django.contrib import admin
from .models import *


@admin.register(Date_Personale)
class Date_PersonaleAdmin(admin.ModelAdmin):
    list_display = ["cnp", "adresa_mail", "nume", "sex", "nationalitate", "cetatenie", "data_nasterii", "telefon",
                    "adresa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Specializare)
class SpecializareAdmin(admin.ModelAdmin):
    list_display = ["nume"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Noutati)
class NoutatiAdmin(admin.ModelAdmin):
    list_display = ["titlu", "anunt", "adresa_mail", "link"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Grupa)
class GrupaAdmin(admin.ModelAdmin):
    list_display = ["id_grupa", "id_specializare", "an", "grupa", "subgrupa", "link"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Note_Materie_Student)
class Note_Materie_StudentAdmin(admin.ModelAdmin):
    list_display = ["email_student", "id_materie_grupa", "nota"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Materiile_Grupelor)
class Materiile_GrupelorAdmin(admin.ModelAdmin):
    list_display = ["ID_mat_grupa", "id_materie", "id_grupa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Materie)
class MaterieAdmin(admin.ModelAdmin):
    list_display = ["nume", "credite"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


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
    list_display = ["email_profesor", "m_materie"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ["titlu", "r_adresa_mail", "e_adresa_mail", "continut"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Grupa_Student)
class Grupa_StudentAdmin(admin.ModelAdmin):
    list_display = ["id_an_studiu", "id_grupa", "email_student", "link"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset