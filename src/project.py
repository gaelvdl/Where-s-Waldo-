import pygame


def main():
	pygame.init()
	pygame.display.set_caption("Where's Waldo?")

	# load all 149 frames into a list
	frames = []
	for frame in range(150):
		img = pygame.image.load(f'frame_{frame:03d}_delay-0.04s.gif').convert_alpha()
		frames.append(img)
		pygame.image.load(f'frame_{frame:03d}_delay-0.04s.gif')
	dt = 0
	resolution = (961, 964)
	# create the display first, then load/scale the background image
	screen = pygame.display.set_mode(resolution)
	bg_image = pygame.image.load('waldo.png')
	explosion_1 = pygame.image.load('')
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
