# Import necessary libraries
import Jetson.GPIO as GPIO
import time

# Setup GPIO pin mode
GPIO.setmode(GPIO.BOARD)

# Set GPIO pins for trigger and echo
trigger_pin = 16
echo_pin = 18

# Set GPIO direction for trigger and echo pins
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def get_distance():
    # Send trigger signal
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    # Record the time the trigger signal is sent
    pulse_start_time = time.time()

    # Wait for echo signal to be received
    while GPIO.input(echo_pin) == GPIO.LOW:
        continue

    # Record the time the echo signal is sent
    pulse_end_time = time.time()

    # Calculate distance based on time of pulse
    pulse_duration = pulse_end_time - pulse_start_time
    speed_of_sound = 34300 # in cm/s
    distance = (pulse_duration * speed_of_sound) / 2

    return distance

# Call the get_distance() function to retrieve the distance
# distance = get_distance()
 
# Print the distance to the console
# print("Distance : {} cm".format(distance))

# Cleanup GPIO settings
# GPIO.cleanup()
