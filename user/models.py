from django.db import models


class User(models.Model):
    # TODO: Inserir outros atributos
    name = models.CharField(verbose_name="Nome", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"
