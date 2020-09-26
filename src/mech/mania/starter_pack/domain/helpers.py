import logging

from mech.mania.starter_pack.domain.model.board.board import Board
from mech.mania.starter_pack.domain.model.characters.player import Player
from mech.mania.starter_pack.domain.model.characters.position import Position

def NONAPI_find_position_to_move(player: Player, destination: Position) -> Position:
    return NotImplementedError

    pos = None
    if len(path) < player.get_speed():
        pos = path[-1]
    else:
        pos = path[player.get_speed() - 1]
    return pos

# feel free to write as many helper functions as you need!
def find_position_to_move(api, player: Player, destination: Position, logger) -> Position:
    path = api.find_path(player.get_position(), destination)
    logger.info(f"Path: {path}")
    pos = None
    if len(path) < player.get_speed():
        pos = path[-1]
    else:
        pos = path[player.get_speed() - 1]
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
def non_api_find_items(player: Player, board: Board, range_val):
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

            items = get_tile_items(board, x, y)
            for item in items:
                available_items.append((item, x, y))
    
    return available_items

def get_tile_items(board, x, y):
    tile = None
    try:
        tile = board.grid[x][y]
    except:
        return list()
    if tile.type == "VOID" or tile.type == "IMPASSABLE" or x < 0 or y < 0:
        return list()
    return tile.items
