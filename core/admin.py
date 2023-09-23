from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    ...


@admin.register(Filtro)
class FiltroAdmin(admin.ModelAdmin):
    ...


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    ...


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    ...


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    ...


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...
