
from mech.mania.starter_pack.domain.model.characters.position import Position

# feel free to write as many helper functions as you need!
def find_position_to_move(self, api, player: Position, destination: Position) -> Position:
    path = api.find_path(player.get_position(), destination)
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
