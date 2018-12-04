import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# 初始化游戏、设置、屏幕
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建一艘飞船
	ship = Ship(ai_settings,screen)
	# 创建一个外星人编组
	aliens = Group()
	# 创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	# 创建一个用于存储子弹的编组 
	bullets = Group()
	# 创建一个用于存储游戏统计信息的实例,并创建计分盘
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	# 创建play按钮
	play_button = Button(ai_settings,screen,"Play")
	
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,stats,play_button,ship,
			aliens,bullets,sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,
				aliens,bullets)
			gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,
				bullets)		
		gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,
			play_button,sb)

# 开始游戏
run_game()
