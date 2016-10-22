#!/usr/bin/python3.5

from pitch import Pitch

PASS='-'
LOW='.'
HIGH='\''
LONG='~'

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
		tempoFactors = list()
		pitch = Pitch()
		symbols = self.file.read().split()
		for symbol in symbols:
			try:
				offset = 0
				length = len(symbol)
				tempoFactor = 1
				if length > 1:
					note = symbol[0]

					for i in range(2, length):
						if symbol[i] != symbol[1]:
							raise ValueError("Syntax Error: " + symbol)

					if symbol[1] == HIGH:
						offset = length - 1
					elif symbol[1] == LOW:
						offset = -1 * (length - 1)
					elif symbol[1] == LONG:
						tempoFactor = length
					else:
						raise ValueError("Syntax Error: " + symbol)
				else:
					if symbol == PASS:
						tempoFactors.append(1)
						notes.append(0)
						continue
					else:
						note = symbol

				try:
					val = pitch.getPitch(note, offset)
				except Exception as e:
					raise ValueError("Syntax Error: " + symbol)

				notes.append(val)
				tempoFactors.append(tempoFactor)
			except Exception as e:
				raise ValueError("Syntax Error: " + symbol)
		return notes, tempoFactors
