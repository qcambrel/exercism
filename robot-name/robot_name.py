import string
import random


class Robot:

	robot_names = set()
	unavailable_names = set()

	def __init__(self):
		if not self.robot_names:
			self.batch_names()
		self.reset()

	def generate_name(self):
		robot_name = ''
		for i in range(2):
			robot_name += random.choice(string.ascii_uppercase)
		for i in range(3):
			robot_name += random.choice(string.digits)
		if robot_name in self.unavailable_names:
			self.generate_name()
		return robot_name

	def batch_names(self):
		for i in range(1000):
			self.robot_names.add(self.generate_name())

	def reset(self):
		self.name = random.choice(list(self.robot_names))
		self.robot_names.remove(self.name)
		self.unavailable_names.add(self.name)
		