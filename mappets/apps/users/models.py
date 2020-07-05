from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _

from mappets.apps.organizations.models import Organization
from .managers import CustomUserManager
from uuid import uuid4

class User(AbstractUser):
    '''
    Representação da model user
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=50,unique=True)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    organizations = models.ManyToManyField(Organization)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')