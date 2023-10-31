import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship """
	def __init__(self,ai_game):
		"""Intialize the ship and set its starting position """
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect= ai_game.screen.get_rect()

		#Load the ship image and its rect.
		self.image = pygame.image.load('image/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store a float for the ship's exact horizontal position
		self.x =float(self.rect.x)

		#Movement flag: start with a ship that's not moving. 
		self.moving_right = False
		self.moving_left = False
		# self.moving_up = False
		# self.moving_down = False

	def update(self):
		'''Update the ship's position based on the movement flag.'''
		#Update the ship's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		#Using up down key to control the ship movments
		# if self.moving_up and self.rect.up > self.screen_rect.up:
		# 	self.x += self.settings.ship_speed
		# if self.moving_down and self.rect.down > 0:
		# 	self.x += self.settings.ship_speed
		#Update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""Center the ship on the screen. """
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)