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
		print('HERE in controller')
		# Get the action data
		tray = self.view.tips_tray_sv.get()
		column = self.view.tips_column_sv.get()
		action = self.view.tips_action_sv.get()
		# Determine which if any row of the treeview is selected
		selected_row = self.view.treeview.selection()[0]
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
		print(action_message)
		# Inset action into the action list
		self.model.insert(len(self.model.actions), action_message)
		# Update the view
		self.view.update_treeview()
