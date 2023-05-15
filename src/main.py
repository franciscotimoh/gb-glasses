from glasses import camera
from record import calc_decibel
from speech_to_text import speech_to_text
# from ultra_sonic import get_distance

from multiprocessing import Process


def main():
    image_probability = camera()

    # ultra_sonic = Process(target=get_distance)
    stt = Process(target=speech_to_text)
    db = Process(target=calc_decibel)

    # ultra_sonic.start()
    stt.start()
    db.start()

    # ultra_sonic.join()
    stt.join()
    db.join()


if __name__ == '__main__':
    main()
