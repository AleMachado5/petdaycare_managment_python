from config import Config


def validate_phone(phone):

    return phone.isdigit()


def validate_pet_type(tipo):

    return tipo.lower() in Config.ALLOWED_TYPES