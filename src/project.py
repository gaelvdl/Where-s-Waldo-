import pygame
import pygame_menu
import cv2
import imageio as iio

pygame.init()

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
	explosion = cv2.VideoCapture('explosion.mp4')
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


def play_game():
	main()

def menu(screen, resolution):
	pygame.display.set_caption("Where's Waldo?")
	surface = pygame.display.set_mode(resolution)

def draw_background(screen, bg_image):
	screen.blit(bg_image, (0, 0))

if __name__ == "__main__":
	resolution = (961, 964)
	screen = pygame.display.set_mode(resolution)
	
	bg_image = pygame.image.load('Loading.png')
	bg_image = pygame.transform.scale(bg_image, resolution)
	
	mainmenu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)
	mainmenu.add.button('Play', play_game)
	mainmenu.add.button('Quit', pygame_menu.events.EXIT)
	
	mainmenu.mainloop(screen, bgfun=lambda: draw_background(screen, bg_image))
