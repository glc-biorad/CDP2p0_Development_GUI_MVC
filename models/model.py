"""
Model represents the data for the GUI
"""
import sqlite3

class Model:
	def __init__(self) -> None:
		self.connection = sqlite3.connect('cdp2p0_gui.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute("create table if not exists main (title text)")
