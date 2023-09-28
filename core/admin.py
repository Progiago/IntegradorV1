from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Project)
class ProjetoAdmin(admin.ModelAdmin):
    ...


@admin.register(Filter)
class FiltroAdmin(admin.ModelAdmin):
    ...


@admin.register(Team)
class EquipeAdmin(admin.ModelAdmin):
    ...


@admin.register(Task)
class TarefaAdmin(admin.ModelAdmin):
    ...


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    ...


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...
