#!/usr/bin/python3.5

from uiwrapper import *
from midiutil.MidiFile import MIDIFile
from track import Track
from instruments import *

def convert(ui):
	compositionName = ui.getTrackName()
	# tracks = input("Number of tracks [1]: ")
	tracks = 1#len(sys.argv) - 1

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
		tempo = "" #input("Tempo for Track " + str(i) + " [240]: ")
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
		MIDI.addProgramChange(track.id, track.channel, 0, instruments[ui.setInstrument()])

		try:
			track.parse(ui.getSrcFullFileName())
		except ValueError as e:
			ui.setErrorMsg(str(e))
			return

		# Add all the nodes to the track
		length = len(track.note)
		for time in range(length):
			MIDI.addTempo(track.id, time, track.tempo / track.tempoFactor[time])
			MIDI.addNote(track.id, track.channel, track.note[time], time, track.duration, track.volume)

	# Write MIDI output to file
	outfile = open(ui.getOutputFolder() + compositionName + ".mid", 'wb')
	MIDI.writeFile(outfile)
	outfile.close()
	ui.setSucessMsg("File Successfully Converted")

if __name__ == '__main__':
	ui=UiWrapper();
	ui.renderUI();
	ui.bindConvertOnClick(lambda:convert(ui));
	ui.showUI();
