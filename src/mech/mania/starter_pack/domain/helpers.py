import logging
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
