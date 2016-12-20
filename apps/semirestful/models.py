from django.db import models
from django.utils.timezone import now
# Create your models here.
class PetManager(models.Manager):
    def update(self, id, form_info):
        pet = Pet.objects.get(id=id)
        pet.name = form_info["name"]
        pet.description = form_info["description"]
        pet.type_of_pet = form_info["type_of_pet"]
        pet.breed = form_info["breed"]
        pet.save()

class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type_of_pet = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    objects = PetManager()
