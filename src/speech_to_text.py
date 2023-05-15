import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    print('Listening to speech...')
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
            if 'walk sign' in said:
                print('\nHeard walk sign: you may cross\n')
            elif 'wait' in said:
                print('\nHeard wait: wait\n')
            else:
                print('Did not hear walk sign or wait: retrying')
                speech_to_text()
        except Exception:
            print('inconclusive audio, retrying')
            speech_to_text()
    return said