from django.test import TestCase

from mappets.apps.pets.models import Pet
# Create your tests here.


class TestPet(TestCase):

    def setUp(self):
        Pet.objects.all()

    def test_pet_has_name(self):
        self.assertEquals(True, False, 'Erro True é diferente de False')
