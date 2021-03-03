import random
import math

class Character:
	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()
		self.hitpoints = 10 + modifier(self.constitution)

	def ability(self):
		rolls = [random.randint(1, 6) for i in range(4)]
		rolls.remove(min(rolls))
		return sum(rolls)


def modifier(constitution):
	return math.floor((constitution - 10) / 2)