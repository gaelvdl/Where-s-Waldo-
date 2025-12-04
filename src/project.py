import pygame

def loading_screen(screen, resolution):
	pygame.display.set_caption("Loading...")
	screen.fill("black")
	resolution = (961, 964)
	screen = pygame.display.set_mode(resolution)
	loading_image = pygame.image.load('Loading.png')
	loading_image = pygame.transform.scale(loading_image, resolution)

	
		

def main():
	pygame.init()
	pygame.display.set_caption("Where's Waldo?")
	resolution = (961, 964)
	# create the display first, then load/scale the background image
	screen = pygame.display.set_mode(resolution)
	screen.fill("black")
	frames = []
	dt = 0
	bg_image = pygame.image.load('waldo.png')
	frame_delay = 40  
	last_frame_time = pygame.time.get_ticks()
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

		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
