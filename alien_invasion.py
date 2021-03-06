import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
from star import Star
import game_functions as gf

def run_game():

    #initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()

    #screen dimensions
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and  create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship, group of bullets, group of stars and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()

    # Create a fleet of aliens and a group of stars.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_stars(ai_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stars, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stars, stats, sb, ship, aliens, bullets, play_button)

if __name__ == "__main__":
    run_game()
