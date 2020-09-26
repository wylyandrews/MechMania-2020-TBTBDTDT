from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
def get_best_weapon(player):
    #get inventory
    inventory = player.inventory
    #get current weapon
    curr_weapon = player.get_weapon()
    #iterate through inventory
    for index, item in enumerate(inventory):
        #check if weapon for higher attack
        curr_weapon_pv = assign_point_value(curr_weapon)
        item_pv = assign_point_value(item)
        if type(item) is Weapon and item_pv > curr_weapon_pv:
            #equip if better
            return CharacterDecision(
                decision_type="EQUIP",
                action_position=None,
                action_index=index
            )

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
    