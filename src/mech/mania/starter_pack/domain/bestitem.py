from mech.mania.starter_pack.domain.model.items.shoes import Shoes
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.items.hat import Hat
from mech.mania.starter_pack.domain.model.items.accessory import Accessory
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
def get_best_item(player, item_type):
    #get inventory
    inventory = player.inventory
    
    our_items = [(index, item) for index, item in enumerate(inventory) if type(item) is item_type]
    if (item_type is Weapon):
        curr_weapon = player.get_weapon()
        curr_pv = assign_weapon_point_value(curr_weapon)
        our_items.sort(key=assign_weapon_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_weapon = our_items[0]
            best_pv = assign_weapon_point_value(best_weapon)
            if best_pv > curr_pv:
                return index

    if (item_type is Clothes):
        curr_clothes = player.get_clothes()
        curr_pv = assign_clothes_point_value(curr_clothes)
        our_items.sort(key=assign_clothes_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_clothes = our_items[0]
            best_pv = assign_clothes_point_value(best_clothes)
            if best_pv > curr_pv:
                return index

    if (item_type is Shoes):
        curr_shoes = player.get_shoes()
        curr_pv = assign_shoes_point_value(curr_shoes)
        our_items.sort(key=assign_shoes_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_shoes = our_items[0]
            best_pv = assign_shoes_point_value(best_shoes)
            if best_pv > curr_pv:
                return index

    if (item_type is Hat):
        curr_hat = player.get_hat()
        curr_pv = assign_hat_and_accessory_point_value(curr_hat)
        our_items.sort(key=assign_hat_and_accessory_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_hat = our_items[0]
            best_pv = assign_hat_and_accessory_point_value(best_hat)
            if best_pv > curr_pv:
                return index

    if (item_type is Accessory):
        curr_accessory = player.get_accessory()
        curr_pv = assign_hat_and_accessory_point_value(curr_accessory)
        our_items.sort(key=assign_hat_and_accessory_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_accessory = our_items[0]
            best_pv = assign_hat_and_accessory_point_value(best_accessory)
            if best_pv > curr_pv:
                return index

    return -1
            

def assign_weapon_point_value(weapon):
    total_pv = 0
    total_pv += weapon.get_attack() * (.25+ (weapon.get_flat_attack_change() * (1 + weapon.get_percent_attack_change())))
    if (weapon.get_on_hit_effect() is not None):
        total_pv = total_pv * (1 + weapon.get_on_hit_effect().get_turns_left()/10)
    if (weapon.get_splash_radius() > 1):
        total_pv = total_pv * (1 + weapon.get_splash_radius()-1/10)
    if (weapon.get_range() > 1):
        total_pv += 10
    total_pv += weapon.get_percent_experience_change * weapon.get_flat_experience_change
    return total_pv

def assign_clothes_point_value(clothes):
    total_pv = 0
    total_pv += clothes.get_flat_defence_change() * clothes.get_percent_defence_change()
    total_pv += clothes.get_flat_health_change() * clothes.get_percent_health_change()
    total_pv += clothes.get_flat_attack_change()
    total_pv += clothes.get_flat_regen_per_turn()
    return total_pv

def assign_shoes_point_value(shoes):
	total_pv = 0
	total_pv += shoes.get_flat_speed_change()
	total_pv += shoes.get_percent_speed_change()
	return total_pv

def assign_hat_and_accessory_point_value(accessory):
    total_pv = 0
    total_pv += accessory.get_flat_experience_change() * accessory.get_percent_experience_change()
    total_pv += accessory.get_flat_defence_change()
    total_pv += accessory.get_flat_health_change() * accessory.get_percent_health_change()
    total_pv += accessory.get_flat_attack_change() * accessory.get_percent_attack_change()
    total_pv += accessory.get_flat_regen_per_turn()
    return total_pv
