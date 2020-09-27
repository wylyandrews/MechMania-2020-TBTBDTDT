import logging
import mech.mania.starter_pack.domain.helpers as helpers
from mech.mania.engine.domain.model import character_pb2
from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.position import Position


def drop_item(index):
    return CharacterDecision(
        decision_type="DROP",
        action_position=None,
        action_index=index
    )

# pickup items in grid around you
def loot_items(api, my_player, logger, board, item_tiles):
    #### grab one based on closeness ####
    current_tile_items = board.get_tile_at(my_player.get_position()).items
    if current_tile_items is not None and len(current_tile_items) > 0:
        return CharacterDecision(
            decision_type="PICKUP",
            action_position=None,
            action_index=0
        )
    
    item_tiles.sort(key=lambda x: Position(x[1], x[2], my_player.get_position().board_id).manhattan_distance(my_player.get_position()))
    return CharacterDecision(
        decision_type="MOVE",
        action_position=item_tiles[0],
        action_index=0
    )

# Expected to grab all items in vicinity (assuming there's an empty inventory slot)
"""def loot_an_item(api, my_player, logger):
    available_items = api.find_items_in_range_by_distance(my_player.get_position(), 5)

    tile_items = self.board.get_tile_at(self.curr_pos).items
    if tile_items is not None or len(tile_items) > 0:
            self.memory.set_value("last_action", "PICKUP")
            return CharacterDecision(
                decision_type="PICKUP",
                action_position=None,
                action_index=0
            )"""

def equip_given_item(inventory_index):
    return CharacterDecision(
        decision_type="EQUIP",
        action_position=None,
        action_index=inventory_index)

def pickup(player, item, board):
    current_position = player.get_position()
    x = current_position.x
    y = current_position.y
    tile = board.grid[x][y]
    items = tile.items
    return CharacterDecision(
        decision_type="PICKUP",
        action_position=None,
        action_index=items.index(item)
    )


def head_to(given_position):
    return CharacterDecision(
        decision_type="MOVE",
        action_position=given_position,
        action_index=None
    )
def head_to_portal_decision(api, my_player, logger):
    my_position = my_player.get_position()
    nearest_portal_pos = api.find_closest_portal(my_player.get_position())
    if nearest_portal_pos.x == my_position.x and nearest_portal_pos.y == my_position.y:
        return CharacterDecision(
        decision_type="TRAVEL",
        action_position=None,
        action_index=0)
    else:
        return CharacterDecision(
            decision_type="MOVE",
            action_position=helpers.find_position_to_move(api, my_player, nearest_portal_pos),
            action_index=None)

def make_our_weapon_decision(api, my_player, logger):
    my_weapon = my_player.get_weapon()
    logger.info(my_weapon)
    logger.info(my_player.inventory)
    logger.info(my_weapon.get_attack())
    return None

# Must return decision, target_monster
def make_our_combat_decision(api, my_player, logger, monsters, searching_graph):
    curr_pos = my_player.get_position()
    target_enemy = find_ideal_monster(api, my_player, monsters)
    enemy_pos = target_enemy.get_position()

    if curr_pos.manhattan_distance(enemy_pos) <= my_player.get_weapon().get_range():
        return CharacterDecision(
            decision_type="ATTACK",
            action_position=enemy_pos,
            action_index=None
        ), target_enemy
    else:
        pos = Position(my_player.get_position())
        pos.y = my_player.get_position().y + my_player.get_speed()
        return CharacterDecision(
                decision_type="MOVE",
                action_position= helpers.find_position_to_move(api, my_player, enemy_pos, logger, searching_graph),
                action_index=None), target_enemy


def find_ideal_monster(api, my_player, monsters):
    #enemies = [enemy for enemy in api.find_enemies_by_distance(my_player.get_position()) if enemy.get_position().board_id == my_player.get_position().board_id]  
    enemies = list(monsters.values())
    # Sorts are really done from last to first
    enemies.sort(key=lambda x: x.get_current_health() / x.get_max_health()) # prioritize on percentage of health
    enemies.sort(key=lambda x: my_player.get_position().manhattan_distance(x.get_position())) # Distance to enemy
    if my_player.get_weapon().get_attack() > 4:
        enemies.sort(key=lambda x: -1 * x.get_level()) # Prioritize higher level enemies
        enemies.sort(key=lambda x: abs((my_player.get_level()) - x.get_level())) # Enemy closest to my level
    else:
        enemies.sort(key=lambda x: x.get_level()) # Prioritize lower level enemies
    #player_damage = my_player.get_weapon().get_attack() * my_player.get_attack()
    #enemies.sort(key=lambda x: 
    enemies.sort(key=lambda x: helpers.get_monster_type(x) != "Legfish") #Prioritizes legfish over anything else
    enemies.sort(key=lambda x: x not in helpers.monsters_in_range(my_player, enemies)) # Enemies that are in aggro
    enemies.sort(key=lambda x: x.is_dead()) # Sorts targets by live ones

    chosen_monster = enemies[0]

    return chosen_monster