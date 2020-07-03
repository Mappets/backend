from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    '''
    Representação da model category
    '''    
    name = models.CharField(verbose_name=_('Key'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')
        verbose_name = _('Category')


class Organization(models.Model):
    '''
    Representação da model organization
    '''
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.CharField(verbose_name=_('Description'), max_length=255)
    email = models.CharField(verbose_name=_('Email'), max_length=50)
    phone = models.CharField(verbose_name=_('Phone'), max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name=('organizations'))

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = _('Organizations')
        verbose_name = _('Organization')
