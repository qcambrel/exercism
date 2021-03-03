class SpaceAge:
	def __init__(self, seconds):
		self.seconds = seconds
		self.earth_year = 31557600
		self.orbital_periods = {
			'Mercury': 0.2408467 * self.earth_year,
			'Venus': 0.61519726 * self.earth_year,
			'Mars': 1.8808158 * self.earth_year,
			'Jupiter': 11.862615 * self.earth_year,
			'Saturn': 29.447498 * self.earth_year,
			'Uranus': 84.016846 * self.earth_year,
			'Neptune': 164.79132 * self.earth_year
		}

	def on_earth(self):
		return round(self.seconds / self.earth_year, 2)

	def on_venus(self):
		return round(self.seconds / self.orbital_periods['Venus'], 2)

	def on_mercury(self):
		return round(self.seconds	/ self.orbital_periods['Mercury'], 2)

	def on_mars(self):
		return round(self.seconds / self.orbital_periods['Mars'], 2)

	def on_jupiter(self):
		return round(self.seconds / self.orbital_periods['Jupiter'], 2)

	def on_saturn(self):
		return round(self.seconds / self.orbital_periods['Saturn'], 2)

	def on_neptune(self):
		return round(self.seconds / self.orbital_periods['Neptune'], 2)

	def on_uranus(self):
		return round(self.seconds / self.orbital_periods['Uranus'], 2)