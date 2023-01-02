import tkinter as tk

class ThermocycleController:
	"""
	System for passing data from the Thermocycle View to the Thermocycle Model
	"""
	def __init__(self, model, view) -> None:
		self.model = model
		self.view = view

	def get_thermocycler_sv(self, id: int) -> tk.StringVar:
		return self.model.thermocycler_sv

	def get_cycles_sv(self, id: int) -> tk.StringVar:
		return self.model.cycles_sv

	def get_use_a_iv(self, id: int) -> tk.IntVar:
		return self.model.use_a_iv

	def get_use_b_iv(self, id: int) -> tk.IntVar:
		return self.model.use_b_iv

	def get_use_c_iv(self, id: int) -> tk.IntVar:
		return self.model.use_c_iv

	def get_use_d_iv(self, id: int) -> tk.IntVar:
		return self.model.use_d_iv

	def get_first_denature_temp_sv(self, id: int) -> tk.StringVar:
		return self.model.first_denature_temp_sv

	def get_anneal_temp_sv(self, id: int) -> tk.StringVar:
		return self.model.anneal_temp_sv

	def get_second_denature_temp_sv(self, id: int) -> tk.StringVar:
		return self.model.second_denature_temp_sv

	def get_first_denature_time_sv(self, id: int) -> tk.StringVar:
		return self.model.first_denature_time_sv

	def get_anneal_time_sv(self, id: int) -> tk.StringVar:
		return self.model.anneal_time_sv

	def get_second_denature_time_sv(self, id: int) -> tk.StringVar:
		return self.model.second_denature_time_sv

