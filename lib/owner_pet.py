class Pet:
    # List of valid pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    # Class variable to store all pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        # Add the pet to the owner's pet list
        if owner:
            owner.add_pet(self)
        # Add the pet to the global list of all pets
        self.__class__.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return a list of pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Ensure the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        # Set the owner of the pet to this owner
        pet.owner = self

    def get_sorted_pets(self):
        # Return the owner's pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)
