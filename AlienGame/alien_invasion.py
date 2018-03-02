import game_functions as gf
import pygame  # 模块pygame包含开发游戏所需的功能
from pygame.sprite import Group

from AlienGame.alien import Alien
from AlienGame.settings import Settings
from AlienGame.ship import Ship


def run_game():
    pygame.init()   #初始化背景设置
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #创建一个名为screen的显示窗口,实参（1200,800）实际上是一个元祖，制定了游戏窗口的尺寸，此处宽1200，高800像素
    pygame.display.set_caption("AlienGame Invasion")   ##设置窗口标题

    #创建一个外星人
    alien = Alien(ai_settings, screen)

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        bullets.update()
        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_bullets(aliens,bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()

