from mech.mania.starter_pack.domain.model.items.shoes import Shoes
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.items.hat import Hat
from mech.mania.starter_pack.domain.model.items.accessory import Accessory
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision

def get_best_item(player, available_items, item_type):
    our_items = [(index, item) for index, item in enumerate(available_items) if type(item) is item_type]
    if (item_type is Weapon):
        curr_weapon = player.get_weapon()
        curr_pv = assign_weapon_point_value(curr_weapon)
        our_items.sort(key=lambda x: assign_weapon_point_value(x[1]), reverse=True)
        if (len(our_items) > 0):
            index, best_weapon = our_items[0]
            best_pv = assign_weapon_point_value(best_weapon)
            if best_pv > curr_pv:
                return index

    if (item_type is Clothes):
        curr_clothes = player.get_clothes()
        curr_pv = assign_clothes_point_value(curr_clothes)
        our_items.sort(key=lambda x: assign_clothes_point_value(x[1]), reverse=True)
        if (len(our_items) > 0):
            index, best_clothes = our_items[0]
            best_pv = assign_clothes_point_value(best_clothes)
            if best_pv > curr_pv:
                return index

    if (item_type is Shoes):
        curr_shoes = player.get_shoes()
        curr_pv = assign_shoes_point_value(curr_shoes)
        our_items.sort(key=lambda x: assign_shoes_point_value(x[1]), reverse=True)
        if (len(our_items) > 0):
            index, best_shoes = our_items[0]
            best_pv = assign_shoes_point_value(best_shoes)
            if best_pv > curr_pv:
                return index

    if (item_type is Hat):
        curr_hat = player.get_hat()
        curr_pv = assign_hat_and_accessory_point_value(curr_hat)
        our_items.sort(key=lambda x: assign_hat_and_accessory_point_value(x[1]), reverse=True)
        if (len(our_items) > 0):
            index, best_hat = our_items[0]
            best_pv = assign_hat_and_accessory_point_value(best_hat)
            if best_pv > curr_pv:
                return index

    if (item_type is Accessory):
        curr_accessory = player.get_accessory()
        curr_pv = assign_hat_and_accessory_point_value(curr_accessory)
        our_items.sort(key=lambda x: assign_hat_and_accessory_point_value(x[1]), reverse=True)
        if (len(our_items) > 0):
            index, best_accessory = our_items[0]
            best_pv = assign_hat_and_accessory_point_value(best_accessory)
            if best_pv > curr_pv:
                return index

    return -1
            

def assign_weapon_point_value(weapon):
    total_pv = 0
    total_pv += weapon.get_attack() * (.25+ (weapon.stats.get_flat_attack_change() * (1 + weapon.stats.get_percent_attack_change())))
    if (weapon.get_on_hit_effect() is not None):
        total_pv = total_pv * (1 + weapon.get_on_hit_effect().get_turns_left()/10)
    if (weapon.get_splash_radius() > 1):
        total_pv = total_pv * (1 + weapon.get_splash_radius()-1/10)
    if (weapon.get_range() > 1):
        total_pv += 10
    total_pv += weapon.stats.get_percent_experience_change() * weapon.stats.get_flat_experience_change()
    return total_pv

def assign_clothes_point_value(clothes):
    total_pv = 0
    total_pv += clothes.stats.get_flat_defense_change() * (1 + clothes.stats.get_percent_defense_change())
    total_pv += clothes.stats.get_flat_health_change() * (1 + clothes.stats.get_percent_health_change())/10
    total_pv += clothes.stats.get_flat_attack_change()
    total_pv += clothes.stats.get_flat_regen_per_turn()
    return total_pv

def assign_shoes_point_value(shoes):
	total_pv = 0
	total_pv += shoes.stats.get_flat_speed_change() * (1 + shoes.stats.get_percent_speed_change())
	if (shoes.stats.get_flat_health_change() > 1):
		total_pv += shoes.stats.get_flat_health_change()
	if (shoes.stats.get_percent_health_change() > 1):
		total_pv += (shoes.stats.get_percent_health_change()/10)
	if (shoes.stats.get_flat_defense_change() > 1):
		total_pv += 10
	if (shoes.stats.get_percent_defense_change() > 1):
		total_pv += 5 + (shoes.stats.get_percent_defense_change())
	if (shoes.stats.get_flat_regen_per_turn() > 0):
		total_pv += 3
	return total_pv

def assign_hat_and_accessory_point_value(accessory):
    total_pv = 0
    total_pv += accessory.stats.get_flat_experience_change() * (1 + accessory.stats.get_percent_experience_change())
    total_pv += accessory.stats.get_flat_defense_change()
    total_pv += accessory.stats.get_flat_health_change() * (1 + accessory.stats.get_percent_health_change())/10
    total_pv += accessory.stats.get_flat_attack_change() * (1 + accessory.stats.get_percent_attack_change())
    total_pv += accessory.stats.get_flat_regen_per_turn()
    if (type(accessory) is Accessory and accessory.get_magic_effect() is not None):
        total_pv += 50
    if (type(accessory) is Hat and accessory.magic_hat_effect() is not None):
        total_pv += 50
    return total_pv
