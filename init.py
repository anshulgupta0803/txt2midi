#!/usr/bin/python3.5

#Import the library
from midiutil.MidiFile import MIDIFile
from parse import Parser
import sys

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0
time = 0

MyMIDI.addTrackName(track, time, "Raag Bhoopali")
MyMIDI.addTempo(track, time, 240)

# Creates parser and parses the input file
parser = Parser()
parser.open(sys.argv[1])
parsedData = parser.parse()
parser.close()

track = 0
channel = 0
volume = 100
time = 0
duration = 1

for pitch in parsedData:
	MyMIDI.addNote(track, channel, pitch, time, duration, volume)
	time += 1

binfile = open("bhoopali.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
