from src.game import Game
if __name__ == "__main__":
    game = Game()
    game.player_setup()
    game.deal_init()
    game.deal_round()
    game.check_winners()
