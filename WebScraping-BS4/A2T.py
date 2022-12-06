import time, os, io
from google.cloud import speech_v1p1beta1 as speech


def audioToText(mp3Path):
    #setting Google credential
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'google_secret_key.json'
    # Instantiates a client
    client = speech.SpeechClient()


    with io.open(mp3Path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        # audio = speech.RecognitionAudio(uri=gcs_uri)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        # Detects speech in the audio file
        response = client.recognize(request={"config": config, "audio": audio})

    return response.results[0].alternatives[0].transcript
