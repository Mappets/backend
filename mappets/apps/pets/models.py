# from django.contrib.gis.db import models as models_gis
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mappets.apps.users.models import CommonInfo

from uuid import uuid4


class Specie(models.Model):
    '''
    Representação da model specie
    '''
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(
        verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Species')
        verbose_name = _('Specie')


class Breed(models.Model):
    '''
    Representação da model breed
    '''

    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(
        verbose_name=_('Description'), max_length=255)
    specie = models.ForeignKey(
        Specie, on_delete=models.SET_NULL, null=True, related_name=('breeds'))

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
    description = models.CharField(
        verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Genders')
        verbose_name = _('Gender')


class Color(models.Model):
    '''
    Representação da model color
    '''
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(
        verbose_name=_('Description'), max_length=255)

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
    description = models.CharField(
        verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Sizes')
        verbose_name = _('Size')


class Pet(CommonInfo):
    '''
    Representação da model pet
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(verbose_name='Name',
                            max_length=50, null=True, blank=True)
    description = models.CharField(
        verbose_name='Description', null=True, max_length=255)
    age = models.IntegerField(verbose_name='Age', null=True)
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, null=True, related_name=('pets'))
    specie = models.ForeignKey(
        Specie, on_delete=models.SET_NULL, null=True, related_name=('pets'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pets"
        verbose_name = "Pet"


class History(CommonInfo):
    '''
    Representação da model history
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pet = models.ForeignKey(
        Pet, verbose_name="Pet history",
        on_delete=models.CASCADE,
        related_name='history'
    )
    address = models.CharField(
        default=None, verbose_name="Address", max_length=255, null=True, blank=True)
    latitude = models.FloatField(
        default=None, verbose_name="Latitude")
    longitude = models.FloatField(
        default=None, verbose_name="Longitude")
    user = models.ForeignKey(
        "users.User", default=None, verbose_name="User",
        on_delete=models.CASCADE)
    description = models.CharField(verbose_name=_(
        'Description'), max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.pet.name} | {self.description[:10]}"


class Photo(CommonInfo):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pet = models.ForeignKey(
        Pet, verbose_name="Pet Photos",
        on_delete=models.CASCADE,
        related_name='photos'
    )
    photo = models.ImageField(verbose_name="Photo", blank=False, null=False)

    def __str__(self):
        return self.photo
