#!/usr/bin/python3.5

from midiutil.MidiFile import MIDIFile
from track import Track
import sys

compositionName = input("Name of the song: ")
# tracks = input("Number of tracks [1]: ")
tracks = len(sys.argv) - 1

# Set default tracks
if tracks == "":
	tracks = 1
try:
	tracks = int(tracks)
except Exception as e:
	print("[ERROR] Number of tracks must be an integer")
	exit()

# Create the MIDIFile Object with number of tracks
MIDI = MIDIFile(tracks)

for i in range(tracks):
	channel = 0
	volume = 127
	duration = 1
	tempo = input("Tempo for Track " + str(i) + " [240]: ")
	# Set default tempo
	if tempo == "":
		tempo = 240
	try:
		tempo = int(tempo)
	except Exception as e:
		print("[ERROR] Tempo must be an integer")
		exit()

	# Initialize the track
	channel = 0
	volume = 127
	duration = 1
	track = Track(i, channel, volume, duration, tempo)
	MIDI.addTrackName(track.id, 0, compositionName)
	track.parse(sys.argv[i + 1])

	# Add all the nodes to the track
	length = len(track.note)
	for time in range(length):
		MIDI.addTempo(track.id, time, track.tempo / track.tempoFactor[time])
		MIDI.addNote(track.id, track.channel, track.note[time], time, track.duration, track.volume)

# Write MIDI output to file
outfile = open(compositionName + ".mid", 'wb')
MIDI.writeFile(outfile)
outfile.close()
