from tkinter import StringVar

# Import the model and view for this controller
from models.build_protocol_model import BuildProtocolModel
from views.build_protocol_frame import BuildProtocolFrame

class BuildProtocolController:
	"""System for passing data from the Build Protocol Frame view to the Build Protocol Model
	"""
	def __init__(
			self, 
			model: BuildProtocolModel,
			view: BuildProtocolFrame
		) -> None:
		# Set the model and view for the controller
		self.model = model
		self.view = view

	def setup_bindings(self):
		# Set bindings between the view and the controller
		self.view.bind_button_tips_add(self.add_tips_action)
		self.view.bind_button_motion_add(self.add_motion_action)

	def insert(self, ID: int, action_message: str) -> None:
		"""Insert the action message into the action list of the model in the correct order
		
		Parameters
		----------
		ID : int
			Key used to insert data in the correct order
		action_message : str
			Action to be inserted into the model
		"""
		self.model.insert(ID, action_message)

	def add_tips_action(self, event=None) -> None:
		# Get the action data
		tray = self.view.tips_tray_sv.get()
		column = self.view.tips_column_sv.get()
		action = self.view.tips_action_sv.get()
		# Determine which if any row of the treeview is selected
		try:
			selected_row = self.view.treeview.selection()[0]
		except:
			pass
		# Make sure there is an action
		if action == '':
			print(f"Tip action must be specified")
			return None
		# Check the action treeview to make sure you are allowed to add this action
		# Generate the action message
		action_message = ''
		if tray == '':
			action_message = f"{action} tips"
		else:
			if action == 'Eject':
				action_message = f"{action} tips in {tray} column {column}"
			elif action == 'Pickup':
				action_message = f"{action} tips from {tray} column {column}"
			else:
				action_message = f"{action} tips on the {tray}"
		# Inset action into the action list
		self.model.insert(len(self.model.actions), action_message)
		# Update the view
		self.view.update_treeview()

	def add_motion_action(self, event=None) -> None:
		"""Deals with adding a motion action to the model from the view
		"""
		# Get the action data
		consumable = self.view.motion_consumable_sv.get()
		tray = self.view.motion_tray_sv.get()
		column = self.view.motion_column_sv.get()
		tip = self.view.motion_tip_sv.get()
		# Determine which if any row of the treeview is selected
		try:
			selected_row = self.view.treeview.selection()[0]
		except:
			pass
		# Make sure consumable is not missing
		if consumable != '':
			# Generate the action message
			action_message = f"Move to {consumable}"
			if tray != '':
				action_message = action_message + f" tray {tray}"
			else:
				# Make sure this is ok
				if consumable not in NO_TRAY_CONSUMABLES:
					print(f"Motion consumable ({consumable}) needs a tray")
					return None
			if column != '':
				action_message = action_message + f" column {column}"
			else:
				# Make sure this is ok
				if consumable not in NO_COLUMN_CONSUMABLES:
					print(f"Motion consumable ({consumable}) needs a column")
					return None
			if tip != '':
				action_message = action_message + f" with {tip} uL tips"
			else:
				action_message = action_message + " without tips"
		else:
			print("Motion Consumable Option was not selected")
			return None
		# Inset action into the action list
		self.model.insert(len(self.model.actions), action_message)
		# Update the view
		self.view.update_treeview()
