import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            filename = "voice.mp3"
            audio.save(filename)
            print(said)
        except Exception:
            print('inconclusive audio, retrying')
            speech_to_text()
    return said


text = speech_to_text()
if 'walk sign' in text:
    print('cross sign is on')
elif 'wait' in text:
    print('wait')
else:
    print('N/A')

