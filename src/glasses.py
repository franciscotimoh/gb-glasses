"""
This module uses a pre-trained image recognition model to detect a walk sign in a live camera feed.

This module assumes the existence of a custom pre-trained YOLOv5 model file named 'model_v9.pt' in the current
directory. This module was mainly provided by Mr. Jeffrey Truong
"""


# For changes to be put into effect during start up, run:
# sudo systemctl daemon-reload

import cv2
import torch
import numpy as np
import time
from sensor import Sensor


def camera():
    """Detects a walk sign in a live camera feed and returns the average confidence score of the detected walk signs.

    Returns:
        average_prob (float): The average confidence score of the detected walk signs.
    """

    image_probability = []

    # Loads the pre-trained image recognition model.
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='model_v9.pt', trust_repo=True)

    # Initializes the camera and sets the frame dimensions.
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

    # Set GPIO for Jetson Nano
    gpio_pin = 18
    sensor = Sensor(gpio_pin)

    sensor.cycle()

    walk_count = 0

    # Enters a loop to continuously read frames from the camera feed.
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

            # Performs object detection on each frame using the loaded model
            for obj in results.pandas().xyxy[0].values:
                if obj[5] == 0:
                    print(f'Don-t Walk : {obj[4]:.2f}')

                # If a walk sign is detected, updates the walk count and appends the confidence score to a list.
                elif obj[5] == 1:
                    walk_count += 2
                    print(f'Walk : {obj[4]:.2f}')
                    image_probability.append(obj[4])

            if walk_count > 0: walk_count -= 1

            # If the walk count reaches a threshold, activates the walk sign using the sensor.
            if walk_count == 10:
                sensor.set_high()
                time.sleep(1)
                sensor.set_low()
                walk_count = 0
                print('camera closed')
                cv2.destroyAllWindows()
                break

            time.sleep(0.1)

        # Turns off camera
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            print('break')
            cap.release()
            print('camera closed')
            cv2.destroyAllWindows()
            break

    # calculates the average confidence score for the detected walk signs.
    average_prob = sum(image_probability) / len(image_probability)

    return average_prob
