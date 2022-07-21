from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
def clean_ingredients(dish_name, dish_ingredients):
    ingredienti =set(dish_ingredients)
    return (dish_name, ingredienti)
def check_drinks(drink_name, drink_ingredients):
    ingredienti = set(drink_ingredients)
    if ingredienti.isdisjoint(ALCOHOLS):
        return drink_name + " Mocktail"
    return drink_name + " Cocktail"
def categorize_dish(dish_name, dish_ingredients):
    categories = {"VEGAN": VEGAN, "VEGETARIAN": VEGETARIAN, "KETO": KETO, "PALEO": PALEO, "OMNIVORE": OMNIVORE}
    for cat, cat_value in categories.items():
        if dish_ingredients.issubset(cat_value):
            dish_name = f"{dish_name}: {cat}"
    return dish_name
def tag_special_ingredients(dish):
    ingredienti = set(dish[1])
    specials = ingredienti.intersection(SPECIAL_INGREDIENTS)
    return (dish[0], specials)
def compile_ingredients(dishes):
    unione = set()
    for dish in dishes:
        unione = unione.union(dish)
    return unione
def separate_appetizers(dishes, appetizers):
    piatto = set(dishes)
    result = piatto.difference(appetizers)
    return result
def singleton_ingredients(dishes, intersection):
    singletons = set()
    for dish in dishes:
        singletons = singletons.union(dish.difference(intersection))
    return singletons