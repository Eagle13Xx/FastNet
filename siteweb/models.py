from django.db import models
from django.contrib.auth.models import User

from FastNet import settings



class Plano(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    velocidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome



class PlanoAdquirido(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="planos_adquiridos"
    )
    plano = models.ForeignKey(
        Plano,
        on_delete=models.CASCADE,
        related_name="adquiridos"
    )
    data_adquirida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} adquiriu {self.plano.nome}"