"""
Model represents the data for the GUI
"""
import sqlite3

from models.thermocycle_model import ThermocycleModel
from models.build_protocol_model import BuildProtocolModel

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

	def get_build_protocol_model(self) -> BuildProtocolModel:
		self.build_protocol_model = BuildProtocolModel()
		return self.build_protocol_model
