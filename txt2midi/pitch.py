class Pitch():
	"""docstring for Pitch."""
	def __init__(self):
		self.pitch = {
			'S': 60,
			'r': 61,
			'R': 62,
			'g': 63,
			'G': 64,
			'M': 65,
			'm': 66,
			'P': 67,
			'd': 68,
			'D': 69,
			'n': 70,
			'N': 71
		}

	def getPitch(self, note, offset=0):
		return self.pitch[note] + offset * 12
