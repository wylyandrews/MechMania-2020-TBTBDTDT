from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
def get_best_weapon(player):
    #get inventory
    inventory = player.inventory
    #get current weapon
    curr_weapon = player.get_weapon()
    curr_pv = curr_weapon.assign_point_value()
    #iterate through inventory
    our_weapons = [(index, item) for index, item in enumerate(inventory) if type(item) is Weapon]
    our_weapons.sort(key=assign_point_value, reverse=True)

    if (len(our_weapons) > 0):
        index, best_weapon = our_weapons[0]
        best_pv = best_weapon.assign_point_value()
        if best_pv > curr_pv:
            return index

    return -1
    #for index, item in our_weapons:
        

        #check if weapon for higher attack
        # curr_weapon_pv = assign_point_value(curr_weapon)
        # item_pv = assign_point_value(item)
        # if type(item) is Weapon and item_pv > curr_weapon_pv:
            

def assign_point_value(weapon):
    total_pv = 0
    total_pv += weapon.get_attack()
    if (weapon.get_on_hit_effect() is not None):
        total_pv = total_pv * (1 + weapon.get_on_hit_effect().get_turns_left()/10)
    if (weapon.get_splash_radius() > 1):
        total_pv = total_pv * (1 + weapon.get_splash_radius()/10)
    if (weapon.get_range() > 1):
        total_pv += 10
    return total_pv
    