from django.db import models
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    '''
    Representação da model organization
    '''
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    email = models.CharField(verbose_name=_('Email'), max_length=50)
    phone = models.CharField(verbose_name=_('Phone'), max_length=50, null=True, blank=True)

    # Opções para categoria
    CATEGORY = (
        ('o', 'Ong'),
        ('c', 'Clinic'),
        ('p', 'Pet house'),
    )    

    # Define a categoria da organização
    category = models.CharField(
        verbose_name=_('Category'), 
        max_length=1, 
        choices=CATEGORY
    )
        
    # Retorna o nome da instância do objeto
    def __str__(self):
        return self.name
        
    # Define o verbose name da model
    class Meta:
        verbose_name_plural = _('Organizations')
        verbose_name = _('Organization')