import sys
import pygame
from  main.ship import Ship
from main.settings import Settings
from pygame.sprite import Group
from main.game_stats import GameStats
from main.button import Button
from main.scoreboard import Scoreboard
import main.game_functions as gf

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    stats = GameStats(ai_settings)
    bullets = Group()
    aliens = Group()
    stars = Group()
    drops = Group()
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen,"Play")
    gf.create_fleet(ai_settings,screen,ship, aliens)
    gf.create_sky(ai_settings, screen, stars)
    #gf.create_rain(ai_settings, screen, drops)
    while True:
        gf.check_events(ai_settings,screen,stats,sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb,ship, aliens, bullets)
            #gf.update_drops(ai_settings, drops)
        gf.update_screen(ai_settings,screen,stats, sb, stars, ship,aliens, bullets, drops, play_button)

run_game()