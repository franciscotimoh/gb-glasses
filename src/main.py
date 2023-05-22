"""The main module for running the accessibility glasses.

Synchronously runs the camera, ultrasonic sensor, and microphone modules all at the same time.
"""

from glasses import camera
from record import calc_decibel
from speech_to_text import speech_to_text
from ultra_sonic import get_distance
import multiprocessing


def main():
    """Main function for starting and running all the sensors' modules"""

    # Gets the certainty of a walk sign
    image_probability = camera()

    while True:
        # Speech to Text certainty
        queue = multiprocessing.Queue()
        stt = multiprocessing.Process(target=speech_to_text, args=(queue,))
        stt.start()
        stt.join()
        result = queue.get()
        print("Increased certainty due to hearing:", result)

        # Calls on each sensor in their own process
        ultra_sonic = multiprocessing.Process(target=get_distance)
        db = multiprocessing.Process(target=calc_decibel)

        # Start the process’s activity.
        ultra_sonic.start()
        stt.start()
        db.start()

        # Method blocks until each process that is called terminates
        ultra_sonic.join()
        stt.join()
        db.join()

        if result is not None:
            image_probability = image_probability * 1.25
            if image_probability > 1:
                image_probability = 1
            print(image_probability)


if __name__ == '__main__':
    main()

