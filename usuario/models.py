from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.username
