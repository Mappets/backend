from django.db import models
from django.utils.translation import gettext as _


class Breed(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Breeds')
        verbose_name = _('Breed')


class Pet(models.Model):
    COLORS = (
        ('P', 'PRETO'),
        ('B', 'BRANCO'),
        ('L', 'LARANJA'),
        ('M', 'MARROM'),
        ('BI', 'BICOLOR'),
        ('TRI', 'TRICOLOR'),
    )
    GENDER = (
        ('f', 'Femeas'),
        ('m', 'Macho'),
    )
    SIZE = (
        ('PQ', 'PEQUENO'),
        ('MD', 'MEDIO'),
        ('GR', 'GRANDE'),
    )
    SPECIES = (
        ('C', 'CACHORRO'),
        ('G', 'GATO'),
    )
    name = models.CharField(verbose_name='Nome', max_length=50, null=False)
    age = models.IntegerField(verbose_name='Idade')
    color = models.CharField(verbose_name='Cor', max_length=20, choices=COLORS)
    gender = models.CharField(
        verbose_name='Sexo', max_length=1, choices=GENDER)
    size = models.CharField(
        default='MD', verbose_name='Porte', max_length=50, choices=SIZE)
    breed = models.ForeignKey(
        Breed, verbose_name='Raça', on_delete=models.CASCADE)
    species = models.CharField(
        max_length=1, verbose_name='Espécie', choices=SPECIES)

    class Meta:
        verbose_name_plural = "Pets"
        verbose_name = "Pet"

    def __str__(self):
       return self.name


class History(models.Model):
    pet = models.ForeignKey(
        Pet, verbose_name="Histórico do Pet",
        on_delete=models.CASCADE
    )
    address = models.CharField(
        default=None, verbose_name="Endereço", max_length=50)
    latitude = models.CharField(
        default=None, verbose_name="Latitude", max_length=50)
    longitude = models.CharField(
        default=None, verbose_name="Longitude", max_length=50)
    user = models.ForeignKey(
        "users.User", default=None, verbose_name="Usuário",
        on_delete=models.CASCADE)


