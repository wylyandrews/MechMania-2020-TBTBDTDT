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
        if type(item) is Weapon and item.get_attack() > curr_weapon.get_attack():
            #equip if better
            return CharacterDecision(
                decision_type="EQUIP",
                action_position=None,
                action_index=index
            )