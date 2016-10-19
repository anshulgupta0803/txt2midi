from pitch import Pitch

PASS='-'
LOW='.'
HIGH='\''

class Parser():
	"""docstring for Parser."""
	def __init__(self):
		self.file = None

	def open(self, fname):
		self.file = open(fname, "r")

	def close(self):
		self.file.close()

	def parse(self):
		notes = list()
		pitch = Pitch()
		symbols = self.file.read().split()
		for symbol in symbols:
			try:
				offset = 0
				length = len(symbol)
				if length > 1:
					note = symbol[0]
					offset = length - 1
					if symbol[1] == LOW:
						offset = -1 * offset
				else:
					if symbol == PASS:
						notes.append(0)
						continue
					else:
						note = symbol

				notes.append(pitch.getPitch(note, offset))
			except Exception as e:
				print("[ERROR] Syntax Error", e)
				exit()
		return notes
