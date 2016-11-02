#!/usr/bin/python3.5

from uiwrapper import *
from midiutil.MidiFile import MIDIFile
from track import Track
from instruments import *
from json import load
from jsonschema import validate

def convert(ui):
	with open(ui.getSrcFullFileName()) as dataFile:
		data = load(dataFile)

	with open('schema.json') as schemaFile:
		schema = load(schemaFile)

	try:
		validate(data, schema)
	except Exception as e:
		ui.setErrorMsg(str(e))
		return

	# Create the MIDIFile Object with number of tracks
	tracks = len(data["tracks"])
	MIDI = MIDIFile(numTracks=tracks)

	compositionName = ui.getTrackName()

	for i in range(tracks):
		try:
			volume = data["tracks"][i]["volume"]
		except Exception as e:
			volume = 127

		try:
			tempo = data["tracks"][i]["tempo"]
		except Exception as e:
			tempo = 240

		# Initialize the track
		track = i
		channel = i
		duration = 1
		time = 0

		track = Track(track, channel, volume, duration, tempo)
		MIDI.addTrackName(track.id, time, data["tracks"][i]["instrument"])
		MIDI.addProgramChange(track.id, track.channel, time, instruments[data["tracks"][i]["instrument"]])

		try:
			track.parse(data["tracks"][i]["notes"])
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
