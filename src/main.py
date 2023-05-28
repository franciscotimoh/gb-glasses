"""The main module for running the accessibility glasses.

Synchronously runs the camera, ultrasonic sensor, and microphone modules all at the same time.
"""

from record import calc_decibel
from speech_to_text import speech_to_text
# from ultra_sonic import get_distance
import multiprocessing
from glasses_cam import camera


def main():
    """Main function for starting and running all the sensors' modules"""

    while True:
        # SPEECH TO TEXT
        # Starts the process of speech to text
        speech = multiprocessing.Queue()
        certainty = multiprocessing.Queue()

        # Calls on each sensor in their own process
        # ultra_sonic = multiprocessing.Process(target=get_distance)
        stt = multiprocessing.Process(target=speech_to_text, args=(speech,))
        db = multiprocessing.Process(target=calc_decibel)
        cam = multiprocessing.Process(target=camera, args=(certainty,))

        # Start the process’s activity.
        # ultra_sonic.start()
        db.start()
        cam.start()
        stt.start()

        # Method blocks until each process that is called terminates
        # ultra_sonic.join()
        cam.join()
        db.join()
        stt.join()

        # Gets the result of what was heard
        text = speech.get()
        image_probability = float(certainty.get())
        print(image_probability)
        print("Received result:", text)

        # Determines the new certainty to cross the street
        if 'walk sign is on' in text:
            image_probability = image_probability * 1.25
            if image_probability > 1:
                image_probability = 1
        elif 'wait' in text:
            image_probability = image_probability - (image_probability * 0.25)
            if image_probability < 0:
                image_probability = 0
        print(image_probability)

        if image_probability > 0.75:
            print('YOU CAN WALK HEHEHEHEH')
        else:
            print('DO NOT WALK AHHHHH')


if __name__ == '__main__':
    main()
