import logging
import mech.mania.starter_pack.domain.helpers as helpers
from mech.mania.engine.domain.model import character_pb2
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision


def make_our_weapon_decision(api, my_player, logger):
    my_weapon = my_player.get_weapon()
    logger.info(my_weapon)
    logger.info(my_player.inventory)
    logger.info(my_weapon.get_attack())
    return None

def make_our_combat_decision(api, my_player):
    curr_pos = my_player.get_position()
    target_enemy = find_ideal_monster(api, my_player)
    enemy_pos = target_enemy.get_position()

    if curr_pos.manhattan_distance(enemy_pos) <= my_player.get_weapon().get_range():
        return CharacterDecision(
            decision_type="ATTACK",
            action_position=enemy_pos,
            action_index=None
        )
    else:
        return CharacterDecision(
                decision_type="MOVE",
                action_position=helpers.find_position_to_move(api, my_player, enemy_pos),
                action_index=None)


def find_ideal_monster(api, my_player):
    enemies = api.find_enemies_by_distance(my_player.get_position())
    enemies.sort(key=lambda x: abs(my_player.get_level - x.get_level)) # Enemy closest to my level
    return enemies[0]

    #if 1 <= my_level <= 2:
    #    target_monster = 