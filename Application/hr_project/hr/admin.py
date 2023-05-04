from django.contrib import admin
# from .models import Employee, Employer
from .models import Sala, Orar, Profesor, Materie, Zi, An, Grupa


@admin.register(Materie)
class MaterieAdmin(admin.ModelAdmin):
    list_display = ["nume_materie"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Grupa)
class GrupaAdmin(admin.ModelAdmin):
    list_display = ["an", "grupa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(An)
class AnAdmin(admin.ModelAdmin):
    list_display = ["id_an"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Zi)
class ZiAdmin(admin.ModelAdmin):
    list_display = ["nume_zi"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ["id_sala", "nume_sala"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ["CNP", "nume_profesor", "prenume_profesor"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Orar)
class OrarAdmin(admin.ModelAdmin):
    list_display = ["id_an", "g_an", "g_grupa", "nume_zi", "nume_materie", "nume_profesor","prenume_profesor", "id_sala", "inceput_ora", "sfarsit_ora"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_staff and not user.is_superuser:
            return queryset.filter(profesor__nume_profesor=user.first_name, profesor__prenume_profesor=user.last_name)

        return queryset
