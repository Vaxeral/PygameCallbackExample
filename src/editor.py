# from PyQt5 import QtCore, GtGui, GtWidgets

# import pygame

# class Image

import pygame

from main import update, render, settings, handle_event

editor = None

class Editor:
	def __init__(self, settings, callback_update, callback_render, callback_handle_event):
		pygame.init()
		
		self.settings = settings
		self.callback_update = callback_update
		self.callback_render = callback_render
		self.callback_handle_event = callback_handle_event
		self.clock = pygame.time.Clock()
		self.is_running = True

		pygame.display.set_caption("Hello Pygame")
		pygame.display.set_mode((640, 480)) #  Ideally set from settings passed in
	
		self.window = pygame.display.get_surface()


	def handle_event(self, event):

		#  Take care of basic events
		if event.type == pygame.QUIT:
			self.is_running = False
		self.callback_handle_event(event)

	def update(self, dt):
		self.callback_update(dt)

	def render(self, window):
		self.callback_render(window)

	def run(self):
		while self.is_running:
			for event in pygame.event.get():
				self.handle_event(event)
			dt = self.clock.tick(60)
			self.update(dt)
			self.render(self.window)

def init():
  global editor
  global settings
  global update
  global render
  global handle_event
  editor = Editor(settings, update, render, handle_event)

init()

editor.run()