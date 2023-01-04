import customtkinter as ctk

from views.image_frame import ImageFrame
from views.thermocycle_frame import ThermocycleFrame
from views.build_protocol_frame import BuildProtocolFrame

# Constants
X = 10
DY = 45
BUTTON_WIDTH = 160
BUTTON_HEIGHT = 30

# Button Titles
BUTTON_TITLES = [
	'Home',
	'Image',
	'Thermocycle',
	"Build Protocol",
	'Optimize',
	'Service',
	'Status',
	'Configure',
]

class MenuFrame(ctk.CTkFrame):
	"""
	Menu Frame
	"""

	def __init__(self, master: ctk.CTk, width: int, height: int, posx: int, posy: int, right_frame_width: int, right_frame_height: int) -> None:
		self.master = master
		self.width = width
		self.height = height
		self.posx = posx
		self.posy = posy
		self.right_frame_width = right_frame_width
		self.right_frame_height = right_frame_height
		self.current_view: ctk.CTkFrame = None
		super().__init__(
			master=self.master, 
			width = self.width,
			height = self.height,
			corner_radius=0,
		)

	def create_ui(self) -> None:
		# Place the Menu Frame
		self.place(x=self.posx, y=self.posy)
		# Set the initial y value
		y = 20
		# Place the label for the GUI at the top of the menu
		self.label = ctk.CTkLabel(master=self, text="CDP 2.0", font=("Roboto Medium", -16))
		self.label.place(x=60,y=y)
		# Create and Place the buttons
		for button_title in BUTTON_TITLES:
			y = y + DY
			button = ctk.CTkButton(master=self, 
				text=button_title,
				command=lambda button_text=button_title:self.on_click(button_text)
			)
			# Place the button on the Menu Frame
			button.place(x=X, y=y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
		# Create and Place Firmware and Software Version Labels

	def on_click(self, button_title: str) -> None:
		# Make sure the button is valid
		assert button_title.title() in BUTTON_TITLES
		# Load the proper view
		if button_title == 'Home':
			print(button_title)
		elif button_title == 'Image':
			#frame = self.image_frame
			a = 1
		elif button_title == 'Thermocycle':
			frame = self.master.thermocycle_frame
			#frame = ThermocycleFrame(self.master, self.right_frame_width, self.right_frame_height, self.width, 0)
		elif button_title == "Build Protocol":
			frame = self.master.build_protocol_frame
			#frame = BuildProtocolFrame(self.master, self.right_frame_width, self.right_frame_height, self.width, 0)
		elif button_title == 'Optimize':
			print(button_title)
		elif button_title == 'Service':
			print(button_title)
		elif button_title == 'Status':
			print(button_title)
		elif button_title == 'Configure':
			print(button_title)
		# Check if the button was clicked for the same view
		if self.current_view == None:
			self.current_view = frame
			#self.current_view.create_ui()
			self.current_view.place_ui()
		elif self.current_view != frame:
			self.destroy_current_view()
			self.current_view = frame
			#self.current_view.create_ui()
			self.current_view.place_ui()

	def destroy_current_view(self) -> None:
		# Clean up the Right Frame for updating
		for widget in self.current_view.winfo_children():
			#widget.destroy()
			widget.place_forget()
