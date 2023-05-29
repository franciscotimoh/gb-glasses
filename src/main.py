"""The main module for running the accessibility glasses.

Synchronously runs the camera, ultrasonic sensor, and microphone modules all at the same time.
"""

from record import calc_decibel
from speech_to_text import speech_to_text
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
        stt = multiprocessing.Process(target=speech_to_text, args=(speech,))
        db = multiprocessing.Process(target=calc_decibel)
        cam = multiprocessing.Process(target=camera, args=(certainty,))

        # Start the process’s activity.
        db.start()
        cam.start()
        stt.start()


if __name__ == '__main__':
    main()
