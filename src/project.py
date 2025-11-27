import pygame











def main():
	pygame.init()
	pygame.display.set_caption("Where's Waldo?")
	clock = pygame.time.Clock()
	dt = 0
	resolution = (1920, 1080)
	screen = pygame.display.set_mode(resolution)
	bg_image = pygame.image.load('waldo.png')
	bg_image = pygame.transform.scale(bg_image, resolution)
	start_time = pygame.time.get_ticks()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.mouse
			if event.type == pygame.QUIT:
				running = False

		elapsed_time = current_time - start_time

		dt = clock.tick(12)
	pygame.quit()

if __name__ == "__main__":
	main()
