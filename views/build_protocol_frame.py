from typing import Any, Callable
from tkinter import StringVar
from PIL import Image
import customtkinter as ctk
import tkinter as tk

# Import the BuildProtocolModel
from models.model import Model
from models.build_protocol_model import BuildProtocolModel

# Constants
IMAGE_CHECK_WIDTH = 20
IMAGE_CHECK_HEIGHT = 20
BUTTON_ADD_COLOR = '#10adfe'
LABEL_TIPS_POSX = 5
LABEL_TIPS_POSY = 40
LABEL_TIPS_TRAY_POSX = 190
LABEL_TIPS_TRAY_POSY = 10
OPTIONMENU_TIPS_TRAY_POSX = 80
OPTIONMENU_TIPS_TRAY_POSY = 40
OPTIONMENU_TIPS_TRAY_WIDTH = 250
LABEL_TIPS_COLUMN_POSX = 345
LABEL_TIPS_COLUMN_POSY = 10
OPTIONMENU_TIPS_COLUMN_POSX = 335
OPTIONMENU_TIPS_COLUMN_POSY = 40
OPTIONMENU_TIPS_COLUMN_WIDTH = 65
LABEL_TIPS_ACTION_POSX = 435
LABEL_TIPS_ACTION_POSY = 10
OPTIONMENU_TIPS_ACTION_POSX = 405
OPTIONMENU_TIPS_ACTION_POSY = 40
OPTIONMENU_TIPS_ACTION_WIDTH = 100
LABEL_TIPS_ADD_POSX = 517
LABEL_TIPS_ADD_POSY = 10
BUTTON_TIPS_ADD_POSX = 510
BUTTON_TIPS_ADD_POSY = 40
BUTTON_TIPS_ADD_WIDTH = 40
LABEL_MOTION_POSX = 5 
LABEL_MOTION_POSY = 100
LABEL_MOTION_CONSUMABLE_POSX = 163
LABEL_MOTION_CONSUMABLE_POSY = 70
OPTIONMENU_MOTION_CONSUMABLE_POSX = 80
OPTIONMENU_MOTION_CONSUMABLE_POSY = 100
OPTIONMENU_MOTION_CONSUMABLE_WIDTH = 235
LABEL_MOTION_TRAY_POSX = 330
LABEL_MOTION_TRAY_POSY = 70
OPTIONMENU_MOTION_TRAY_POSX = 320
OPTIONMENU_MOTION_TRAY_POSY = 100
OPTIONMENU_MOTION_TRAY_WIDTH = 50
LABEL_MOTION_COLUMN_POSX = 375
LABEL_MOTION_COLUMN_POSY = 70
OPTIONMENU_MOTION_COLUMN_POSX = 375
OPTIONMENU_MOTION_COLUMN_POSY = 100
OPTIONMENU_MOTION_COLUMN_WIDTH = 55
LABEL_MOTION_TIP_POSX = 445
LABEL_MOTION_TIP_POSY = 70
OPTIONMENU_MOTION_TIP_POSX = 435 
OPTIONMENU_MOTION_TIP_POSY = 100
OPTIONMENU_MOTION_TIP_WIDTH = 70
LABEL_MOTION_ADD_POSX = 517
LABEL_MOTION_ADD_POSY = 70
BUTTON_MOTION_ADD_POSX = 510
BUTTON_MOTION_ADD_POSY = 100
BUTTON_MOTION_ADD_WIDTH = 40
LABEL_PIPETTOR_POSX = 5
LABEL_PIPETTOR_POSY = 160
LABEL_PIPETTOR_VOLUME_POSX = 92
LABEL_PIPETTOR_VOLUME_POSY = 130
ENTRY_PIPETTOR_VOLUME_POSX = 85
ENTRY_PIPETTOR_VOLUME_POSY = 160
ENTRY_PIPETTOR_VOLUME_WIDTH = 95
LABEL_PIPETTOR_TIP_POSX = 200
LABEL_PIPETTOR_TIP_POSY = 130
OPTIONMENU_PIPETTOR_TIP_POSX = 185
OPTIONMENU_PIPETTOR_TIP_POSY = 160
OPTIONMENU_PIPETTOR_TIP_WIDTH = 70
LABEL_PIPETTOR_ACTION_POSX = 295
LABEL_PIPETTOR_ACTION_POSY = 130
OPTIONMENU_PIPETTOR_ACTION_POSX = 260
OPTIONMENU_PIPETTOR_ACTION_POSY = 160
OPTIONMENU_PIPETTOR_ACTION_WIDTH = 120
LABEL_PIPETTOR_PRESSURE_POSX = 420
LABEL_PIPETTOR_PRESSURE_POSY = 130
OPTIONMENU_PIPETTOR_PRESSURE_POSX = 385
OPTIONMENU_PIPETTOR_PRESSURE_POSY = 160
OPTIONMENU_PIPETTOR_PRESSURE_WIDTH = 120
LABEL_PIPETTOR_ADD_POSX = 517
LABEL_PIPETTOR_ADD_POSY = 130
BUTTON_PIPETTOR_ADD_POSX = 510
BUTTON_PIPETTOR_ADD_POSY = 160
BUTTON_PIPETTOR_ADD_WIDTH = 40
BUTTON_PIPETTOR_ADD_HEIGHT = 25
LABEL_TIME_POSX = 5
LABEL_TIME_POSY = 220
LABEL_TIME_DELAY_POSX = 102
LABEL_TIME_DELAY_POSY = 190
ENTRY_TIME_DELAY_POSX = 85
ENTRY_TIME_DELAY_POSY = 220
ENTRY_TIME_DELAY_WIDTH = 75
LABEL_TIME_UNITS_POSX = 215
LABEL_TIME_UNITS_POSY = 190
OPTIONMENU_TIME_UNITS_POSX = 165
OPTIONMENU_TIME_UNITS_POSY = 220
OPTIONMENU_TIME_UNITS_WIDTH = 120
LABEL_TIME_ADD_POSX = 297
LABEL_TIME_ADD_POSY = 190
BUTTON_TIME_ADD_POSX = 290
BUTTON_TIME_ADD_POSY = 220
BUTTON_TIME_ADD_WIDTH = 40
LABEL_OTHER_POSX = 5
LABEL_OTHER_POSY = 280
LABEL_OTHER_OPTION_POSX = 150
LABEL_OTHER_OPTION_POSY = 250
OPTIONMENU_OTHER_OPTION_POSX = 85
OPTIONMENU_OTHER_OPTION_POSY = 280
OPTIONMENU_OTHER_OPTION_WIDTH = 200
LABEL_OTHER_ADD_POSX = 297
LABEL_OTHER_ADD_POSY = 250
BUTTON_OTHER_ADD_POSX = 290
BUTTON_OTHER_ADD_POSY = 280
BUTTON_OTHER_ADD_WIDTH = 40
TREEVIEW_POSX = 5
TREEVIEW_POSY = 320
TREEVIEW_COLUMN_WIDTH = 440
TREEVIEW_WIDTH = 440
TREEVIEW_HEIGHT = 160
SCROLLBAR_POSX = 5
SCROLLBAR_POSY = 480
SCROLLBAR_WIDTH = 440

# Constants Deck Plate 
NO_TRAY_CONSUMABLES = ["Pre-Amp Thermocycler", "Assay Strip", "Heater/Shaker", "Mag Separator", "Chiller"]
NO_COLUMN_CONSUMABLES = ["Aux Heater", "Sample Rack", "Quant Strip"]
TWELVE_COLUMN_CONSUMABLES = ["Pre-Amp Thermocycler", "Mag Separator", "Chiller", "Reagent Cartridge"]
EIGHT_COLUMN_CONSUMABLES = ["Tip Transfer Tray", "Assay Strip", "Tip Tray"]
FOUR_COLUMN_CONSUMABLES = ["Heater/Shaker"]

# Constant Other Option Values
OTHER_OPTION_VALUES = [
	"Home pipettor",
	"Move relative left",
	"Move relative right",
	"Move relative up",
	"Move relative down",
	"Move relative forwards",
	"Move relative backwards",
	"Generate standard droplets",
	"Generate pico droplets",
	"Extraction",
	"Transfer plasma",
	"Binding",
	"Pooling",
	"Wash 1",
	"Wash 2",
	"Pre-Eultion",
	"Elution",
	"Enrichment",
	"Pre-Amp",
	"Assay Prep",
	"Shake on",
	"Shake off",
	"Engage magnet",
	"Disengage magnet",
	"Pre-Amp Thermocycle",
	"Move lid",
	"Move chip",
]

# Image Paths
IMAGE_PATHS = {
	'check': './images/check.png'
}

class BuildProtocolFrame(ctk.CTkFrame):
	"""
	BuildProtocolFrame for creating the Build Protocol UI View
	"""
	def __init__(self, master: ctk.CTk, width: int, height: int, posx: int, posy: int) -> None:
		"""Constructs the BuildProtocolFrame
	
		Parameters
		----------
		master : ctk.CTk
			The parent widget for this frame
		width : int
			The width of this widget
		height : int
			The height of this widget
		posx : int
			The x position relative to the root origin
		posy : int
			The y position relative to the root origin
		"""
		#self.model = BuildProtocolModel()
		self.model = Model().get_build_protocol_model()
		self.master = master
		self.width = width
		self.height = height
		self.posx = posx
		self.posy = posy
		super().__init__(
			master=self.master,
			width=self.width,
			height=self.height,
			corner_radius=0,
		)
		self.create_ui()

	def create_ui(self) -> None:
		"""Create the UI for the BuildProtocolFrame
		"""
		# Create the photoimage for the check mark
		self.photoimage_check = ctk.CTkImage(
			dark_image=Image.open(IMAGE_PATHS['check']),
			size=(IMAGE_CHECK_WIDTH, IMAGE_CHECK_HEIGHT),
		)
		# Create the Tips Section
		self.create_tips_ui()
		# Create the Motion Section
		self.create_motion_ui()
		# Create the Pipettor Section
		self.create_pipettor_ui()
		# Create the Time Section
		self.create_time_ui()
		# Create the Other Section
		self.create_other_ui()
		# Create the Protocol Action Treeview
		self.create_treeview_ui()
		# Create the Protocol Progress Bar
		# Create the Start Button
		# Create the Load Button
		# Create the Save Button
		# Create the Delete Button

	def place_ui(self) -> None:
		"""Place the UI for the Build Protocol Frame
		"""
		# Place the build protocol frame
		self.place(x=self.posx, y=self.posy)
		# Place the tips section
		self.place_tips_ui()
		# Place the motion section
		self.place_motion_ui()
		# Place the pipettor section
		self.place_pipettor_ui()
		# Place the time section
		self.place_time_ui()
		# Place the other section
		self.place_other_ui()
		# Place the progress bar
		# Place the start, load, save, delete buttons
		# Place the protocol action treeview 
		self.place_treeview_ui()
		

	def create_tips_ui(self) -> None:
		"""Create the UI for the Tips portion of the frame
		"""
		# Create the tips label
		self.label_tips = ctk.CTkLabel(master=self, text='Tips', font=("Roboto Medium", -16))
		# Create the tray label and optionmenu
		self.label_tips_tray = ctk.CTkLabel(master=self, text='Tray', font=("Roboto Medium", -16))
		self.tips_tray_sv = StringVar()
		self.tips_tray_sv.set('')
		self.tips_tray_sv.trace('w', self.callback_tips_tray)
		self.optionmenu_tips_tray = ctk.CTkOptionMenu(
			master=self,
			variable=self.tips_tray_sv,
			values=('A', 'B', 'C', 'D', "Tip Transfer Tray", ''),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_TIPS_TRAY_WIDTH
		)
		# Create the column label and optionmenu
		self.label_tips_column = ctk.CTkLabel(master=self, text='Column', font=("Roboto Medium", -16))
		self.tips_column_sv = StringVar()
		self.tips_column_sv.set('')
		self.tips_column_sv.trace('w', self.callback_tips_column)
		self.optionmenu_tips_column = ctk.CTkOptionMenu(
			master=self,
			variable=self.tips_column_sv,
			values=(''),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_TIPS_COLUMN_WIDTH
		)
		# Create the action label and optionmenu
		self.label_tips_action = ctk.CTkLabel(master=self, text='Action', font=("Roboto Medium", -16))
		self.tips_action_sv = StringVar()
		self.tips_action_sv.set('Eject')
		self.optionmenu_tips_action = ctk.CTkOptionMenu(
			master=self,
			variable=self.tips_action_sv,
			values=('Eject',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_TIPS_ACTION_WIDTH
		)
		# Create the add label and button
		self.label_tips_add = ctk.CTkLabel(master=self, text='Add', font=("Roboto Medium", -14))
		self.button_tips_add = ctk.CTkButton(
			master=self,
			text='',
			#image=self.photoimage_check,
			fg_color=BUTTON_ADD_COLOR,
			width=BUTTON_TIPS_ADD_WIDTH
		)

	def place_tips_ui(self) -> None:
		"""Place the UI for the Tips portion of the frame
		"""
		# Place the tips label
		self.label_tips.place(x=LABEL_TIPS_POSX, y=LABEL_TIPS_POSY)
		# Place the tray label and optionmenu
		self.label_tips_tray.place(x=LABEL_TIPS_TRAY_POSX, y=LABEL_TIPS_TRAY_POSY)
		self.optionmenu_tips_tray.place(x=OPTIONMENU_TIPS_TRAY_POSX, y=OPTIONMENU_TIPS_TRAY_POSY)
		# Place the column label and optionmenu
		self.label_tips_column.place(x=LABEL_TIPS_COLUMN_POSX, y=LABEL_TIPS_COLUMN_POSY)
		self.optionmenu_tips_column.place(x=OPTIONMENU_TIPS_COLUMN_POSX, y=OPTIONMENU_TIPS_COLUMN_POSY)
		# Place the action label and optionmenu
		self.label_tips_action.place(x=LABEL_TIPS_ACTION_POSX, y=LABEL_TIPS_ACTION_POSY)
		self.optionmenu_tips_action.place(x=OPTIONMENU_TIPS_ACTION_POSX, y=OPTIONMENU_TIPS_ACTION_POSY)
		# Place the add label and button
		self.label_tips_add.place(x=LABEL_TIPS_ADD_POSX, y=LABEL_TIPS_ADD_POSY)
		self.button_tips_add.place(x=BUTTON_TIPS_ADD_POSX, y=BUTTON_TIPS_ADD_POSY)
		try:
			print(self.button_tips_add.bind())
		except:
			pass

	def create_motion_ui(self) -> None:
		"""Deals with creating the UI for the Motion section of the Build Protocol Frame
		"""
		# Create the motion label
		self.label_motion = ctk.CTkLabel(master=self, text='Motion', font=("Roboto Medium", -16))
		# Create the consumable label and optionmenu
		self.label_motion_consumable = ctk.CTkLabel(master=self, text='Consumable', font=("Roboto Medium", -16))
		self.motion_consumable_sv = StringVar()
		self.motion_consumable_sv.set('')
		self.motion_consumable_sv.trace('w', self.callback_motion_consumable)
		self.optionmenu_motion_comsumable = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_consumable_sv,
			values=(
				"Assay Strip",
				"Aux Heater",
				"Chiller",
				"Heater/Shaker",
				"Mag Separator",
				"Pre-Amp Thermocycler",
				"Quant Strip",
				"Reagent Cartridge",
				"Sample Rack",
			),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_CONSUMABLE_WIDTH
		)
		# Create the tray label and optionmenu
		self.label_motion_tray = ctk.CTkLabel(master=self, text='Tray', font=("Roboto Medium", -16))
		self.motion_tray_sv = StringVar()
		self.motion_tray_sv.set('')
		self.motion_tray_sv.trace('w', self.callback_motion_tray)
		self.optionmenu_motion_tray = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_tray_sv,
			values=('',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_TRAY_WIDTH,
		)
		# Create the column label and optionmenu
		self.label_motion_column = ctk.CTkLabel(master=self, text='Column', font=("Roboto Medium", -16))
		self.motion_column_sv = StringVar()
		self.motion_column_sv.set('')
		self.optionmenu_motion_column = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_column_sv,
			values=('',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_COLUMN_WIDTH
		)
		# Create the tip label and optionmenu
		self.label_motion_tip = ctk.CTkLabel(master=self, text="Tip (uL)", font=("Roboto Medium", -16))
		self.motion_tip_sv = StringVar()
		self.motion_tip_sv.set('')
		self.optionmenu_motion_tip = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_tip_sv,
			values=('',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_TIP_WIDTH
		)
		# Create the add label and button
		self.label_motion_add = ctk.CTkLabel(master=self, text='Add', font=("Roboto Medium", -14))
		self.button_motion_add = ctk.CTkButton(
			master=self,
			text='',
			#image=self.photoimage_check,
			fg_color=BUTTON_ADD_COLOR,
			width=BUTTON_MOTION_ADD_WIDTH
			#command=self.on_click_motion_add
		)

	def place_motion_ui(self) -> None:
		"""Deals with placing the UI for the Motion section of the Build Protocol Frame
		"""
		# Place the motion label
		self.label_motion.place(x=LABEL_MOTION_POSX, y=LABEL_MOTION_POSY)
		# Place the consumable label and optionmenu
		self.label_motion_consumable.place(x=LABEL_MOTION_CONSUMABLE_POSX, y=LABEL_MOTION_CONSUMABLE_POSY)
		self.optionmenu_motion_comsumable.place(x=OPTIONMENU_MOTION_CONSUMABLE_POSX, y=OPTIONMENU_MOTION_CONSUMABLE_POSY)
		# Place the tray label and optionmenu
		self.label_motion_tray.place(x=LABEL_MOTION_TRAY_POSX, y=LABEL_MOTION_TRAY_POSY)
		self.optionmenu_motion_tray.place(x=OPTIONMENU_MOTION_TRAY_POSX, y=OPTIONMENU_MOTION_TRAY_POSY)
		# Place the column label and optionmenu
		self.label_motion_column.place(x=LABEL_MOTION_COLUMN_POSX, y=LABEL_MOTION_COLUMN_POSY)
		self.optionmenu_motion_column.place(x=OPTIONMENU_MOTION_COLUMN_POSX, y=OPTIONMENU_MOTION_COLUMN_POSY)
		# Place the tip label and optionmenu
		self.label_motion_tip.place(x=LABEL_MOTION_TIP_POSX, y=LABEL_MOTION_TIP_POSY)
		self.optionmenu_motion_tip.place(x=OPTIONMENU_MOTION_TIP_POSX, y=OPTIONMENU_MOTION_TIP_POSY)
		# Place the add label and button
		self.label_motion_add.place(x=LABEL_MOTION_ADD_POSX, y=LABEL_MOTION_ADD_POSY)
		self.button_motion_add.place(x=BUTTON_MOTION_ADD_POSX, y=BUTTON_MOTION_ADD_POSY)

	def create_pipettor_ui(self) -> None:
		"""Creates the UI for the pipettor portion of the BuildProtocol view
		"""
		# Create the pipettor label
		self.label_pipettor = ctk.CTkLabel(master=self, text='Pipettor', font=("Roboto Medium", -16))
		# Create the volume label and entry
		self.label_pipettor_volume = ctk.CTkLabel(master=self, text='Volume (uL)', font=("Roboto Medium", -14))
		self.pipettor_volume_sv = StringVar()
		self.pipettor_volume_sv.set('')
		self.entry_pipettor_volume = ctk.CTkEntry(
			master=self,
			textvariable=self.pipettor_volume_sv, 
			width=ENTRY_PIPETTOR_VOLUME_WIDTH
		)
		# Create the tip label and optionmenu
		self.label_pipettor_tip = ctk.CTkLabel(master=self, text="Tip (uL)", font=("Roboto Medium", -14))
		self.pipettor_tip_sv = StringVar()
		self.pipettor_tip_sv.set('')
		self.optionmenu_pipettor_tip = ctk.CTkOptionMenu(
			master=self,
			variable=self.pipettor_tip_sv,
			values=('1000', '50', '200',),
			width=OPTIONMENU_PIPETTOR_TIP_WIDTH
		)
		# Create the action label and optionmenu
		self.label_pipettor_action = ctk.CTkLabel(master=self, text='Action', font=("Roboto Medium", -14))
		self.pipettor_action_sv = StringVar()
		self.pipettor_action_sv.set('Aspirate')
		self.optionmenu_pipettor_action = ctk.CTkOptionMenu(
			master=self,
			variable=self.pipettor_action_sv,
			values=('Aspirate', 'Dispense', 'Mix'),
			width=OPTIONMENU_PIPETTOR_ACTION_WIDTH
		)
		# Create the pressure label and optionmenu
		self.label_pipettor_pressure = ctk.CTkLabel(master=self, text='Pressure', font=("Roboto Medium", -14))
		self.pipettor_pressure_sv = StringVar()
		self.pipettor_pressure_sv.set('High')
		self.optionmenu_pipettor_pressure = ctk.CTkOptionMenu(
                        master=self,
			variable=self.pipettor_pressure_sv,
			values=('High', 'Low',),
			width=OPTIONMENU_PIPETTOR_PRESSURE_WIDTH
		)
		# Create the add label and button
		self.label_pipettor_add = ctk.CTkLabel(master=self, text='Add', font=("Roboto Medium", -14))
		self.button_pipettor_add = ctk.CTkButton(
			master=self,
			text='',
			#image=self.photoimage_check,
			fg_color=BUTTON_ADD_COLOR,
			width=BUTTON_PIPETTOR_ADD_WIDTH
		)

	def place_pipettor_ui(self) -> None:
		"""Places the UI for the pipettor portion of the BuildProtocol view
		"""
		# Place the pipettor label
		self.label_pipettor.place(x=LABEL_PIPETTOR_POSX, y=LABEL_PIPETTOR_POSY)
		# Place the volume label and entry
		self.label_pipettor_volume.place(x=LABEL_PIPETTOR_VOLUME_POSX, y=LABEL_PIPETTOR_VOLUME_POSY)
		self.entry_pipettor_volume.place(x=ENTRY_PIPETTOR_VOLUME_POSX, y=ENTRY_PIPETTOR_VOLUME_POSY)
		# Place the tip label and optionmenu
		self.label_pipettor_tip.place(x=LABEL_PIPETTOR_TIP_POSX, y=LABEL_PIPETTOR_TIP_POSY)
		self.optionmenu_pipettor_tip.place(x=OPTIONMENU_PIPETTOR_TIP_POSX, y=OPTIONMENU_PIPETTOR_TIP_POSY)
		# Place the action label and optionmenu
		self.label_pipettor_action.place(x=LABEL_PIPETTOR_ACTION_POSX, y=LABEL_PIPETTOR_ACTION_POSY)
		self.optionmenu_pipettor_action.place(x=OPTIONMENU_PIPETTOR_ACTION_POSX, y=OPTIONMENU_PIPETTOR_ACTION_POSY)
		# Place the pressure label and optionmenu
		self.label_pipettor_pressure.place(x=LABEL_PIPETTOR_PRESSURE_POSX, y=LABEL_PIPETTOR_PRESSURE_POSY)
		self.optionmenu_pipettor_pressure.place(x=OPTIONMENU_PIPETTOR_PRESSURE_POSX, y=OPTIONMENU_PIPETTOR_PRESSURE_POSY)
		# Place the add label and button
		self.label_pipettor_add.place(x=LABEL_PIPETTOR_ADD_POSX, y=LABEL_PIPETTOR_ADD_POSY)
		self.button_pipettor_add.place(x=BUTTON_PIPETTOR_ADD_POSX, y=BUTTON_PIPETTOR_ADD_POSY)

	def create_time_ui(self) -> None:
		"""Creates the UI for the time portion of the Build Protocol Frame view
		"""
		# Create the time label
		self.label_time = ctk.CTkLabel(master=self, text='Time', font=("Roboto Medium", -16))
		# Create the delay label and entry
		self.label_time_delay = ctk.CTkLabel(master=self, text='Delay', font=("Roboto Medium", -14))
		self.time_delay_sv = StringVar()
		self.time_delay_sv.set('')
		self.entry_time_delay = ctk.CTkEntry(
			master=self,
			textvariable=self.time_delay_sv, 
			width=ENTRY_TIME_DELAY_WIDTH
		)
		# Create the units label and optionmenu
		self.label_time_units = ctk.CTkLabel(master=self, text='Units', font=("Roboto Medium", -14))
		self.time_units_sv = StringVar()
		self.time_units_sv.set('seconds')
		self.optionmenu_time_units = ctk.CTkOptionMenu(
			master=self,
			variable=self.time_units_sv,
			values=('seconds', 'minutes'),
			width=OPTIONMENU_TIME_UNITS_WIDTH
		)
		# Create the add label and button
		self.label_time_add = ctk.CTkLabel(master=self, text='Add', font=("Roboto Medium", -14))
		self.button_time_add = ctk.CTkButton(
			master=self,
			text='',
			fg_color=BUTTON_ADD_COLOR,
			width=BUTTON_TIME_ADD_WIDTH
		)

	def place_time_ui(self) -> None:
		"""Places the UI for the time portion of the Build Protocol Frame view
		"""
		# Place the time label
		self.label_time.place(x=LABEL_TIME_POSX, y=LABEL_TIME_POSY)
		# Place the delay label and entry
		self.label_time_delay.place(x=LABEL_TIME_DELAY_POSX, y=LABEL_TIME_DELAY_POSY)
		self.entry_time_delay.place(x=ENTRY_TIME_DELAY_POSX, y=ENTRY_TIME_DELAY_POSY)
		# Place the units label and optionmenu
		self.label_time_units.place(x=LABEL_TIME_UNITS_POSX, y=LABEL_TIME_UNITS_POSY)
		self.optionmenu_time_units.place(x=OPTIONMENU_TIME_UNITS_POSX, y=OPTIONMENU_TIME_UNITS_POSY)
		# Place the add label and button
		self.label_time_add.place(x=LABEL_TIME_ADD_POSX, y=LABEL_TIME_ADD_POSY)
		self.button_time_add.place(x=BUTTON_TIME_ADD_POSX, y=BUTTON_TIME_ADD_POSY)

	def create_other_ui(self) -> None:
		"""Create the UI for the other portion of the Build Protocol Frame view
		"""
		# Create the other label
		self.label_other = ctk.CTkLabel(master=self, text='Other', font=("Roboto Medium", -16))
		# Create the option label and optionmenu
		self.label_other_option = ctk.CTkLabel(master=self, text='Option', font=("Roboto Medium", -14))
		self.other_option_sv = StringVar()
		self.other_option_sv.set("Home Pipettor")
		self.optionmenu_other_option = ctk.CTkOptionMenu(
			master=self,
			variable=self.other_option_sv,
			values=OTHER_OPTION_VALUES,
			width=OPTIONMENU_OTHER_OPTION_WIDTH
		)
		# Create the add label and button
		self.label_other_add = ctk.CTkLabel(master=self, text='Add', font=("Roboto Medium", -14))
		self.button_other_add = ctk.CTkButton(
			master=self,
			text='',
			fg_color=BUTTON_ADD_COLOR,
			width=BUTTON_OTHER_ADD_WIDTH
		)

	def place_other_ui(self) -> None:
		"""Place the UI for the other portion of the Build Protocol Frame view
		"""
		# Place the other label
		self.label_other.place(x=LABEL_OTHER_POSX, y=LABEL_OTHER_POSY)
		# Place the option label and optionmenu
		self.label_other_option.place(x=LABEL_OTHER_OPTION_POSX, y=LABEL_OTHER_OPTION_POSY)
		self.optionmenu_other_option.place(x=OPTIONMENU_OTHER_OPTION_POSX, y=OPTIONMENU_OTHER_OPTION_POSY)
		# Place the add label and button
		self.label_other_add.place(x=LABEL_OTHER_ADD_POSX, y=LABEL_OTHER_ADD_POSY)
		self.button_other_add.place(x=BUTTON_OTHER_ADD_POSX, y=BUTTON_OTHER_ADD_POSY)

	def create_treeview_ui(self) -> None:
		"""Create the UI for the actions treeview
		"""
		# Create the scrollbar
		self.scrollbar = tk.Scrollbar(self, orient='horizontal')
		# Create the treeview and link with the scrollbar
		self.treeview = tk.ttk.Treeview(
			self,
			columns=('Action'),
			show='headings',
			xscrollcommand=self.scrollbar.set
		)	
		self.scrollbar.config(command=self.treeview.xview)
		# Setup the treeview
		self.treeview.column('Action', width=TREEVIEW_COLUMN_WIDTH, stretch=False)
		self.treeview.heading('Action', text='Action')
		# Add copy and paste functionality to the treeview

	def place_treeview_ui(self) -> None:
		"""Place the UI for the actions treeview
		"""
		# Place the treeview and scrollbar
		self.treeview.place(x=TREEVIEW_POSX, y=TREEVIEW_POSY, width=TREEVIEW_WIDTH, height=TREEVIEW_HEIGHT)
		self.scrollbar.place(x=SCROLLBAR_POSX, y=SCROLLBAR_POSY, width=SCROLLBAR_WIDTH)

	def callback_tips_tray(self, *args) -> None:
		"""Deals with what happens if the Tips Tray changes
		"""
		# Get the tray
		tray = self.tips_tray_sv.get()
		column = self.tips_column_sv.get()
		# Change the Column optionmenu values based on the tray choice
		if tray in ['A', 'B', 'C', 'D']:
			if column == '':
				self.tips_action_sv.set('')
				self.optionmenu_tips_action.configure(values=('',))
				self.optionmenu_tips_column.configure(values=('1','2','3','4','5','6','7','8','9','10','11','12'))
			else:
				# Make sure the current action is valid
				if self.tips_action_sv.get() not in ['Pickup', 'Eject']:
					self.tips_action_sv.set('Eject')
				self.optionmenu_tips_column.configure(values=('1','2','3','4','5','6','7','8','9','10','11','12'))
				self.optionmenu_tips_action.configure(values=('Pickup','Eject',))
		elif tray == "Tip Transfer Tray":
			self.optionmenu_tips_column.configure(values=('1','2','3','4','5','6','7','8',''))
			if column == '':
				self.tips_action_sv.set('Tip-Press')
				self.optionmenu_tips_action.configure(values=('Tip-Press',))
			else:
				# Make sure the current action is valid
				if self.tips_action_sv.get() not in ['Pickup', 'Eject']:
					self.tips_action_sv.set('Eject')
				self.optionmenu_tips_action.configure(values=('Pickup','Eject',))
		else:
			self.tips_column_sv.set('')
			self.optionmenu_tips_column.configure(values=(''))
			self.tips_action_sv.set('Eject')
			self.optionmenu_tips_action.configure(values=('Eject',))

	def callback_tips_column(self, *args) -> None:
		"""Deals with what happens if the Tips Column changes
		"""
		# Get the tray and column
		tray = self.tips_tray_sv.get()
		column = self.tips_column_sv.get()
		# Check if Tip Transfer Tray is selected and if no column is selected
		if column == '':
			if tray == "Tip Transfer Tray":
				# Add the tip press action
				self.tips_action_sv.set('Tip-Press')
				self.optionmenu_tips_action.configure(values=('Tip-Press',))
			else:
				self.tips_action_sv.set('')
				self.optionmenu_tips_action.configure(values=('',))
		else:
			# Make sure the current action is valid
			if self.tips_action_sv.get() not in ['Pickup', 'Eject']:
				self.tips_action_sv.set('Pickup')
			self.optionmenu_tips_action.configure(values=('Pickup','Eject',))
			
	def callback_motion_consumable(self, *args) -> None:
		"""Deals with changes to the motion consumable optionmenu
		"""
		# Get the consumable, tray, column, and tip
		consumable = self.motion_consumable_sv.get()
		tray = self.motion_tray_sv.get()
		column = self.motion_column_sv.get()
		tip = self.motion_tip_sv.get()
		# Reset the tray and column optionmenus to default
		self.motion_tray_sv.set('')
		self.motion_column_sv.set('')
		# Check the consumable cases to update the trays, columns, and tips
		if consumable in NO_TRAY_CONSUMABLES:
			# No tray option
			self.motion_tray_sv.set('')
			self.optionmenu_motion_tray.configure(values=('',))
			# Set the column options
			if consumable in TWELVE_COLUMN_CONSUMABLES:
				self.optionmenu_motion_column.configure(values=('1','2','3','4','5','6','7','8','9','10','11','12',))
			elif consumable in EIGHT_COLUMN_CONSUMABLES:
				self.optionmenu_motion_column.configure(values=('1','2','3','4','5','6','7','8',))
			elif consumable in FOUR_COLUMN_CONSUMABLES:
				self.optionmenu_motion_column.configure(values=('1','2','3','4',))
			else:
				self.optionmenu_motion_column.configure(values=('',))
		else:
			# Allow for tray options
			self.optionmenu_motion_tray.configure(values=('A', 'B', 'C', 'D',))
			# Set the column options
			if consumable in NO_COLUMN_CONSUMABLES:
				self.optionmenu_motion_column.configure(values=('1',))
			else:
				self.optionmenu_motion_column.configure(values=('1','2','3','4','5','6','7','8','9','10','11','12',))
		# Allow tip options
		self.optionmenu_motion_tip.configure(values=('1000', '50', '200',))

	def callback_motion_tray(self, *args) -> None:
		"""Deals with the tray option changing
		"""
		# Get the consumable, tray, column, and tip
		consumable = self.motion_consumable_sv.get()
		tray = self.motion_tray_sv.get()
		column = self.motion_column_sv.get()
		tip = self.motion_tip_sv.get()

	def bind_button_tips_add(self, c):
		try:
			self.button_tips_add.bind('<Button-1>', c)
		except:
			pass

	def bind_button_motion_add(self, callback: Callable[[tk.Event], None]) -> None:
		try:
			self.button_motion_add.bind('<Button-1>', callback)
		except:
			pass

	def bind_button_pipettor_add(self, callback: Callable[[tk.Event], None]) -> None:
		try:
			self.button_pipettor_add.bind('<Button-1>', callback)
		except:
			pass

	def bind_button_time_add(self, callback: Callable[[tk.Event], None]) -> None:
		try:
			self.button_time_add.bind('<Button-1>', callback)
		except:
			pass
	
	def bind_button_other_add(self, callback: Callable[[tk.Event], None]) -> None:
                try:
                        self.button_other_add.bind('<Button-1>', callback)
                except:
                        pass

	def update_treeview(self) -> None:
		"""Update the treeview based on the build protocol model
		"""
		# Cleanout the treeview
		#self.treeview(*self.treeview.get_children())
		for i in self.treeview.get_children():
			self.treeview.delete(i)
		# Add the actions back to the treeview
		n_actions = len(self.model.select())
		for i in range(n_actions):
			action = self.model.actions[i][0]
			self.treeview.insert('', 'end', iid=i, values=(action,))
		self.model.actions
