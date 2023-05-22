import multiprocessing
import speech_recognition as sr


def speech_to_text(queue):
    """Converts speech to text, prints what you have said, and notifies user to walk, wait, or neither.

        Returns:
            Converted speech to text

        Raises:
            Exception: inconclusive speech, non-speech sounds, or absolutely no sound
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
                print('\nHeard walk sign\n')

            # Heard wait, continues to listen for "walk sign"
            elif 'wait' in said:
                print('\nHeard wait: wait\n')
                # Send negative haptic feedback
                # queue.put(speech_to_text(queue))

            # Did not hear either "walk sign" or "wait", continues to listen for "walk sign"
            else:
                print('Did not hear walk sign or wait: retrying')
                queue.put(speech_to_text(queue))

        # Exception for when there inconclusive speech, non-speech sounds, or absolutely no sound
        except Exception:
            print('inconclusive audio, retrying')
            queue.put(speech_to_text(queue))

    queue.put(said)


def main():
    """ A portion of the intended main function only using speech to text. It increases or decreases the
    image probability based on what it has heard.
    """

    # Assumed walk sign certainty
    image_probability = 0.7

    # Enters a loop of using speech to text
    while True:
        # Starts the process of speech to text
        queue = multiprocessing.Queue()
        stt = multiprocessing.Process(target=speech_to_text, args=(queue,))
        stt.start()
        stt.join()

        # Gets the result of what was heard
        result = queue.get()
        print("Received result:", result)

        # Determines the new certainty to cross the street
        if 'walk sign' in result:
            image_probability = image_probability * 1.25
            if image_probability > 1:
                image_probability = 1
        elif 'wait' in result:
            image_probability = image_probability - (image_probability * 0.25)
            if image_probability < 0:
                image_probability = 0
        print(image_probability)

           # Tells users to walk or not to walk based off of certainity after speech to text
        if image_probability > 0.75:
            print('YOU CAN WALK')
        else:
            print('DO NOT WALK')


if __name__ == '__main__':
    main()
