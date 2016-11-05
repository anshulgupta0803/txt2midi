Indian Musical Notations to Music
====

## Description
This tool converts **Indian Musical Notations** to MIDI music.

It takes a `.json` file as input as gives a `.mid` file as the output.

----

## Installation
This tool depends on

 - pygame
	 - Install it using

	 `sudo pip3 install pygame`
 - tkinter
	 - On debain based systems, install it using

	`sudo apt-get install python3-tk`

Install the tool using

	sudo python3 setup.py install

This will install the tool in `/usr/local/bin` and you can run it using

	txt-midi

## Input File Format
The `.json` file has 2 parameters:

 - *tempo*
 - *tracks*

### tempo
It takes a positive Integer as the argument.
Default Value is **240**. This is an optional parameter.

### tracks
It is an array. Structure of an element of the array is:
```
{
    "instrument": "Acoustic Grand Piano",
    "loop": 1,
    "volume": 127,
    "baseOffset": "S",
    "notes": "S R G M P D N S'"
}
```

#### instrument
`instrument` takes predefined value supported by MIDI. Take a look at the [instruments](https://www.midi.org/specifications/item/gm-level-1-sound-set). Default value is **Acoustic Grand Piano**. This is an optional parameter.

#### loop
`loop` is a positive integer. It defines the number of times the notes will be looped. Default is **1**. This is an optional parameter.

#### volume
`volume` is a positive integer. Maximum allowed volume is **127**. This is an optional parameter.

#### baseOffset
`baseOffset` is the Starting point of the first note. Default is **S**. This is an optional parameter.

#### notes
`notes` are in space separated musical notation which will be played. Look at the Syntax section. This is a required parameter.

----

## Syntax
Natural notes supported are:

 - **S**: Sa
 - **R**: Re
 - **G**: Ga
 - **M**: Ma
 - **P**: Pa
 - **D**: Dha
 - **N**: Ni

Flat notes supported are:

 - **r**: Komal Re
 - **g**: Komal Ga
 - **m**: Komal Ma
 - **d**: Komal Dha
 - **n**: Komal Ni

To play a high note, append the note with `'` and to play a low note, append it with `.`

For example:

To play **S** at one, two and three notes higher,

	S' S'' S'''

To play **S** at one, two and three notes lower,

	S. S.. S...

To elongate a note, append it with `~`

For example:

To play **S** for two beats, **S.** for three beats and **S''** for four beats,

	S~ S.~~ S''~~~

To give a pause, use `-`
For example:
To give a pause between **S** and **R**

	S - R

----

## Sample input file
```
{
	"tempo": 240,
	"tracks": [
		{
			"loop": 3,
			"notes": "S R G M P D N S'"
		},
		{
			"instrument": "Sitar",
			"volume": 100,
			"loop": 2,
			"baseOffset": "D.",
			"notes": "S R G"
		}
	]
}

```
