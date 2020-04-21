import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import os

fs = 44100  # Sample rate
seconds = 3  # Duration of recording
tmp_default = 'tmp.wav'
out_default = 'tmp.flac'


def get_audio():
    try:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()                                                           # Wait until recording is finished
        write(tmp_default, fs, myrecording)                                 # Save as WAV file

        data, fs_read = sf.read(tmp_default)                                # Extract audio data and sampling rate from file
        sf.write(out_default, data, fs_read)                                # Save as FLAC file at correct sampling rate

        os.remove(tmp_default)                                              # Get rid of temporal wav
        return True

    except Exception as e:
        print("ERROR: %s" % e)
        return


if __name__ == '__main__':
    get_audio()
