from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
def get_best_weapon(player):
    #get inventory
    inventory = player.inventory
    #get current weapon
    curr_weapon = player.getWeapon()
    #iterate through inventory
    for i in inventory:
        #check if weapon for higher attack
        if type(i) is Weapon and i.get_attack() > curr_weapon.get_attack():
            #equip if better
            return CharacterDecision(
                decision_type="EQUIP",
                action_position=None,
                action_index=player.get_free_inventory_index()
            )