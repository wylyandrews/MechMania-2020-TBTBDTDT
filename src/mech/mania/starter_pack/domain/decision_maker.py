
import mech.mania.starter_pack.domain.helpers as helpers
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision

def make_our_decision(api, my_player):
    curr_pos = my_player.get_position()
    enemies = api.find_enemies_by_distance(curr_pos)
    enemy_pos = enemies[0].get_position()

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
