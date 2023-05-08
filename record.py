import pyaudio
import wave
import audioop
from math import log10

CHUNK = 1024  # Record in chunks of 1024 samples


def save_audio_clip():
    decibel_list = []
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=CHUNK,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / CHUNK * seconds)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        decibel = 20 * log10(rms)
        decibel_list.append(decibel)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    decibel_total = 0
    for interval in decibel_list:
        decibel_total += interval
    average_decibel = decibel_total/len(decibel_list)

    return average_decibel


zero_seconds = save_audio_clip()
three_seconds = save_audio_clip()
six_seconds = save_audio_clip()

if zero_seconds < three_seconds and zero_seconds < six_seconds:
    print('car moving towards you')
elif zero_seconds > three_seconds and zero_seconds > six_seconds:
    print('car moving away from you')

