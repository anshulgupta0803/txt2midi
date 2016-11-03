#!/usr/bin/python3.5

from uiwrapper import *
from midiutil.MidiFile import MIDIFile
from track import Track
from instruments import *
from json import load
from jsonschema import validate
from os import system

def convert(ui):
	with open(ui.getSrcFullFileName()) as dataFile:
		data = load(dataFile)

	with open('schema.json') as schemaFile:
		schema = load(schemaFile)

	try:
		validate(data, schema)
	except Exception as e:
		ui.setErrorMsg(str(e).split("\n")[0])
		return

	# Create the MIDIFile Object with number of tracks
	tracks = len(data["tracks"])
	MIDI = MIDIFile(numTracks=tracks)

	compositionName = ui.getTrackName()

	for i in range(tracks):
		try:
			instrument = data["tracks"][i]["instrument"]
		except Exception as e:
			instrument = "Acoustic Grand Piano"

		try:
			volume = data["tracks"][i]["volume"]
		except Exception as e:
			volume = 127

		try:
			tempo = data["tempo"]
		except Exception as e:
			tempo = 240

		try:
			baseOffset = data["tracks"][i]["baseOffset"]
		except Exception as e:
			baseOffset = "S"

		try:
			loop = data["tracks"][i]["loop"]
		except Exception as e:
			loop = 1

		# Initialize the track
		track = i
		channel = i
		duration = 1
		time = 0

		track = Track(track, channel, volume, duration, tempo)
		MIDI.addTrackName(track.id, time, instrument)
		MIDI.addProgramChange(track.id, track.channel, time, instruments[instrument])

		try:
			track.parse(data["tracks"][i]["notes"], baseOffset)
		except ValueError as e:
			ui.setErrorMsg(str(e))
			return None

		# Add all the nodes to the track
		time = 0
		length = len(track.note)
		for times in range(loop):
			for currentBeat in range(length):
				MIDI.addTempo(track.id, time, track.tempo / track.tempoFactor[currentBeat])
				MIDI.addNote(track.id, track.channel, track.note[currentBeat], time, track.duration, track.volume)
				time += 1

	# Write MIDI output to file
	outfile = open(ui.getOutputFolder() + compositionName + ".mid", 'wb')
	MIDI.writeFile(outfile)
	outfile.close()
	#converting .mid to wav file
	#converMidToWav(compositionName);
	#deleting mid file
	#delFile(compositionName+".mid")
	ui.setSucessMsg("File Successfully Converted")
	return compositionName + ".mid"

def converMidToWav(mid_filename):
	system("timidity -Ow -o " + mid_filename + ".wav " + mid_filename + ".mid")

def delFile(filename):
	system("rm " + filename)

if __name__ == '__main__':
	ui=UiWrapper();
	ui.renderUI();
	ui.bindConvertOnClick(lambda:convert(ui));
	ui.showUI();
