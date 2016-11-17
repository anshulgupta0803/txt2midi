from txt2midi.pitch import Pitch
from re import search as reSearch

PASS='-'
LOW='.'
HIGH='\''
LONG='~'

class Parser():
	"""docstring for Parser."""
	def __init__(self, baseOffset="S"):
		length = len(baseOffset)
		note = baseOffset[0]
		offset = 0
		if length > 1:
			if baseOffset[1] == LOW:
				offset = -1 * (length - 1)
			elif baseOffset[1] == HIGH:
				offset = (length - 1)
		pitch = Pitch()
		self.baseOffset = pitch.getPitch(note, offset) - pitch.getPitch("S", 0)

	def parse(self, symbols):
		notes = list()
		tempoFactors = list()
		pitch = Pitch()
		symbols = symbols.split()
		for symbol in symbols:
			try:
				regex="^[SrRgGmMPdDnN](?:\\.*|'*)~*$|^\((?:[SrRgGmMPdDnN](?:\\.*|'*))+\)$|^-$"
				if reSearch(regex, symbol) == None:
					raise ValueError("Syntax Error: " + symbol)
					return

				length = len(symbol)
				note = symbol[0]

				if reSearch("^\((?:[SrRgGmMPdDnN](?:\\.*|'*))+\)$", symbol) != None:
					tempoFactor = 0
					for i in range(1, length - 1):
						if reSearch("[SrRgGmMPdDnN]", symbol[i]) != None:
							tempoFactor += 1

					currentSymbol = symbol[1]
					for i in range(2, length):
						if reSearch("[SrRgGmMPdDnN]", symbol[i]) != None or symbol[i] == ')':
							offset = self.getOffset(currentSymbol)
							try:
								val = pitch.getPitch(currentSymbol[0], offset) + self.baseOffset
							except Exception as e:
								raise ValueError("Syntax Error: " + str(e))
								return

							notes.append(val)
							tempoFactors.append(2 / tempoFactor)
							currentSymbol = symbol[i]
						else:
							currentSymbol += symbol[i]

					continue

				offset = self.getOffset(symbol)

				tempoFactor = 1
				tempoPattern = reSearch("~+", symbol)
				if tempoPattern != None:
					tempoFactor = tempoPattern.span()[1] - tempoPattern.span()[0] + 1

				if symbol == PASS:
					tempoFactors.append(tempoFactor)
					notes.append(0)
					continue

				try:
					val = pitch.getPitch(note, offset) + self.baseOffset
				except Exception as e:
					raise ValueError("Syntax Error: " + symbol)
					return

				notes.append(val)
				tempoFactors.append(tempoFactor)
			except Exception as e:
				raise ValueError("Syntax Error: " + str(e))
				return

		return notes, tempoFactors

	def getOffset(self, symbol):
		offset = 0
		# reSearch object's span() function returns the start and end position of the pattern
		offsetPattern = reSearch("\\.+", symbol)
		if offsetPattern != None:
			# offset is negative for Low
			offset = offsetPattern.span()[0] - offsetPattern.span()[1]

		offsetPattern = reSearch("'+", symbol)
		if offsetPattern != None:
			# offset is positive for High
			offset = offsetPattern.span()[1] - offsetPattern.span()[0]

		return offset
