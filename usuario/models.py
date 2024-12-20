from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Exemplo de campo extra (opcional)
    data_nascimento = models.DateField(null=True, blank=True)

    # Especificando os related_names para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',  # Nome único para evitar conflito
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_user_permissions',  # Nome único para evitar conflito
        blank=True
    )

    def __str__(self):
        return self.username
