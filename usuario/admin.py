from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'profile'
