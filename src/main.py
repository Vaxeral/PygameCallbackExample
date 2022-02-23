import pygame

settings = None

time_accumalted = 0.0

def update(dt):
	global time_accumalted
	time_accumalted += dt

def render(window):
	window.fill((0, 0, 0, 255))
	pygame.draw.rect(window, (255, 255, 255, 255), pygame.Rect(0, 0, 20, 20))
	pygame.display.update()

def handle_event(event):
	pass