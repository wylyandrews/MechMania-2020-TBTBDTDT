import logging
import mech.mania.starter_pack.domain.decision_maker as decision_maker
import mech.mania.starter_pack.domain.helpers as helpers

from mech.mania.starter_pack.domain.model.characters.character_decision import CharacterDecision
from mech.mania.starter_pack.domain.model.characters.position import Position
from mech.mania.starter_pack.domain.model.game_state import GameState
from mech.mania.starter_pack.domain.api import API

class Strategy:
    def __init__(self, memory):
        self.memory = memory
        self.logger = logging.getLogger('strategy')
        self.logger.setLevel(logging.INFO)
        logging.basicConfig(level = logging.INFO)

    def make_decision(self, player_name: str, game_state: GameState) -> CharacterDecision:
        """
        Parameters:
        player_name (string): The name of your player
        game_state (GameState): The current game state
        """
        ######################## Initialize ########################
        self.api = API(game_state, player_name)
        self.my_player = game_state.get_all_players()[player_name]
        self.current_board = game_state.get_board(self.my_player.get_position().board_id)
        self.curr_pos = self.my_player.get_position()
        self.monsters_on_board = {name:monster for name, monster in game_state.get_all_monsters().items() if monster.get_position().board_id == self.curr_pos.board_id}
        target_monster = None
        self.logger.info("In make_decision")

        # self.logger.info(helpers.TELL_ME_ME(self.my_player))

        ######################## TAKE TURN HERE ########################
        # self.logger.info(f"All monsters: {game_state.get_all_monsters()}")
        #decision = CharacterDecision(
        #        decision_type="MOVE",
        #        action_position=Position(self.curr_pos.x+2, self.curr_pos.y, "tb_tbdt_dt"),
        #        action_index=None)

        item_index = helpers.should_we_equip(self.my_player, self.logger)

        available_items_tiles = helpers.non_api_find_items(self.my_player, self.current_board, self.my_player.get_speed(), self.logger)
        self.logger.info(f"Available items around: {available_items_tiles}")

        if item_index != -1:
            decision = decision_maker.equip_given_item(item_index)
        elif available_items_tiles:
            decision = decision_maker.loot_items(self.api, self.my_player, self.logger, self.current_board, available_items_tiles)
        else:
            decision, target_monster = decision_maker.make_our_combat_decision(self.api, self.my_player, self.logger, self.monsters_on_board)
        
        #decision = decision_maker.make_our_weapon_decision(self.api, self.my_player, self.logger)
        #decision = decision_maker.head_to_portal_decision(self.api, self.my_player, self.logger)
        # decision_maker.head_to_portal_decision(self.api, self.my_player, self.logger)
        self.logger.info(f"We are doing {decision.__dict__}")
        self.logger.info(f"Player experience: {self.my_player.get_total_experience()}")

        ######################## Logging ########################
        self.memory.set_value("last_decision", decision)
        self.memory.set_value("last_target_monster", target_monster)
        self.logger.info(f"{target_monster.__dict__}")
        self.memory.set_value("last_current_health", self.my_player.current_health)

        ######################## END TURN ########################
        return decision

        """
        last_action, type = self.memory.get_value("last_action", str)
        if last_action is not None and last_action == "PICKUP":
            self.memory.set_value("last_action", "EQUIP")
            return CharacterDecision(
                decision_type="EQUIP",
                action_position=None,
                action_index=self.my_player.get_free_inventory_index()
            )

        tile_items = self.board.get_tile_at(self.curr_pos).items
        if tile_items is not None or len(tile_items) > 0:
            self.memory.set_value("last_action", "PICKUP")
            return CharacterDecision(
                decision_type="PICKUP",
                action_position=None,
                action_index=0
            )

        weapon = self.my_player.get_weapon()
        enemies = self.api.find_enemies(self.curr_pos)
        if enemies is None or len(enemies) > 0:
            self.memory.set_value("last_action", "MOVE")
            return CharacterDecision(
                decision_type="MOVE",
                action_position=self.my_player.get_spawn_point(),
                action_index=None
            )

        enemy_pos = enemies[0].get_position()
        if self.curr_pos.manhattan_distance(enemy_pos) <= weapon.get_range():
            self.memory.set_value("last_action", "ATTACK")
            return CharacterDecision(
                decision_type="ATTACK",
                action_position=enemy_pos,
                action_index=None
            )

        self.memory.set_value("last_action", "MOVE")
        decision = CharacterDecision(
            decision_type="MOVE",
            action_position=self.find_position_to_move(self.my_player, enemy_pos),
            action_index=None
        )
        return decision
        """
