import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""飞船类"""
	
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		# 获取屏幕外接矩形
		self.screen_rect = self.screen.get_rect()
		
		# 将飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)
		# 移动标志
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		"""根据移动标志调整飞船的位置,位置只能在屏幕内"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0 :
			self.center -= self.ai_settings.ship_speed_factor
			
		# 根据self.center更新rect对象，只存储整数部分
		self.rect.centerx = self.center
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
