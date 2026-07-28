from models.pet_model import Pet
from utils.validation_util import (
    validate_phone,
    validate_pet_type
)

pets = []


def get_all():

    return [pet.to_dict() for pet in pets]


def create(data):

    if not validate_pet_type(data["tipo"]):
        return {"error": "Tipo de mascota inválido"}

    pet = Pet(
        nombre=data["nombre"],
        tipo=data["tipo"]
    )

    pets.append(pet)

    return pet.to_dict()


def update(index, data):

    if index >= len(pets):
        return None

    pet = pets[index]

    pet.nombre = data.get("nombre", pet.nombre)
    pet.color = data.get("color", pet.color)
    pet.apodo = data.get("apodo", pet.apodo)
    pet.propietario = data.get("propietario", pet.propietario)

    telefono = data.get("telefono")

    if telefono:

        if not validate_phone(telefono):
            return {"error": "Teléfono inválido"}

        pet.telefono = telefono

    return pet.to_dict()


def delete(index):

    if index >= len(pets):
        return None

    pets.pop(index)

    return True