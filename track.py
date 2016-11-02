#!/usr/bin/python3.5

from parse import Parser

class Track():
	"""docstring for Track."""
	def __init__(self, id, channel, volume, duration, tempo):
		self.id = id
		self.channel = channel
		self.volume = volume
		self.duration = duration
		self.tempo = tempo
		self.note = None
		self.tempoFactor = None

	def parse(self, symbols):
		# Creates parser and parses the input file
		parser = Parser()
		self.note, self.tempoFactor = parser.parse(symbols)
