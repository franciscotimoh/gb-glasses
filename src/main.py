from speech_to_text import speech_to_text
# from ultra_sonic import get_distance
import multiprocessing
from glasses_cam import camera
from record import calc_decibel

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
        stt.start()
        cam.start()
        db.start()


        # Gets the result of what was heard
        text = speech.get()
        print("Received result:", text)


if __name__ == '__main__':
    main()
