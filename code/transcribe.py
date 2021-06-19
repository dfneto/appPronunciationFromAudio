#!/usr/bin/env python
import argparse
import io
from google.oauth2 import service_account
"""Google Cloud Speech API sample that demonstrates word time offsets with language change option.
Example usage:
    python transcribe_word_time_offsets.py -s <language> resources/audio.raw
    python transcribe_word_time_offsets.py -s <language> \gs://cloud-samples-tests/speech/vr.flac
"""
"""
pip3 install -U google-cloud-speech
pip3 install -U google-api-python-client
"""

credentials = service_account.Credentials.from_service_account_file('api-key.json')


def transcribe_file_with_word_time_offsets(speech_file):
    """Transcribe the given audio file synchronously and output the word time
    offsets."""
    from google.cloud import speech

    client = speech.SpeechClient(credentials=credentials)

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_word_time_offsets=True,
    )

    response = client.recognize(config=config, audio=audio)
    all_words_with_timestamp = []
    all_transcripts = []
    for result in response.results:
        alternative = result.alternatives[0]
        print("Transcript: {}".format(alternative.transcript))
        all_transcripts.append(alternative.transcript)

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print(f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}")
            word_with_timestamp = "\"" + word + "\"" + ": [" + str(start_time.total_seconds()) + ", " \
                                  + str(end_time.total_seconds()) + "],"
            all_words_with_timestamp.append(word_with_timestamp)

    save_in_text_file(all_words_with_timestamp, "all_words")
    save_in_text_file(all_transcripts, "all_transcripts")


def save_in_text_file(elements_to_save, file_name):
    with open(f'../files_generated/{file_name}.txt', 'w') as f:
        for element in elements_to_save:
            f.write(element + "\n")


transcribe_file_with_word_time_offsets("../audios/brand_1.wav")
