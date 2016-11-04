#!/usr/bin/python3.5

from setuptools import setup, find_packages

setup(	name='txt2midi',
		version='1.0',
		description='Convert Indian Musical Notations to MIDI file',
		url='https://github.com/anshulgupta0803/txt2midi',
		author='Anshul Gupta / Khursheed Ali',
		author_email='anshulgupta0803@gmail.com / khursheed.ali1991@gmail.com',
		license='GPL-3.0',
		packages=find_packages(),
		include_package_data=True,
		install_requires=[
			'jsonschema',
			'midiutil'
		],
		scripts=['txt-midi'],
		zip_safe=False
	)
