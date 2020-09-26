from mech.mania.starter_pack.domain.model.items.shoes import Shoes
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
def get_best_item(player, item_type):
    #get inventory
    inventory = player.inventory
    
    our_items = [(index, item) for index, item in enumerate(inventory) if type(item) is item_type]
    if (item_type is Weapon):
        curr_weapon = player.get_weapon()
        curr_pv = curr_weapon.assign_point_value()
        our_items.sort(key=assign_weapon_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_weapon = our_items[0]
            best_pv = best_weapon.assign_weapon_point_value()
            if best_pv > curr_pv:
                return index

    if (item_type is Clothes):
        curr_clothes = player.get_clothes()
        curr_pv = curr_clothes.assign_clothes_point_value()
        our_items.sort(key=assign_clothes_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_clothes = our_items[0]
            best_pv = best_clothes.assign_clothes_point_value()
            if best_pv > curr_pv:
                return index

    if (item_type is Shoes):
        curr_shoes = player.get_shoes()
        curr_pv = curr_shoes.assign_shoes_point_value()
        our_items.sort(key=assign_shoes_point_value, reverse=True)
        if (len(our_items) > 0):
            index, best_shoes = our_items[0]
            best_pv = best_shoes.assign_shoes_point_value()
            if best_pv > curr_pv:
                return index

    return -1
    #for index, item in our_weapons:
        

        #check if weapon for higher attack
        # curr_weapon_pv = assign_point_value(curr_weapon)
        # item_pv = assign_point_value(item)
        # if type(item) is Weapon and item_pv > curr_weapon_pv:
            

def assign_weapon_point_value(weapon):
    total_pv = 0
    total_pv += weapon.get_attack() * (.25+ (weapon.get_flat_attack_change() * (1 + weapon.get_percent_attack_change())))
    if (weapon.get_on_hit_effect() is not None):
        total_pv = total_pv * (1 + weapon.get_on_hit_effect().get_turns_left()/10)
    if (weapon.get_splash_radius() > 1):
        total_pv = total_pv * (1 + weapon.get_splash_radius()-1/10)
    if (weapon.get_range() > 1):
        total_pv += 10
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
