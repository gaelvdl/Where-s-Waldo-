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
	explosion = cv2.VideoCapture('Waldo_Explode.mp4')
	frame_delay = 40  
	last_frame_time = pygame.time.get_ticks()
	bg_image = pygame.transform.scale(bg_image, resolution)
	start_time = pygame.time.get_ticks()
	show_image = False
	explosion_pos = (0, 0)
	running = True
	video_finished = False

	while running:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				rect_x1, rect_y1 = 50,300
				rect_x2, rect_y2 = 100,359
				if rect_x1 <= mouse_x <= rect_x2 and rect_y1 <= mouse_y <= rect_y2:
					show_image = True
					explosion_pos = (mouse_x, mouse_y)
					frames = []
					while True:
						ret, frame = explosion.read()
						if not ret:
							break
						frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
						frame = cv2.resize(frame, resolution)
						new_frames = pygame.surfarray.make_surface(frame)
						frames.append(frame)
					for frame in frames:
						frame = pygame.surfarray.make_surface(frame)
						screen.blit(frame, (0, 0))
						pygame.time.delay(frame_delay)
						pygame.display.flip()
					video_finished = True
					if video_finished == True:
						menu(screen, resolution)
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
	mainmenu.mainloop(screen, bgfun=lambda: draw_background(screen, bg_image))

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
