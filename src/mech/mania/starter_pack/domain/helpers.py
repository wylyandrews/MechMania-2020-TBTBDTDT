import logging
import re

import mech.mania.starter_pack.domain.bestitem as bestitem

from mech.mania.starter_pack.domain.model.board.board import Board
from mech.mania.starter_pack.domain.model.characters.player import Player
from mech.mania.starter_pack.domain.model.characters.position import Position
from mech.mania.starter_pack.domain.model.items.shoes import Shoes
from mech.mania.starter_pack.domain.model.items.weapon import Weapon
from mech.mania.starter_pack.domain.model.items.clothes import Clothes
from mech.mania.starter_pack.domain.model.items.hat import Hat
from mech.mania.starter_pack.domain.model.items.accessory import Accessory

"""def NONAPI_find_position_to_move(player: Player, destination: Position) -> Position:
    return NotImplementedError

    pos = None
    if len(path) < player.get_speed():
        pos = path[-1]
    else:
        pos = path[player.get_speed() - 1]
    return pos"""

# feel free to write as many helper functions as you need!
def find_position_to_move(api, player: Player, destination: Position, logger, graph) -> Position:
    #path = api.find_path(player.get_position(), destination)
    path, _ = graph.AStarSearch(player.get_position(), destination)
    pos = None
    logger.info(f"Path: {path}")
    if len(path) <= player.get_speed():
        coordinates = path[-1]
        pos = Position.create(coordinates[0], coordinates[1], player.get_position().board_id)
    else:
        coordinates = path[player.get_speed()]
        pos = Position.create(coordinates[0], coordinates[1], player.get_position().board_id)
    logger.info(f"target destination: {coordinates}")
    return pos

def TELL_ME_ME(player):
    #my_player_description = "Player stuff is: "
    #my_player_description += player.
    return f"\nPlayer: {player.__dict__}\nWeapon: {player.get_weapon().__dict__}\nWeapon Stats: {player.get_weapon().stats.__dict__}\nClothes: {player.get_clothes().stats.__dict__}\nAccessory: {player.get_accessory().stats.__dict__}\nHat: {player.get_hat().stats.__dict__}\nShoes: {player.get_shoes().stats.__dict__}"

def get_equipment_level(player):
    my_equipment = list()
    my_equipment.append(player.get_weapon())
    my_equipment.append(player.get_clothes())
    my_equipment.append(player.get_weapon())
    my_equipment.append(player.get_weapon())
    return NotImplementedError

# Returns a list of tuples of items and (x,y) coordinates
def non_api_find_items(player: Player, board: Board, range_val, logger):
    current_location = player.get_position()
    available_items = list()
    for i in range(-1*range_val, range_val+1):
        x = current_location.x + i
        if x < 0 or x >= board.width:
            continue
        for j in range(-1*range_val, range_val+1):
            y = current_location.y + j
            if y < 0 or y >= board.height:
                continue

            if abs(i) + abs(j) > range_val:
                continue
            
            items = get_tile_items(board, x, y, logger)
            
            for item in items:
                available_items.append((item, x, y))
    
    return available_items

def get_tile_items(board, x, y, logger):
    tile = None
    try:
        tile = board.grid[x][y]
    except:
        return list()
    logger.info(f"Checking tile: {tile.__dict__}")
    if tile.type == "VOID" or tile.type == "IMPASSABLE" or x < 0 or y < 0:
        return list()
    return tile.items

def should_we_equip(player, available_items, logger):
    for t in [Weapon, Clothes, Shoes, Hat, Accessory]:
        best_item_index = bestitem.get_best_item(player, available_items, t)
        if best_item_index > -1:
            return best_item_index
    return -1

def get_monster_type(monster):
    return re.split("[0-9]", monster.name)[0]

def monsters_in_range(player, monsters):
	aggro_monsters = list()
	for monster in monsters:
		player_location = player.get_position()
		monster_location = monster.get_position()
		monster_aggro_range = monster.get_aggro_range()
		range_dist = monster_location.manhattan_distance(player_location)
		if monster_aggro_range > range_dist:
			aggro_monsters.append(monster)
	return aggro_monsters
