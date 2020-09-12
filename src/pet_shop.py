def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]


def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]


def add_or_remove_cash(pet_shop_dict, cash_change_amount):
    pet_shop_dict["admin"]["total_cash"] = get_total_cash(pet_shop_dict) + cash_change_amount
    return pet_shop_dict


def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"]


def increase_pets_sold(pet_shop_dict, sold_int):
    pet_shop_dict["admin"]["pets_sold"] += sold_int
    return pet_shop_dict


def get_stock_count(pet_shop_dict):
    return len(pet_shop_dict["pets"])


def get_pets_by_breed(pet_shop_dict, pet_breed):
    breed = []
    for pet in pet_shop_dict["pets"]:
        if pet["breed"] == pet_breed:
            breed.append(pet)
    return breed


def find_pet_by_name(pet_shop_dict, pet_name):
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == pet_name:
            return pet


 