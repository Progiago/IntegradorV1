from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(("Imagem de perfil"), upload_to='Profile/covers/%Y/%m/%d/', blank=True, default='')

    class Meta:
        db_table = "profile"

    def __str__(self):
        return str(self.user)
