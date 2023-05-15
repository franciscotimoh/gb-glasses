# For changes to be put into effect during start up, run:
# sudo systemctl daemon-reload

import cv2
import torch
import numpy as np
import time

from sensor import Sensor


def camera():
    image_probability = []

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='model_v9.pt', trust_repo=True)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

    gpio_pin = 18
    sensor = Sensor(gpio_pin)

    sensor.cycle()

    walk_count = 0

    while True:
        ret, frame = cap.read()

        if ret:

            if frame.shape[2] != 3:
                print("size mismatch - skip frame")
                continue

            with torch.no_grad():
                results = model(frame)

            classes = results.pandas().xyxy[0].values

            if len(classes) == 0:
                sensor.set_low()
                print(" === no detections")
            for obj in results.pandas().xyxy[0].values:
                if obj[5] == 0:
                    print(f'Don-t Walk : {obj[4]:.2f}')
                elif obj[5] == 1:
                    walk_count += 2
                    print(f'Walk : {obj[4]:.2f}')
                    image_probability.append(obj[4])

            if walk_count > 0: walk_count -= 1

            if walk_count == 10:
                sensor.set_high()
                time.sleep(1)
                sensor.set_low()
                walk_count = 0
                print('camera closed')
                cv2.destroyAllWindows()
                break

            time.sleep(0.1)

        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            print('break')
            cap.release()
            print('camera closed')
            cv2.destroyAllWindows()
            break

    average_prob = sum(image_probability) / len(image_probability)

    return average_prob
