from typing import Any, Callable
from tkinter import StringVar
import customtkinter as ctk

# Import the BuildProtocolModel

# Constants
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

	def create_ui(self) -> None:
		"""Create the UI for the BuildProtocolFrame
		"""
		# Place the build protocol frame
		self.place(x=self.posx, y=self.posy)
		# Place the Tips Section
		self.create_tips_ui()
		# Place the Motion Section
		self.create_motion_ui()
		# Place the Pipettor Section
		# Place the Time Section
		# Place the Other Section
		# Place the Protocol Progress Bar
		# Place the Protocol Action Treeview
		# Place the Start Button
		# Place the Load Button
		# Place the Save Button
		# Place the Delete Button

	def create_tips_ui(self) -> None:
		"""Create the UI for the Tips portion of the frame
		"""
		# Place the tips label
		self.label_tips = ctk.CTkLabel(master=self, text='Tips', font=("Roboto Medium", -16))
		self.label_tips.place(x=LABEL_TIPS_POSX, y=LABEL_TIPS_POSY)
		# Place the tray label and optionmenu
		self.label_tips_tray = ctk.CTkLabel(master=self, text='Tray', font=("Roboto Medium", -16))
		self.label_tips_tray.place(x=LABEL_TIPS_TRAY_POSX, y=LABEL_TIPS_TRAY_POSY)
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
		self.optionmenu_tips_tray.place(x=OPTIONMENU_TIPS_TRAY_POSX, y=OPTIONMENU_TIPS_TRAY_POSY)
		# Place the column label and optionmenu
		self.label_tips_column = ctk.CTkLabel(master=self, text='Column', font=("Roboto Medium", -16))
		self.label_tips_column.place(x=LABEL_TIPS_COLUMN_POSX, y=LABEL_TIPS_COLUMN_POSY)
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
		self.optionmenu_tips_column.place(x=OPTIONMENU_TIPS_COLUMN_POSX, y=OPTIONMENU_TIPS_COLUMN_POSY)
		# Place the action label and optionmenu
		self.label_tips_action = ctk.CTkLabel(master=self, text='Action', font=("Roboto Medium", -16))
		self.label_tips_action.place(x=LABEL_TIPS_ACTION_POSX, y=LABEL_TIPS_ACTION_POSY)
		self.tips_action_sv = StringVar()
		self.tips_action_sv.set('Eject')
		self.optionmenu_tips_action = ctk.CTkOptionMenu(
			master=self,
			variable=self.tips_action_sv,
			values=('Eject',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_TIPS_ACTION_WIDTH
		)
		self.optionmenu_tips_action.place(x=OPTIONMENU_TIPS_ACTION_POSX, y=OPTIONMENU_TIPS_ACTION_POSY)
		# Place the add button

	def create_motion_ui(self) -> None:
		"""Deals with creating the UI for the Motion section of the Build Protocol Frame
		"""
		# Place the motion label
		self.label_motion = ctk.CTkLabel(master=self, text='Motion', font=("Roboto Medium", -16))
		self.label_motion.place(x=LABEL_MOTION_POSX, y=LABEL_MOTION_POSY)
		# Place the consumable label and optionmenu
		self.label_motion_consumable = ctk.CTkLabel(master=self, text='Consumable', font=("Roboto Medium", -16))
		self.label_motion_consumable.place(x=LABEL_MOTION_CONSUMABLE_POSX, y=LABEL_MOTION_CONSUMABLE_POSY)
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
		self.optionmenu_motion_comsumable.place(x=OPTIONMENU_MOTION_CONSUMABLE_POSX, y=OPTIONMENU_MOTION_CONSUMABLE_POSY)
		# Place the tray label and optionmenu
		self.label_motion_tray = ctk.CTkLabel(master=self, text='Tray', font=("Roboto Medium", -16))
		self.label_motion_tray.place(x=LABEL_MOTION_TRAY_POSX, y=LABEL_MOTION_TRAY_POSY)
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
		self.optionmenu_motion_tray.place(x=OPTIONMENU_MOTION_TRAY_POSX, y=OPTIONMENU_MOTION_TRAY_POSY)
		# Place the column label and optionmenu
		self.label_motion_column = ctk.CTkLabel(master=self, text='Column', font=("Roboto Medium", -16))
		self.label_motion_column.place(x=LABEL_MOTION_COLUMN_POSX, y=LABEL_MOTION_COLUMN_POSY)
		self.motion_column_sv = StringVar()
		self.motion_column_sv.set('')
		self.optionmenu_motion_column = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_column_sv,
			values=('',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_COLUMN_WIDTH
		)
		self.optionmenu_motion_column.place(x=OPTIONMENU_MOTION_COLUMN_POSX, y=OPTIONMENU_MOTION_COLUMN_POSY)
		# Place the tip label and optionmenu
		self.label_motion_tip = ctk.CTkLabel(master=self, text="Tip (uL)", font=("Roboto Medium", -16))
		self.label_motion_tip.place(x=LABEL_MOTION_TIP_POSX, y=LABEL_MOTION_TIP_POSY)
		self.motion_tip_sv = StringVar()
		self.motion_tip_sv.set('')
		self.optionmenu_motion_tip = ctk.CTkOptionMenu(
			master=self,
			variable=self.motion_tip_sv,
			values=('',),
			font=("Roboto Medium", -14),
			width=OPTIONMENU_MOTION_TIP_WIDTH
		)
		self.optionmenu_motion_tip.place(x=OPTIONMENU_MOTION_TIP_POSX, y=OPTIONMENU_MOTION_TIP_POSY)
		# Place the add button

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
				self.tips_action_sv.set('Eject')
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
		if consumable in ["Assay Strip", "Pre-Amp Thermocycler", "Heater/Shaker", "Mag Separator", "Chiller"]:
			# No tray option
			self.motion_tray_sv.set('')
			self.optionmenu_motion_tray.configure(values=('',))
			# Set the column options
			if consumable in ["Pre-Amp Thermocycler", "Mag Separator", "Chiller"]:
				self.optionmenu_motion_column.configure(values=('1','2','3','4','5','6','7','8','9','10','11','12',))
			elif consumable in ["Assay Strip"]:
				self.optionmenu_motion_column.configure(values=('1','2','3','4','5','6','7','8',))
			elif consumable in ["Heater/Shaker"]:
				self.optionmenu_motion_column.configure(values=('1','2','3','4',))
			else:
				self.optionmenu_motion_column.configure(values=('',))
		else:
			# Allow for tray options
			self.optionmenu_motion_tray.configure(values=('A', 'B', 'C', 'D',))
			# Set the column options
			if consumable in ["Sample Rack", "Aux Heater", "Quant Strip"]:
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
