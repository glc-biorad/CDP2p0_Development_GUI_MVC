"""
System which passes data from the GUI to the model
"""
from models.model import Model
from views.view import View

class Controller:
	def __init__(self, model: Model, view: View) -> None:
		self.model = model
		self.view = view

	def run(self) -> None:
		self.view.mainloop()
