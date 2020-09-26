
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
