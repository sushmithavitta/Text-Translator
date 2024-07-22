from google.cloud import translate_v2 as translate
from google.cloud import speech
from google.cloud import texttospeech

def setup_translation_service(api_key):
    client = translate.Client(api_key=api_key)
    return client

def setup_speech_to_text_service(api_key):
    client = speech.SpeechClient(api_key=api_key)
    return client

def setup_text_to_speech_service(api_key):
    client = texttospeech.TextToSpeechClient(api_key=api_key)
    return client
