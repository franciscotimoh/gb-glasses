"""Records and saves an audio file to calculate the decibels.

This module records audio in a .wav file and records the average decibels each second in three second intervals.
"""

import pyaudio
import wave
import audioop
from math import log10


def calc_decibel():
    """ Function to record and calculate decibels.

    Returns:
        average decibels in three seconds

    """

    # settings to record .wav file: 1024 samples, 16 bits per sample, 44100 sampls per second
    CHUNK = 1024
    total_decibel_list = []
    one_sec_decibel = []
    two_sec_decibel = []
    three_sec_decibel = []
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    interval = .5
    filename = "output.wav"

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # print('Recording for decibels...')

    # Starts recording
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
        try:
            decibel1 = 20 * log10(rms)
            one_sec_decibel.append(decibel1)
            total_decibel_list.append(decibel1)
            frames.append(data)
        except ValueError:
            pass

    for i in range(0, int(fs / CHUNK * interval)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        try:
            decibel2 = 20 * log10(rms)
            two_sec_decibel.append(decibel2)
            total_decibel_list.append(decibel2)
            frames.append(data)
        except ValueError:
            pass

    for i in range(0, int(fs / CHUNK * interval)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        try:
            decibel3 = 20 * log10(rms)
            three_sec_decibel.append(decibel3)
            total_decibel_list.append(decibel3)
            frames.append(data)
        except ValueError:
            pass

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()

    # print('Finished recording for decibels.')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Finds the average decibels from 0 to 1 seconds, 1 to 2 seconds, and 2 to 3 seconds, and across total 3 seconds
    try:
        first_average = sum(one_sec_decibel) / len(one_sec_decibel)
        second_average = sum(two_sec_decibel) / len(two_sec_decibel)
        third_average = sum(three_sec_decibel) / len(three_sec_decibel)
        average_decibel = (first_average + second_average + third_average) / (
                    len(one_sec_decibel) + len(two_sec_decibel) + len(three_sec_decibel))
    except ZeroDivisionError:
        calc_decibel()

    # Compares the average decibels to determine if a car is coming towards you or not or neither
    if first_average < second_average < third_average:
        print('\nGetting louder. Car may be moving towards you.\n')
    elif first_average > second_average > third_average:
        print('\nGetting quieter. Car may be moving away from you.\n')
    else:
        print('\nNot getting louder or quieter.\n')

    return calc_decibel()

