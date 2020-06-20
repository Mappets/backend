from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import AbstractBaseUser
from organizations.models import Organization


class User(AbstractBaseUser):
    '''
    Representação da model user
    '''
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=50)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    organizations = models.ManyToManyField(Organization)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')