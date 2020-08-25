from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from mappets.apps.organizations.models import Organization
from .managers import CustomUserManager
from uuid import uuid4


class CommonInfo(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    deleted_at = models.DateTimeField(_('Deleted At'), blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
    
    def delete(self):
        self.deleted_at = timezone.now()
        self.deleted = True
        self.save()

    def hard_delete(self):
        super(CommonInfo, self).delete()


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
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')
    
    @property
    def username(self):
        return f"{self.id}-{timezone.now()}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class Profile(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=50)
    picture = models.ImageField(_('Profile Image'), upload_to="profile", blank=True, null=True)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.email



class History(CommonInfo):
    '''
    Representação da model history
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profile = models.ForeignKey(
        Profile, verbose_name="Profile history",
        on_delete=models.DO_NOTHING,
        related_name='history'
    )
    address = models.CharField(
        default=None, verbose_name="Address", max_length=50)
    latitude = models.FloatField(
        default=None, verbose_name="Latitude")
    longitude = models.FloatField(
        default=None, verbose_name="Longitude")
    description = models.CharField(verbose_name=_('Description'), max_length=255, null=True, blank=True)

    def __str__(self):
       return f"{self.profile.name} | {self.description[:10]}"
