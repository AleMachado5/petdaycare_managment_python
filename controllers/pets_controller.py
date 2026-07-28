from flask import Blueprint
from flask import jsonify
from flask import request

from services import pets_service

pets_bp = Blueprint("pets", __name__)


@pets_bp.get("/")
def get_pets():

    return jsonify(pets_service.get_all())


@pets_bp.post("/")
def create_pet():

    data = request.json

    response = pets_service.create(data)

    return jsonify(response), 201


@pets_bp.put("/<int:id>")
def update_pet(id):

    data = request.json

    response = pets_service.update(id, data)

    if response is None:

        return jsonify({"error": "Mascota no encontrada"}), 404

    return jsonify(response)


@pets_bp.delete("/<int:id>")
def delete_pet(id):

    deleted = pets_service.delete(id)

    if not deleted:

        return jsonify({"error": "Mascota no encontrada"}), 404

    return jsonify({"mensaje": "Mascota eliminada"})