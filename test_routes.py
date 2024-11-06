from unittest import TestCase
from service.models import Pet, db, Gender
from tests.factories import PetFactory

class TestPetModel(TestCase):

    def test_create_a_pet(self):
        pet = Pet(name="Fido", category="dog", available=True, gender=Gender.MALE)
        pet.create()
        self.assertIsNotNone(pet.id)

    def test_read_a_pet(self):
        pet = PetFactory()
        pet.create()
        found_pet = Pet.find(pet.id)
        self.assertEqual(found_pet.name, pet.name)

    def test_update_a_pet(self):
        pet = PetFactory()
        pet.create()
        pet.category = "k9"
        pet.update()
        self.assertEqual(pet.category, "k9")

    def test_delete_a_pet(self):
        pet = PetFactory()
        pet.create()
        pet.delete()
        self.assertIsNone(Pet.find(pet.id))

    def test_list_all_pets(self):
        pets = Pet.all()
        self.assertGreater(len(pets), 0)

    def test_find_by_name(self):
        pet = PetFactory(name="Fido")
        pet.create()
        found_pet = Pet.find_by_name("Fido")
        self.assertEqual(found_pet.name, "Fido")

    def test_find_by_category(self):
        pet = PetFactory(category="dog")
        pet.create()
        found_pets = Pet.find_by_category("dog")
        self.assertGreater(len(found_pets), 0)

    def test_find_by_availability(self):
        pet = PetFactory(available=True)
        pet.create()
        found_pets = Pet.find_by_availability(True)
        self.assertGreater(len(found_pets), 0)
