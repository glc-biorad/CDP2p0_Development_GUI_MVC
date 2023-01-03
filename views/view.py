"""
Main Graphical representation of the GUI
"""

import customtkinter as ctk
import tkinter as tk

from models.model import Model

from views.menu_frame import MenuFrame

from views.build_protocol_frame import BuildProtocolFrame

# Constants
TITLE = "CDP 2.0 Development GUI"
WIDTH = 780
HEIGHT = 520
RIGHT_FRAME_WIDTH = 600
RIGHT_FRAME_HEIGHT = 520
MENU_WIDTH = 180
MENU_HEIGHT = 520
MENU_POSX = 0
MENU_POSY = 0

# Appearance and Theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

class View(ctk.CTk):
	def __init__(self, model: Model) -> None:
		super().__init__()
		self.model = model
		self.title(TITLE)
		self.geometry(f"{WIDTH}x{HEIGHT}")
		self.menu_frame = MenuFrame(self, MENU_WIDTH, MENU_HEIGHT, MENU_POSX, MENU_POSY, RIGHT_FRAME_WIDTH, RIGHT_FRAME_HEIGHT)
		self.create_ui()
		
	def create_ui(self) -> None:
		# Create the MenuFrame
		self.menu_frame.create_ui()
	
