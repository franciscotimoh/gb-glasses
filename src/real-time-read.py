import serial

serial_port = "COM6"  # Update with the correct port for your Arduino
baud_rate = 9600

try:
    ser = serial.Serial(serial_port, baud_rate)
    print("Serial communication established.")
except serial.SerialException:
    print("Failed to establish serial communication.")
    exit(1)

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print("Received data:", data)
    except KeyboardInterrupt:
        break

ser.close()
