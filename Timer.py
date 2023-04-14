import pygame
import time

pygame.init()

pygame.mixer.music.load("alarm.mp3")

screen = pygame.display.set_mode((600, 650))
font = pygame.font.SysFont('Sans', 35)
font_1 = pygame.font.SysFont('Sans', 31)
font_2 = pygame.font.SysFont('Sans', 50)
font_3 = pygame.font.SysFont('Sans', 100)
font_4 = pygame.font.SysFont('Sans', 40)

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 67, 67)
GREEN = (99, 255, 94)
YELLOW = (255, 246, 155)
CYAN = (193, 252, 255)

text_1 = font.render('+1s', True, BLACK)
text_2 = font.render('-1s', True, BLACK)
text_3 = font_1.render('+1m', True, BLACK)
text_4 = font_1.render('-1m', True, BLACK)
text_5 = font_2.render('START', True, BLACK)
text_6 = font_2.render('RESET', True, WHITE)
text_7 = font.render('+5s', True, BLACK)
text_8 = font.render('-5s', True, BLACK)
text_9 = font_4.render('STOP', True, BLACK)
title = font_2.render("Count Down Timer", True, BLACK)
footer = font_1.render("This program is made by ThanhLiem", True, BLACK)

running = True
Start = False
total_secs = 0

while running:
	screen.fill(YELLOW)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, BLACK, (95, 95, 60, 60))
	pygame.draw.rect(screen, WHITE, (100, 100, 50, 50))
	pygame.draw.rect(screen, BLACK, (195, 95, 60, 60))
	pygame.draw.rect(screen, WHITE, (200, 100, 50, 50))
	pygame.draw.rect(screen, BLACK, (95, 245, 60, 60))
	pygame.draw.rect(screen, WHITE, (100, 250, 50, 50))
	pygame.draw.rect(screen, BLACK, (195, 245, 60, 60))
	pygame.draw.rect(screen, WHITE, (200, 250, 50, 50))
	pygame.draw.rect(screen, BLACK, (95, 170, 60, 60))
	pygame.draw.rect(screen, WHITE, (100, 175, 50, 50))
	pygame.draw.rect(screen, BLACK, (195, 170, 60, 60))
	pygame.draw.rect(screen, WHITE, (200, 175, 50, 50))

	pygame.draw.rect(screen, BLACK, (345, 95, 160, 110))
	pygame.draw.rect(screen, GREEN, (350, 100, 150, 100))
	pygame.draw.rect(screen, BLACK, (345, 195, 160, 110))
	pygame.draw.rect(screen, RED, (350, 200, 150, 100))

	pygame.draw.circle(screen, BLACK, (300, 450), 130)
	pygame.draw.circle(screen, CYAN, (300, 450), 125)
	pygame.draw.rect(screen, BLACK, (248, 348, 104, 54))
	pygame.draw.rect(screen, WHITE, (250, 350, 100, 50))
	

	screen.blit(title, (130, 15))
	screen.blit(text_1, (100, 105))
	screen.blit(text_2, (205, 105))
	screen.blit(text_7, (100, 180))
	screen.blit(text_8, (203, 180))
	screen.blit(text_3, (100, 255))
	screen.blit(text_4, (205, 255))
	screen.blit(text_5, (358, 120))
	screen.blit(text_6, (358, 220))
	screen.blit(text_9, (255, 352))
	screen.blit(footer, (95, 600))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (95 < mouse_x < 155) and (95 < mouse_y < 155):
					total_secs += 1
					print ("press +1s")
				if (195 < mouse_x < 255) and (95 < mouse_y < 155):
					if (total_secs > 0):
						total_secs -= 1
					print ("press -1s")
				if (95 < mouse_x < 155) and (170 < mouse_y < 230):
					total_secs += 5
					print ("press +5s")
				if (195 < mouse_x < 255) and (170 < mouse_y < 230):
					if (total_secs > 4):
						total_secs -= 5
					print ("press -5s")
				if (95 < mouse_x < 155) and (245 < mouse_y < 305):
					total_secs += 60
					print ("press +1m")
				if (195 < mouse_x < 255) and (245 < mouse_y < 305):
					if (total_secs > 59):
						total_secs -= 60
					print ("press -1m")
				if (345 < mouse_x < 505) and (95 < mouse_y < 200):
					if total_secs > 0:
						Start = True
					else: 
						Start = False
					print ("press START")
				if (345 < mouse_x < 505) and (200 < mouse_y < 315):
					Start = False
					total_secs = 0
					print ("press RESET")
				if (248 < mouse_x < 352) and (348 < mouse_y < 402):
					Start = False
					print ("press STOP")

	if Start == True:
		time.sleep(1)
		total_secs -= 1
		if (total_secs <= 0):
			Start = False
			pygame.mixer.music.play()
			print ("Time out!!!")

	mins = total_secs // 60
	secs = total_secs % 60

	time_display = '{:02d}:{:02d}'.format(mins, secs)
	text_time = font_3.render(time_display, True, BLACK)
	screen.blit(text_time, (197, 390))

	pygame.display.flip()

pygame.quit()