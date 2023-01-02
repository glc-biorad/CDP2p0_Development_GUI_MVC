import types
import customtkinter as ctk

import threading
import time
from PIL import Image
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Import the Controller for the Thermocycle View
from controllers.thermocycle_controller import ThermocycleController

# Import the Model for the Thermocycle View
from models.thermocycle_model import ThermocycleModel

# Constants
TRAY_N_STEPS=500
LABEL_THERMOCYCLER_PROTOCOL_POSX = 50
LABEL_THERMOCYCLER_PROTOCOL_POSY = 5
LABEL_THERMOCYCLER_POSX = 10
LABEL_THERMOCYCLER_POSY = 40
OPTIONMENU_THERMOCYCLER_POSX = 150
OPTIONMENU_THERMOCYCLER_POSY = 40
LABEL_CYCLES_POSX = 10
LABEL_CYCLES_POSY = 80
ENTRY_CYCLES_POSX = 150
ENTRY_CYCLES_POSY = 80
IMAGE_THERMOCYCLERS_POSX = 310
IMAGE_THERMOCYCLERS_POSY = 5
IMAGE_THERMOCYCLERS_WIDTH = 250
IMAGE_THERMOCYCLERS_HEIGHT = 470
IMAGE_THERMOCYCLER_RAILS_POSX = 310
IMAGE_THERMOCYCLER_RAILS_POSY = 5
IMAGE_THERMOCYCLER_RAILS_WIDTH = 250
IMAGE_THERMOCYCLER_RAILS_HEIGHT = 470
TRAY_CLOSED_POSX = 435
IMAGE_THERMOCYCLER_TRAY_AB_POSX = 314
IMAGE_THERMOCYCLER_TRAY_AB_POSY = 17
IMAGE_THERMOCYCLER_TRAY_AB_WIDTH = 100
IMAGE_THERMOCYCLER_TRAY_AB_HEIGHT = 225
IMAGE_THERMOCYCLER_BLOCK_AB_POSX = 445
IMAGE_THERMOCYCLER_BLOCK_AB_POSY = 37
IMAGE_THERMOCYCLER_BLOCK_AB_WIDTH = 97
IMAGE_THERMOCYCLER_BLOCK_AB_HEIGHT = 185
IMAGE_THERMOCYCLER_TRAY_CD_POSX = 314
IMAGE_THERMOCYCLER_TRAY_CD_POSY = 242
IMAGE_THERMOCYCLER_TRAY_CD_WIDTH = 100
IMAGE_THERMOCYCLER_TRAY_CD_HEIGHT = 225
IMAGE_THERMOCYCLER_BLOCK_CD_POSX = 445
IMAGE_THERMOCYCLER_BLOCK_CD_POSY = 262
IMAGE_THERMOCYCLER_BLOCK_CD_WIDTH = 97
IMAGE_THERMOCYCLER_BLOCK_CD_HEIGHT = 185
BUTTON_BLOCK_LEFT_POSX = 418
BUTTON_BLOCK_LEFT_POSY = 13
BUTTON_BLOCK_LEFT_WIDTH = 25
BUTTON_BLOCK_LEFT_HEIGHT = 460
BUTTON_BLOCK_RIGHT_POSX = 542
BUTTON_BLOCK_RIGHT_POSY = 13
BUTTON_BLOCK_RIGHT_WIDTH = 25
BUTTON_BLOCK_RIGHT_HEIGHT = 460
BUTTON_BLOCK_TOP_POSX = 418
BUTTON_BLOCK_TOP_POSY = 13
BUTTON_BLOCK_TOP_WIDTH = 149
BUTTON_BLOCK_TOP_HEIGHT = 12
BUTTON_BLOCK_BOTTOM_POSX = 418
BUTTON_BLOCK_BOTTOM_POSY = 462
BUTTON_BLOCK_BOTTOM_WIDTH = 149
BUTTON_BLOCK_BOTTOM_HEIGHT = 12
BUTTON_START_POSX = 45
BUTTON_START_POSY = 480
BUTTON_START_WIDTH = 55
BUTTON_LOAD_POSX = 105
BUTTON_LOAD_POSY = 480
BUTTON_LOAD_WIDTH = 55
BUTTON_SAVE_POSX = 165
BUTTON_SAVE_POSY = 480
BUTTON_SAVE_WIDTH = 55
BUTTON_HOME_POSX = 225
BUTTON_HOME_POSY = 480
BUTTON_HOME_WIDTH = 55
PROGRESSBAR_THERMOCYCLER_POSX = 30
PROGRESSBAR_THERMOCYCLER_POSY = 432
PROGRESSBAR_THERMOCYCLER_WIDTH = 260
PROGRESSBAR_THERMOCYCLER_HEIGHT = 25
IMAGE_THERMOMETER_POSX = 15
IMAGE_THERMOMETER_POSY = 365
IMAGE_THERMOMETER_WIDTH = 24
IMAGE_THERMOMETER_HEIGHT = 24
IMAGE_CLOCK_POSX = 15
IMAGE_CLOCK_POSY = 395
IMAGE_CLOCK_WIDTH = 24
IMAGE_CLOCK_HEIGHT = 24
LABEL_A_POSX = 320
LABEL_A_POSY = 485
CHECKBOX_A_POSX = 340
CHECKBOX_A_POSY = 485
LABEL_B_POSX = 380
LABEL_B_POSY = 485
CHECKBOX_B_POSX = 400
CHECKBOX_B_POSY = 485
LABEL_C_POSX = 440
LABEL_C_POSY = 485
CHECKBOX_C_POSX = 460
CHECKBOX_C_POSY = 485
LABEL_D_POSX = 500
LABEL_D_POSY = 485
CHECKBOX_D_POSX = 520
CHECKBOX_D_POSY = 485
ENTRY_FIRST_DENATURE_TEMP_POSX = 65
ENTRY_FIRST_DENATURE_TEMP_POSY = 365
ENTRY_FIRST_DENATURE_TEMP_WIDTH = 40
ENTRY_ANNEAL_TEMP_POSX = 145
ENTRY_ANNEAL_TEMP_POSY = 365
ENTRY_ANNEAL_TEMP_WIDTH = 40
ENTRY_SECOND_DENATURE_TEMP_POSX = 225
ENTRY_SECOND_DENATURE_TEMP_POSY = 365
ENTRY_SECOND_DENATURE_TEMP_WIDTH = 40
ENTRY_FIRST_DENATURE_TIME_POSX = 65
ENTRY_FIRST_DENATURE_TIME_POSY = 395
ENTRY_FIRST_DENATURE_TIME_WIDTH = 40
ENTRY_SECOND_DENATURE_TEMP_WIDTH = 40
ENTRY_ANNEAL_TIME_POSX = 145
ENTRY_ANNEAL_TIME_POSY = 395
ENTRY_ANNEAL_TIME_WIDTH = 40
ENTRY_SECOND_DENATURE_TIME_POSX = 225
ENTRY_SECOND_DENATURE_TIME_POSY = 395
ENTRY_SECOND_DENATURE_TIME_WIDTH = 40

# Button Titles
BUTTON_TITLES = [
	'Start',
	'Load',
	'Save',
	'Home',
]

# Image Paths
IMAGE_PATHS = {
	'thermocyclers': './images/thermocyclers.png',
	'thermocycler_rails': './images/thermocycler_rails.png',
	'thermocycler_block': './images/thermocycler_block.png',
	'thermocycler_tray': './images/thermocycler_tray.png',
	'thermometer': './images/thermometer.png', # Credit goes to author (Freepik)
	'clock': './images/clock.png', # Credit goes to author (Freepik)
}

class ThermocycleFrame(ctk.CTkFrame):
	"""
	Thermocycle Frame: UI for the Thermocycle view
	"""
	def __init__(self, master: ctk.CTk, width: int, height: int, posx: int, posy: int) -> None:
		self.master = master
		self.width = width
		self.height = height
		self.posx = posx
		self.posy = posy
		self.controller = ThermocycleController(ThermocycleModel(), self)
		self.buttons = {}
		super().__init__(
			master=self.master,
			width=self.width,
			height=self.height,
			corner_radius=0,
		)

	def create_ui(self) -> None:
		# Place Thermocycle Frame
		self.place(x=self.posx, y=self.posy)
		# Place the Thermocycler Protocol Label
		self.label_thermocycler_protocol = ctk.CTkLabel(master=self, text="Thermocycler Protocol", font=("Roboto Bold", -20))
		self.label_thermocycler_protocol.place(x=LABEL_THERMOCYCLER_PROTOCOL_POSX, y=LABEL_THERMOCYCLER_PROTOCOL_POSY)
		# Place the Thermocycler Option Menu
		self.label_thermocycler = ctk.CTkLabel(master=self, text='Thermocycler', font=("Roboto Light", -16))
		self.label_thermocycler.place(x=LABEL_THERMOCYCLER_POSX, y=LABEL_THERMOCYCLER_POSY)
		thermocycler_sv = self.controller.get_thermocycler_sv(1)
		self.optionmenu_thermocycler = ctk.CTkOptionMenu(
			master=self,
			variable=thermocycler_sv,
			values=('A', 'B', 'C', 'D'),
		)
		self.optionmenu_thermocycler.place(x=OPTIONMENU_THERMOCYCLER_POSX, y=OPTIONMENU_THERMOCYCLER_POSY)
		# Place the Cycles Entry
		self.label_cycles = ctk.CTkLabel(master=self, text='Cycles', font=("Roboto Light", -16))
		self.label_cycles.place(x=LABEL_CYCLES_POSX, y=LABEL_CYCLES_POSY)
		cycles_sv = self.controller.get_cycles_sv(1)
		self.entry_cycles = ctk.CTkEntry(
			master=self,
			textvariable=cycles_sv,
		)
		self.entry_cycles.bind('<FocusOut>', self.callback_cycles)
		self.entry_cycles.place(x=ENTRY_CYCLES_POSX, y=ENTRY_CYCLES_POSY)
		# Place the Thermocycler Image
		self.photoimage_thermocycler_rails = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermocycler_rails']),
			size=(IMAGE_THERMOCYCLER_RAILS_WIDTH, IMAGE_THERMOCYCLER_RAILS_HEIGHT),
		)
		self.image_thermocycler_rails = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermocycler_rails)
		self.image_thermocycler_rails.place(x=IMAGE_THERMOCYCLER_RAILS_POSX, y=IMAGE_THERMOCYCLER_RAILS_POSY)
		self.image_thermocycler_rails.bind('<Button-1>', self.on_click_rails)
		self.photoimage_thermocycler_tray_ab = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermocycler_tray']),
			size=(IMAGE_THERMOCYCLER_TRAY_AB_WIDTH, IMAGE_THERMOCYCLER_TRAY_AB_HEIGHT),
		)
		self.image_thermocycler_tray_ab = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermocycler_tray_ab)
		self.image_thermocycler_tray_ab.place(x=IMAGE_THERMOCYCLER_TRAY_AB_POSX, y=IMAGE_THERMOCYCLER_TRAY_AB_POSY)
		self.image_thermocycler_tray_ab.bind('<Button-1>', self.on_click_tray_ab)
		self.photoimage_thermocycler_block_ab = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermocycler_block']),
			size=(IMAGE_THERMOCYCLER_BLOCK_AB_WIDTH, IMAGE_THERMOCYCLER_BLOCK_AB_HEIGHT),
		)
		self.image_thermocycler_block_ab = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermocycler_block_ab)
		self.image_thermocycler_block_ab.place(x=IMAGE_THERMOCYCLER_BLOCK_AB_POSX, y=IMAGE_THERMOCYCLER_BLOCK_AB_POSY)
		self.photoimage_thermocycler_tray_cd = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermocycler_tray']),
			size=(IMAGE_THERMOCYCLER_TRAY_CD_WIDTH, IMAGE_THERMOCYCLER_TRAY_CD_HEIGHT),
		)
		self.image_thermocycler_tray_cd = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermocycler_tray_cd)
		self.image_thermocycler_tray_cd.place(x=IMAGE_THERMOCYCLER_TRAY_CD_POSX, y=IMAGE_THERMOCYCLER_TRAY_CD_POSY)
		self.image_thermocycler_tray_cd.bind('<Button-1>', self.on_click_tray_cd)
		self.photoimage_thermocycler_block_cd = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermocycler_block']),
			size=(IMAGE_THERMOCYCLER_BLOCK_CD_WIDTH, IMAGE_THERMOCYCLER_BLOCK_CD_HEIGHT),
		)
		self.image_thermocycler_block_cd = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermocycler_block_cd)
		self.image_thermocycler_block_cd.place(x=IMAGE_THERMOCYCLER_BLOCK_CD_POSX, y=IMAGE_THERMOCYCLER_BLOCK_CD_POSY)
		self.button_block_left = ctk.CTkButton(
			master=self,
			text='',
			width=BUTTON_BLOCK_LEFT_WIDTH,
			height=BUTTON_BLOCK_LEFT_HEIGHT,
			corner_radius=0,
			state='disabled',
			fg_color='black',
		
		)
		self.button_block_left.place(x=BUTTON_BLOCK_LEFT_POSX, y=BUTTON_BLOCK_LEFT_POSY)
		self.button_block_right = ctk.CTkButton(
			master=self,
			text='',
			width=BUTTON_BLOCK_RIGHT_WIDTH,
			height=BUTTON_BLOCK_RIGHT_HEIGHT,
			corner_radius=0,
			state='disabled',
			fg_color='black',
		
		)
		self.button_block_right.place(x=BUTTON_BLOCK_RIGHT_POSX, y=BUTTON_BLOCK_RIGHT_POSY)
		self.button_block_top = ctk.CTkButton(
			master=self,
			text='',
			width=BUTTON_BLOCK_TOP_WIDTH,
			height=BUTTON_BLOCK_TOP_HEIGHT,
			corner_radius=0,
			state='disabled',
			fg_color='black',
		
		)
		self.button_block_top.place(x=BUTTON_BLOCK_TOP_POSX, y=BUTTON_BLOCK_TOP_POSY)
		self.button_block_bottom = ctk.CTkButton(
			master=self,
			text='',
			width=BUTTON_BLOCK_BOTTOM_WIDTH,
			height=BUTTON_BLOCK_BOTTOM_HEIGHT,
			corner_radius=0,
			state='disabled',
			fg_color='black',
		
		)
		self.button_block_bottom.place(x=BUTTON_BLOCK_BOTTOM_POSX, y=BUTTON_BLOCK_BOTTOM_POSY)
		# Place the Start Button
		self.button_start = ctk.CTkButton(
			master=self,
			text='Start',
			command=self.on_start,
			fg_color='#4C7BD3',
			width=BUTTON_START_WIDTH,
		)
		self.button_start.place(x=BUTTON_START_POSX, y=BUTTON_START_POSY)
		# Place the Load Button
		self.button_load = ctk.CTkButton(
			master=self,
			text='Load',
			command=self.on_load,
			width=BUTTON_LOAD_WIDTH,
		)
		self.button_load.place(x=BUTTON_LOAD_POSX, y=BUTTON_LOAD_POSY)
		# Place the Save Button
		self.button_save = ctk.CTkButton(
			master=self,
			text='Save',
			command=self.on_save,
			width=BUTTON_SAVE_WIDTH,
		)
		self.button_save.place(x=BUTTON_SAVE_POSX, y=BUTTON_SAVE_POSY)
		# Place the Home Button
		self.button_home = ctk.CTkButton(
			master=self,
			text='Home',
			command=self.on_home,
			width=BUTTON_HOME_WIDTH,
		)
		self.button_home.place(x=BUTTON_HOME_POSX, y=BUTTON_HOME_POSY)
		# Place the Thermocycler ProgressBar
		self.progressbar_thermocycler = ctk.CTkProgressBar(
			master=self,
			orientation='horizontal',
			mode='determinate',
			progress_color='green',
			height=PROGRESSBAR_THERMOCYCLER_HEIGHT,
			width=PROGRESSBAR_THERMOCYCLER_WIDTH,
			corner_radius=0,
		)
		self.progressbar_thermocycler.set(0)
		self.progressbar_thermocycler.place(x=PROGRESSBAR_THERMOCYCLER_POSX, y=PROGRESSBAR_THERMOCYCLER_POSY)
		# Place the Thermocycle Protocol Figure
		# Place the 1st Denature Label
		# Place the Anneal Label
		# Place the 2nd Denature Label
		# Place the Thermometer Icon
		self.photoimage_thermometer = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['thermometer']),
			size=(IMAGE_THERMOMETER_WIDTH, IMAGE_THERMOMETER_HEIGHT),
		)
		self.image_thermometer = ctk.CTkLabel(master=self, text='', image=self.photoimage_thermometer)
		self.image_thermometer.place(x=IMAGE_THERMOMETER_POSX, y=IMAGE_THERMOMETER_POSY)
		# Place the Clock Icon
		self.photoimage_clock = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['clock']),
			size=(IMAGE_CLOCK_WIDTH, IMAGE_CLOCK_HEIGHT),
		)
		self.image_clock = ctk.CTkLabel(master=self, text='', image=self.photoimage_clock)
		self.image_clock.place(x=IMAGE_CLOCK_POSX, y=IMAGE_CLOCK_POSY)
		# Place the 1st Denature Temperature Entry
		first_denature_temp_sv = self.controller.get_first_denature_temp_sv(1)
		self.entry_first_denature_temp = ctk.CTkEntry(
			master=self,
			textvariable=first_denature_temp_sv,
			width=ENTRY_FIRST_DENATURE_TEMP_WIDTH,
		)
		self.entry_first_denature_temp.place(x=ENTRY_FIRST_DENATURE_TEMP_POSX, y=ENTRY_FIRST_DENATURE_TEMP_POSY)
		# Place the Anneal Temperature Entry
		anneal_temp_sv = self.controller.get_anneal_temp_sv(1)
		self.entry_anneal_temp = ctk.CTkEntry(
			master=self,
			textvariable=anneal_temp_sv,
			width=ENTRY_ANNEAL_TEMP_WIDTH,
		)
		self.entry_anneal_temp.place(x=ENTRY_ANNEAL_TEMP_POSX, y=ENTRY_ANNEAL_TEMP_POSY)
		# Place the 2nd Denature Temperature Entry
		second_denature_temp_sv = self.controller.get_second_denature_temp_sv(1)
		self.entry_second_denature_temp = ctk.CTkEntry(
			master=self,
			textvariable=second_denature_temp_sv,
			width=ENTRY_SECOND_DENATURE_TEMP_WIDTH,
		)
		self.entry_second_denature_temp.place(x=ENTRY_SECOND_DENATURE_TEMP_POSX, y=ENTRY_SECOND_DENATURE_TEMP_POSY)
		# Place the 1st Denature Time Entry
		first_denature_time_sv = self.controller.get_first_denature_time_sv(1)
		self.entry_first_denature_time = ctk.CTkEntry(
			master=self,
			textvariable=first_denature_time_sv,
			width=ENTRY_FIRST_DENATURE_TIME_WIDTH,
		)
		self.entry_first_denature_time.place(x=ENTRY_FIRST_DENATURE_TIME_POSX, y=ENTRY_FIRST_DENATURE_TIME_POSY)
		# Place the Anneal Time Entry
		anneal_time_sv = self.controller.get_anneal_time_sv(1)
		self.entry_anneal_time = ctk.CTkEntry(
			master=self,
			textvariable=anneal_time_sv,
			width=ENTRY_ANNEAL_TIME_WIDTH,
		)
		self.entry_anneal_time.place(x=ENTRY_ANNEAL_TIME_POSX, y=ENTRY_ANNEAL_TIME_POSY)
		# Place the 2nd Denature Time Entry
		second_denature_time_sv = self.controller.get_second_denature_time_sv(1)
		self.entry_second_denature_time = ctk.CTkEntry(
			master=self,
			textvariable=second_denature_time_sv,
			width=ENTRY_SECOND_DENATURE_TIME_WIDTH,
		)
		self.entry_second_denature_time.place(x=ENTRY_SECOND_DENATURE_TIME_POSX, y=ENTRY_SECOND_DENATURE_TIME_POSY)
		# Place the A Checkbox
		self.label_a = ctk.CTkLabel(master=self, text='A', font=("Roboto Bold", -12))
		self.label_a.place(x=LABEL_A_POSX, y=LABEL_A_POSY)
		use_a_iv = self.controller.get_use_a_iv(1)
		self.checkbox_a = ctk.CTkCheckBox(
			master=self,
			text='',
			variable=use_a_iv,
			onvalue=1,
			offvalue=0,
		)
		self.checkbox_a.place(x=CHECKBOX_A_POSX, y=CHECKBOX_A_POSY)
		# Place the B Checkbox
		self.label_b = ctk.CTkLabel(master=self, text='B', font=("Roboto Bold", -12))
		self.label_b.place(x=LABEL_B_POSX, y=LABEL_B_POSY)
		use_b_iv = self.controller.get_use_b_iv(2)
		self.checkbox_b = ctk.CTkCheckBox(
			master=self,
			text='',
			variable=use_b_iv,
			onvalue=1,
			offvalue=0,
		)
		self.checkbox_b.place(x=CHECKBOX_B_POSX, y=CHECKBOX_B_POSY)
		# Place the C Checkbox
		self.label_c = ctk.CTkLabel(master=self, text='C', font=("Roboto Bold", -12))
		self.label_c.place(x=LABEL_C_POSX, y=LABEL_C_POSY)
		use_c_iv = self.controller.get_use_c_iv(3)
		self.checkbox_c = ctk.CTkCheckBox(
			master=self,
			text='',
			variable=use_c_iv,
			onvalue=1,
			offvalue=0,
		)
		self.checkbox_c.place(x=CHECKBOX_C_POSX, y=CHECKBOX_C_POSY)
		# Place the D Checkbox
		self.label_d = ctk.CTkLabel(master=self, text='D', font=("Roboto Bold", -12))
		self.label_d.place(x=LABEL_D_POSX, y=LABEL_D_POSY)
		use_d_iv = self.controller.get_use_d_iv(4)
		self.checkbox_d = ctk.CTkCheckBox(
			master=self,
			text='',
			variable=use_d_iv,
			onvalue=1,
			offvalue=0,
		)
		self.checkbox_d.place(x=CHECKBOX_D_POSX, y=CHECKBOX_D_POSY)

	def callback_cycles(self, event):
		print('Cycles')

	def on_click(self, event):
		x, y = event.x, event.y
		print(f"{x}, {y}")

	def on_click_tray_ab(self, event):
		# Get the current posx
		posx = self.image_thermocycler_tray_ab.place_info()['x']
		# Make sure the tray is allowed to close
		if True:
			# Change the posx
			thread = threading.Thread(
				target=self.move_tray, 
				args=(
					self.image_thermocycler_tray_ab, 
					IMAGE_THERMOCYCLER_TRAY_AB_POSX,
					TRAY_CLOSED_POSX, 
				)
			)
			thread.start()

	def on_click_tray_cd(self, event):
		# Get the current posx
		posx = self.image_thermocycler_tray_cd.place_info()['x']
		# Make sure the tray is allowed to close
		if True:
			# Change the posx
			thread = threading.Thread(
				target=self.move_tray, 
				args=(
					self.image_thermocycler_tray_cd, 
					IMAGE_THERMOCYCLER_TRAY_CD_POSX,
					TRAY_CLOSED_POSX, 
				)
			)
			thread.start()

	def on_click_rails(self, event):
		# Get x and y from the click event
		x, y = event.x, event.y
		# Determine which tray is being clicked
		if x >= 5 and x <= 106 and y >= 16 and y <= 235:
			# Make sure tray ab is allowed to open
			if True:
				# Open the tray (change posx)
				thread = threading.Thread(
					target=self.move_tray, 
					args=(
						self.image_thermocycler_tray_ab, 
						TRAY_CLOSED_POSX, 
						IMAGE_THERMOCYCLER_TRAY_AB_POSX,
					)
				)
				thread.start()
		elif x >= 5 and x <= 106 and y >= 241 and y <= 463:
			# Make sure tray cd is allowed to open
			if True:
				# Open the tray (change posx)
				thread = threading.Thread(
					target=self.move_tray, 
					args=(
						self.image_thermocycler_tray_cd, 
						TRAY_CLOSED_POSX, 
						IMAGE_THERMOCYCLER_TRAY_CD_POSX,
					)
				)
				thread.start()

	def move_tray(self, image_tray: ctk.CTkLabel, x0:int , x:int , seconds:int=1, n_steps:int=TRAY_N_STEPS) -> None:
		dx = (x-x0)/n_steps
		dt = seconds/n_steps
		for i in range(n_steps):
			image_tray.place(x=x0)
			x0 = x0 + dx
			time.sleep(dt)
		image_tray.place(x=x)
			

	def on_start(self):
		print('Start')

	def on_load(self):
		print('Load')

	def on_save(self):
		print('Save')

	def on_home(self):
		print('Home')
