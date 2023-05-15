import pyaudio
import wave
import audioop
from math import log10
import time


def calc_decibel():
    time.sleep(3)
    CHUNK = 1024  # Record in chunks of 1024 samples
    total_decibel_list = []
    one_sec_decibel = []
    two_sec_decibel = []
    three_sec_decibel = []
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    interval = 1
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording for decibels...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=CHUNK,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / CHUNK * interval)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        decibel1 = 20 * log10(rms)
        one_sec_decibel.append(decibel1)
        total_decibel_list.append(decibel1)
        frames.append(data)

    for i in range(0, int(fs / CHUNK * interval)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        decibel2 = 20 * log10(rms)
        two_sec_decibel.append(decibel2)
        total_decibel_list.append(decibel2)
        frames.append(data)

    for i in range(0, int(fs / CHUNK * interval)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        decibel3 = 20 * log10(rms)
        three_sec_decibel.append(decibel3)
        total_decibel_list.append(decibel3)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording for decibels.')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    first_average = sum(one_sec_decibel) / len(one_sec_decibel)
    second_average = sum(two_sec_decibel) / len(two_sec_decibel)
    third_average = sum(three_sec_decibel) / len(three_sec_decibel)
    average_decibel = (first_average + second_average + third_average) / (len(one_sec_decibel) + len(two_sec_decibel) + len(three_sec_decibel))

    if first_average < second_average < third_average:
        print('\nGetting louder. Car may be moving towards you.\n')
    elif first_average > second_average > third_average:
        print('\nGetting quieter. Car may be moving away from you.\n')
    else:
        print('Not getting louder or quieter.')

    return calc_decibel()