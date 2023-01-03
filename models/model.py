"""
Model represents the data for the GUI
"""
import sqlite3

from models.thermocycle_model import ThermocycleModel

DB_NAME = 'cdp2p0_gui.db'

class Model:
	# Models
	thermocycle_model: ThermocycleModel = None

	def __init__(self) -> None:
		self.connection = sqlite3.connect(DB_NAME)
		self.cursor = self.connection.cursor()


	def get_thermocycle_model(self) -> ThermocycleModel:
		self.thermocycle_model = ThermocycleModel(DB_NAME, self.cursor, self.connection)
		return self.thermocycle_model
