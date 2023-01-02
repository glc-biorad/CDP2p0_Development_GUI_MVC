import sqlite3

import tkinter as tk

class ThermocycleModel:
	def __init__(self):
		self.connection = sqlite3.connect('cdp2p0_gui.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute("create table if not exists thermocycle (title text)")
		self.thermocycler_sv = tk.StringVar()
		self.thermocycler_sv.set('A')
		self.cycles_sv = tk.StringVar()
		self.cycles_sv.set('40')
		self.use_a_iv = tk.IntVar()
		self.use_a_iv.set(1)
		self.use_b_iv = tk.IntVar()
		self.use_b_iv.set(1)
		self.use_c_iv = tk.IntVar()
		self.use_c_iv.set(0)
		self.use_d_iv = tk.IntVar()
		self.use_d_iv.set(1)
		self.first_denature_temp_sv = tk.StringVar()
		self.first_denature_temp_sv.set('84')
		self.anneal_temp_sv = tk.StringVar()
		self.anneal_temp_sv.set('50')
		self.second_denature_temp_sv = tk.StringVar()
		self.second_denature_temp_sv.set('84')
		self.first_denature_time_sv = tk.StringVar()
		self.first_denature_time_sv.set('3')
		self.anneal_time_sv = tk.StringVar()
		self.anneal_time_sv.set('40')
		self.second_denature_time_sv = tk.StringVar()
		self.second_denature_time_sv.set('30')
