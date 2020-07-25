import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mappets.settings')

import django
django.setup()

from django_seed import Seed

from mappets.apps.pets.models import Breed, Color, Size, Gender, Pet, Specie, History
from mappets.apps.organizations.models import Category, Organization
from mappets.apps.users.models import User

try:
    populator = Seed.seeder()
except:
    populator = Seed.seeder()
finally:
    print(populator)


models = [
    [7, Breed, {}],
    [20, Color, {
        'name': lambda x: populator.faker.color_name()
    }],
    [3, Size, {
        'name': lambda x: populator.faker.random_choices(['pequeno','medio', 'grande'])
    }],
    [7, Gender, {}],
    [4, Specie, {
        'name': lambda x: populator.faker.random_choices(['cachorro','gato', 'cobra', 'pássaro'])
    }],
    [7, Category, {} ],
    [10, Organization, {}],
    [30, User, {}],
    [20, Pet, {
        'name': lambda x: populator.faker.name(),
        'description': lambda x: populator.faker.text(30),
        'age': lambda x: populator.faker.random_int(1, 50),
        'color': lambda x: Color.objects.order_by('?')[0],
        'gender': lambda x: Gender.objects.order_by('?')[0],
        'size': lambda x: Size.objects.order_by('?')[0],
        # 'breed': lambda x: Breed.objects.order_by('?')[0],
        'specie':lambda x: Specie.objects.order_by('?')[0],
    }],
]
for model in models:
    if model[1].objects.all().count() < model[0]:
        populator.add_entity(model[1], model[0], model[2])
result = populator.execute()
print(result)
# try:
#     result = populator.execute()
# except Exception as e:
#     print(e)