from django.db import models


class Animal(models.Model):
    COLORS = (
        ('P', 'PRETO'),
        ('B', 'BRANCO'),
        ('L', 'LARANJA'),
        ('M', 'MARROM'),
        ('BI', 'BICOLOR'),
        ('TRI', 'TRICOLOR'),
    )
    GENDER = (
        ('f', 'Femea'),
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
        'animal.Breed', verbose_name='Raça', on_delete=models.CASCADE)
    species = models.CharField(
        max_length=1, verbose_name='Espécie', choices=SPECIES)

    class Meta:
        verbose_name_plural = "Animais"
        verbose_name = "Animal"


class AnimalHistory(models.Model):
    animal = models.ForeignKey(
        "animal.Animal", verbose_name="Histórico do Animal",
        on_delete=models.CASCADE
    )
    address = models.CharField(
        default=None, verbose_name="Endereço", max_length=50)
    latitude = models.CharField(
        default=None, verbose_name="Latitude", max_length=50)
    longitude = models.CharField(
        default=None, verbose_name="Longitude", max_length=50)
    user = models.ForeignKey(
        "user.User", default=None, verbose_name="Usuário",
        on_delete=models.CASCADE)


class Breed(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Raças"
        verbose_name = "Raça"
