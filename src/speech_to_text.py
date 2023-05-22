"""Converts text to speech.

This module uses Google's speech recognition library to convert speech to text.
"""

import speech_recognition as sr


def speech_to_text():
    """Converts speech to text, prints what you have said, and notifies user to walk, wait, or neither.

    Returns:
        Converted speech to text
    """

    # Creates a new Recognizer instance, a collection of speech recognition functionality.
    r = sr.Recognizer()
    print('Listening to speech...')

    # Identifies microphone as a source for input and converts input into a audio
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        # Using Google's speech recognition, it uses the audio to identify speech and determines walk ability
        try:
            said = r.recognize_google(audio)
            print(f'\nYou said: {said}\n')

            # You can walk
            if 'walk sign' in said:
                print('\nHeard walk sign: you may cross\n')

            # Heard wait, continues to listen for "walk sign"
            elif 'wait' in said:
                print('\nHeard wait: wait\n')
                # Send negative haptic feedback
                speech_to_text()

            # Did not hear either "walk sign" or "wait", continues to listen for "walk sign"
            else:
                print('Did not hear walk sign or wait: retrying')
                speech_to_text()

        # Exception for when there inconclusive speech, non-speech sounds, or absolutely no sound
        except Exception:
            print('inconclusive audio, retrying')
            speech_to_text()

    return said
