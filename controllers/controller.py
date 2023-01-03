"""
System which passes data from the GUI to the model
"""
from models.model import Model
from views.view import View

from controllers.build_protocol_controller import BuildProtocolController

class Controller:
	def __init__(self, model: Model, view: View) -> None:
		self.model = model
		self.view = view
		self.build_protocol_controller = BuildProtocolController(
			model=self.model.get_build_protocol_model(),
			view=self.view.menu_frame.build_protocol_frame
		)

	def run(self) -> None:
		self.view.mainloop()
