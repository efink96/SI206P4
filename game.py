import random
import sys

import pygame

# character will be on the ground the whole time (able to move horizontally), and they will catch as much fruit as possible in 60 seconds
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP, Rect, FULLSCREEN, QUIT, DOUBLEBUF

LEFT, RIGHT = 0, 1
START, STOP = 0, 1

X_MAX = 600
Y_MAX = 600

everything = pygame.sprite.Group()

class Basket(pygame.sprite.Sprite):
	def __init__(self):
		super(Basket, self).__init__()
		self.image = pygame.image.load("basket.png")
		self.rect = self.image.get_rect()
		self.rect.center = (X_MAX/2, Y_MAX - 30)
		self.dx = 0
		self.dy = 0

	def steer(self, direction, operation):
		v = 10
		if operation == START:
			if direction in (LEFT, RIGHT):
				self.dx = {LEFT: -v, RIGHT: v}[direction]
		if operation == STOP:
			if direction in (LEFT, RIGHT):
				self.dx = 0

class Apple(pygame.sprite.Sprite):
	def __init__(self, x_pos, groups):
		super(Apple, self).__init__()
		self.image = pygame.image.load("apple.png")
		self.rect = self.image.get_rect()
		self.rect.center = (0, x_pos)
		self.dx = 0
		self.dy = 0
		self.velocity = 7

	def update(self):
		x, y = self.rect.center

		if y > Y_MAX:
			x, y = random.randint(0, X_MAX), 0
			self.velocity = 7
		else:
			x, y = x, y + self.velocity

		self.rect.center = x, y

	def caught_in_basket(self):
		super(Apple, self).kill()

class Banana(pygame.sprite.Sprite):
	def __init__(self, x_pos, groups):
		super(Banana, self).__init__()
		self.image = pygame.image.load("banana.png")
		self.rect = self.image.get_rect()
		self.rect.center = (0, x_pos)
		self.dx = 0
		self.dy = 0
		self.velocity = 7

	def update(self):
		x, y = self.rect.center

		if y > Y_MAX:
			x, y = random.randint(0, X_MAX), 0
			self.velocity = 7
		else:
			x, y = x, y + self.velocity

		self.rect.center = x, y

	def caught_in_basket(self):
 		super(Banana, self).kill()

class Carrot(pygame.sprite.Sprite):
	def __init__(self, x_pos, groups):
		super(Carrot, self).__init__()
		self.image = pygame.image.load("carrot.png")
		self.rect = self.image.get_rect()
		self.rect.center = (0, x_pos)
		self.dx = 0
		self.dy = 0
		self.velocity = 7

	def update(self):
		x, y = self.rect.center

		if y > Y_MAX:
			x, y = random.randint(0, X_MAX), 0
			self.velocity = 7
		else:
			x, y = x, y + self.velocity

		self.rect.center = x, y

	def caught_in_basket(self):
		super(Carrot, self).kill()


def main():
	print("here")
	game_over = False
	screen = pygame.display.set_mode((X_MAX, Y_MAX), DOUBLEBUF)
	time = pygame.time.Clock()

	apples = pygame.sprite.Group()
	bananas = pygame.sprite.Group()
	carrots = pygame.sprite.Group()

	basket = Basket()


	for i in range(5):
		pos1 = random.randint(0, X_MAX)
		obj1 = Apple(pos1, everything)
		apples.add(obj1)

	for j in range(3):
		pos2 = random.randint(0, X_MAX)
		obj2 = Banana(pos2, everything)
		bananas.add(obj2)

	for k in range(2):
		pos3 = random.randint(0, X_MAX)
		obj3 = Carrot(pos3, everything)
		carrots.add(obj3)

	while True:
		time.tick(30)
		apples.draw(screen)
		bananas.draw(screen)
		carrots.draw(screen)

		for event in pygame.event.get():
			if not game_over:
				if event.type == KEYDOWN:
					if event.key == K_RIGHT:
						basket.steer(RIGHT, START)
					if event.key == K_LEFT:
						basket.steer(LEFT, START)
				if event.type == KEYUP:
					if event.key == K_RIGHT:
						basket.steer(RIGHT, STOP)
					if event.key == K_LEFT:
						basket.steer(LEFT, STOP)

		catch_apple = pygame.sprite.spritecollide(basket, apples, True)
		for i in catch_apple: 
			basket.score += 10
			i.caught_in_basket()

		catch_banana = pygame.sprite.spritecollide(basket, bananas, True)
		for j in catch_banana:
			basket.score += 20
			j.caught_in_basket()

		catch_carrot = pygame.sprite.spritecollide(basket, carrots, True)
		for k in catch_carrot:
			basket.score += 30
			k.caught_in_basket()

	everything.clear(screen, empty)
	everything.update()
	everything.draw(screen)
	pygame.display.flip()

if __name__ == '__main__':
	main()