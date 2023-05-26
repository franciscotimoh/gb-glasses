"""The main module for running the accessibility glasses.

Synchronously runs the camera, ultrasonic sensor, and microphone modules all at the same time.
"""

from record import calc_decibel
from speech_to_text import speech_to_text
# from ultra_sonic import get_distance
import multiprocessing
from detect import mayne, parse_opt


def camera():
    opt = parse_opt()
    mayne(opt)

def main():
    """Main function for starting and running all the sensors' modules"""

    # Gets the certainty of a walk sign

    image_probability = 0.7

    while True:
        # SPEECH TO TEXT
        # Starts the process of speech to text
        queue = multiprocessing.Queue()


        # Calls on each sensor in their own process
        # ultra_sonic = multiprocessing.Process(target=get_distance)
        stt = multiprocessing.Process(target=speech_to_text, args=(queue,))
        db = multiprocessing.Process(target=calc_decibel)
        cam = multiprocessing.Process(target=camera)


        # Start the process’s activity.
        # ultra_sonic.start()
        db.start()
        cam.start()
        stt.start()

        # Method blocks until each process that is called terminates
        # ultra_sonic.join()
        # cam.join()
        # db.join()
        # stt.join()

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

        if image_probability > 0.75:
            print('YOU CAN WALK')
        else:
            print('DO NOT WALK')


if __name__ == '__main__':
    main()

