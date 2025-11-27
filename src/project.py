import pygame


def main():
	pygame.init()
	pygame.display.set_caption("Where's Waldo?")

	dt = 0
	resolution = (961, 964)
	# create the display first, then load/scale the background image
	screen = pygame.display.set_mode(resolution)
	bg_image = pygame.image.load('waldo.png')
	explosion_1 = pygame.image.load('waldo_explosion_1.gif')
	explosion_2 = pygame.image.load('waldo_explosion_secret.gif')
	bg_image = pygame.transform.scale(bg_image, resolution)
	start_time = pygame.time.get_ticks()
	show_image = False
	explosion_pos = (0, 0)
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				# record the position and request showing the explosion
				explosion_pos = pygame.mouse.get_pos()
				show_image = True
			if event.type == pygame.QUIT:
				running = False

		# draw the background each frame before flipping
		screen.blit(bg_image, (0, 0))

		if show_image:
			rect = explosion_1.get_rect(center=explosion_pos)
			screen.blit(explosion_1, rect)

		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
