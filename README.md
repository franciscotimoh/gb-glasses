# Guidance Glasses
## Guidance Glasses Engineering Project - Gamma Beta Class
The goal of the guidance glasses is to **assist visually impaired people** in being able to **safely cross the street**. The glasses use a combination of information provided by a camera and a microphone to determine whether it is safe enough to cross. The ultrasonic provides additional information about obstacles in front of the user. This is then communicated to the user through vibrations from haptic feedback motors as the user crosses the street.
- The camera uses a ML model (YoloV5) to detect and recognize pedestrian stop or walk signs. 
- The microhpone listens to sounds that might come from pedestrian walk and stop signals to add to the algorithms confidence level on if it is a walk signal or not. It also measures the decibels of ambient sounds to determine if there is a car.
- The ultrasonic detects any objects within its range and how far they are to determine if an object is in the way.
- Haptic feedback motors located on both temples then communicate all of this through vibrations of varying frequencies and intensities.


## How to set up the environment
1. Install YoloV5
You may download directly as a Zip file from https://github.com/ultralytics/yolov5
You may also use `git clone` to clone the repository
  WARNING: Make sure to use the SSH key. We ran into a lot of environmental setup issues with HTTPS setup.
3. Install Python 3.8 or higher and set to PATH.
4. Install CUDA, selecting the options that apply to your machine.
5. Install PyTorch, again, selecting the options that apply to your machine.
6. In the YoloV5 file, open Terminal (or your OS's equivalent) and run `pip install -r requirements.txt` to download all necessary modules and components. 
7. Ensure that YoloV5 works by running this code in the Terminal of your YoloV5 directory: `python detect.py --source 0`
Make sure you have a webcam or camera plugged in into your work station.
8. If `detect.py` runs well, download all the files in the /src directory of our repository and put it in the YoloV5 directory.
9. Run the main function

*Note: Setup instructions will be updated accordingly as we progress with the project*

## Demonstrations
### Iteration 1
https://youtu.be/HQ8TKWEDKyo
