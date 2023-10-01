from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(("Imagem de perfil"), upload_to='Profile/covers/%Y/%m/%d/', blank=True, default='')

    class Meta:
        db_table = "profile"

    def __str__(self):
        return str(self.user)


# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", 'Admin'
#         MANAGER = "MANAGER", 'Manager'
#         PARTICIPANT = "ATTENDANT", 'Attendant'
    
#     base_role = Role.ADMIN
#     role = models.CharField(max_length=50, choices=Role.choices)
    
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)


# class Attendant(User):
#     base_role = User.Role.PARTICIPANT
    
#     class Meta:
#         proxy = True
    