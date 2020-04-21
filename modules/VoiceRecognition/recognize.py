import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech.SpeechClient.from_service_account_json('carles-voice-recognition-0c2e79e4566d.json')

    # The language of the supplied audio
    # Catala: ca-ES
    # Español: es-ES
    language_code = "ca-ES"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # 1 channel for mono, 2 for stereo
    audio_channel_count = 2

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "audio_channel_count" : audio_channel_count,
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)

    transcription = ""

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        transcription += alternative.transcript
        #print(u"Transcript: {}".format(alternative.transcript))

    return transcription


if __name__ == '__main__':
    print(sample_recognize('test.flac'))
