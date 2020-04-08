from django.db import models
from django.utils.translation import gettext as _


class Breed(models.Model):
    '''
    Representação da model breed
    '''     
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Breeds')
        verbose_name = _('Breed')


class Gender(models.Model):
    '''
    Representação da model gender
    '''     
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Genders')
        verbose_name = _('Gender')


class Color(models.Model):
    '''
    Representação da model color
    '''     
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Colors')
        verbose_name = _('Color')


class Size(models.Model):
    '''
    Representação da model size
    '''     
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Sizes')
        verbose_name = _('Size')


class Specie(models.Model):
    '''
    Representação da model specie
    '''     
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Species')
        verbose_name = _('Specie')


class Pet(models.Model):
    '''
    Representação da model pet
    '''    
    name = models.CharField(verbose_name='Name', max_length=50, null=False)
    description = models.CharField(verbose_name='Description', null=True, max_length=255)
    age = models.IntegerField(verbose_name='Age', null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    specie = models.ForeignKey(Specie, on_delete=models.SET_NULL, null=True, related_name=('pets'))

    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = "Pets"
        verbose_name = "Pet"


class History(models.Model):
    '''
    Representação da model history
    '''     
    pet = models.ForeignKey(
        Pet, verbose_name="Pet history",
        on_delete=models.CASCADE
    )
    address = models.CharField(
        default=None, verbose_name="Address", max_length=50)
    latitude = models.CharField(
        default=None, verbose_name="Latitude", max_length=50)
    longitude = models.CharField(
        default=None, verbose_name="Longitude", max_length=50)
    user = models.ForeignKey(
        "users.User", default=None, verbose_name="User",
        on_delete=models.CASCADE)
