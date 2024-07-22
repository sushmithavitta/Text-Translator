from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

def translate_text(translate_client, text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def detect_language(translate_client, text):
    result = translate_client.detect_language(text)
    return result['language']

def text_to_speech(tts_client, text, target_language):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code=target_language)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    return response.audio_content
