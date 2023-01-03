from tkinter import StringVar

# Constants
DEFAULTS = {
	'tips_tray': '',
	'tips_column': '',
	'tips_action': 'Eject',
	'motion_consumable': '',
	'motion_tray': '',
	'motion_column': '',
	'motion_tip': '',
	'pipettor_volume': '',
	'pipettor_tip': '',
	'pipettor_action': 'Aspirate',
	'pipettor_pressure': 'High',
	'time_delay': '',
	'time_units': 'seconds',
	'other_option': "Home pipettor",
}

class BuildProtocolModel:
	""" Model for the Build Protocol View
	"""
	def __init__(self) -> None:
		# Initialize the optionmenu and entry variables
		self.tips_tray_sv = StringVar()
		self.tips_column_sv = StringVar()
		self.tips_action_sv = StringVar()
		self.motion_consumable_sv = StringVar()
		self.motion_tray_sv = StringVar()
		self.motion_column_sv = StringVar()
		self.motion_tip_sv = StringVar()
		self.pipettor_volume_sv = StringVar()
		self.pipettor_tip_sv = StringVar()
		self.pipettor_action_sv = StringVar()
		self.pipettor_pressure_sv = StringVar()
		self.time_delay_sv = StringVar()
		self.time_units_sv = StringVar()
		self.other_option_sv = StringVar()
		# Initialize the action list
		self.actions = []

	def setup_defaults(self) -> None:
		"""Setup the default option and entry values for the Build Protocol Frame view
		"""
		# Set the variables with their default values
		self.tips_tray_sv.set(DEFAULTS['tips_tray'])
		self.tips_column_sv.set(DEFAULTS['tips_column'])
		self.tips_action_sv.set(DEFAULTS['tips_action'])
		self.motion_consumable_sv.set(DEFAULTS['motion_consumable'])
		self.motion_tray_sv.set(DEFAULTS['motion_tray'])
		self.motion_column_sv.set(DEFAULTS['motion_column'])
		self.motion_tip_sv.set(DEFAULTS['motion_tip'])
		self.pipettor_volume_sv.set(DEFAULTS['pipettor_volume'])
		self.pipettor_tip_sv.set(DEFAULTS['pipettor_tip'])
		self.pipettor_action_sv.set(DEFAULTS['pipettor_action'])
		self.pipettor_pressure_sv.set(DEFAULTS['pipettor_pressure'])
		self.time_delay_sv.set(DEFAULTS['time_delay'])
		self.time_units_sv.set(DEFAULTS['time_units'])
		self.other_option_sv.set(DEFAULTS['other_option'])		

	def select(self, ID: int = None) -> list:
		"""Query the action list by key
		
		Parameters
		----------
		ID : int, optional
			Key value for looking up actions in the action list
		"""
		if ID == None:
			return self.actions
		return [self.actions[ID]]

	def insert(self, ID: int,  action_message: str) -> None:
		"""Query for inserting a new action

		Parameters
		----------
		ID : int
			Key to put the action at a particular index
		action_message : str
			The action message to be added to the action treeview
		"""
		self.actions = self.actions[:ID] + [action_message] + self.actions[ID:]

	def delete(self, ID: int) -> None:
		"""Query for deleting an action from the action list by id
	
		Parameters
		----------
		ID : int
			The id necessary to know which action to delete
		"""
		self.actions.pop(ID)
