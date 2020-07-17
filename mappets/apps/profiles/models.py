from mappets.apps.users.models import CommonInfo

from django.db import models

from uuid import uuid4

# Create your models here.

class Profile(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(_("Profile Image"), upload_to="profile_image", blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Profiles')
        verbose_name = _('Profile')