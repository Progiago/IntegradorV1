from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return str(self.user)
