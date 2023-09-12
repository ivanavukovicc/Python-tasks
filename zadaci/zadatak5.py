import random

class Candyman:

	def __init__(self):
		self.candy_sticks = []
		self.total_count = 0
		self.total_size = 0
		self.red_count = 0

	def add_candy(self, size, is_red):
		self.candy_sticks.append((size, is_red))
		self.total_count += 1
		self.total_size += size
		if is_red:
			self.red_count += 1

	def get_a_random_candy(self):
		if not self.candy_sticks:
			return None
		return random.choice(self.candy_sticks)

	def get_average_size(self):
		if self.total_count == 0
			return 0
		return self.total_size / self.total_count

	def get_red_candy_chance(self):
		if self.total_count == 0:
			return 0
		return self.red_count / self.total_count
