#!/usr/bin/env python

# [START import_libraries]
import argparse
import io
# [END import_libraries]
from google.cloud import speech
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_file(speech_files):
	output = ""
	"""Transcribe the given audio file."""
	speech_client = speech.Client()
	for speech_file in speech_files:
		with io.open(speech_file, 'rb') as audio_file:
			content = audio_file.read()
			audio_sample = speech_client.sample(
			content=content,
			source_uri=None,
			encoding='LINEAR16',
			sample_rate_hertz=16000)
		alternatives = audio_sample.recognize('cmn-Hant-TW')
		for alternative in alternatives:
			output+=alternative
		#print('Transcript: {}'.format(alternative.transcript))
	return output

def wavSplit(filename=''):
	
	if(filename==''):
		print 'ERROR Filename!'
		return False
	chunklist = [] 
	sound_file = AudioSegment.from_wav(filename)
	audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=500,
    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
)
	for i, chunk in enumerate(audio_chunks):
		out_file = "{0}-chunk{1}.wav".format(filename,i)
		print "exporting", out_file
		chunk.export(out_file, format="wav")
		chunklist.append(out_file)
	#return transcribe_file(chunklist)
	return chunklist 
	