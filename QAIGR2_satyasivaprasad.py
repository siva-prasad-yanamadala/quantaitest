import serial
import time

def main():
    # Replace 'COM1' and 'COM2' with the actual COM port names on your system
    port_name = 'COM1'
    baud_rate = 9600
    message = "QuantumAI"

    try:
        # Open the serial port
        ser = serial.Serial(port_name, baudrate=baud_rate, timeout=1)
        
        # Give some time for the connection to establish
        time.sleep(2)

        # Send the message
        print(f"Sending data: {message}")
        ser.write(message.encode())

        # Wait a bit to ensure the message is sent and received
        time.sleep(1)

        # Read the response
        if ser.in_waiting > 0:
            received_data = ser.read(len(message)).decode()
            print(f"Received data: {received_data}")
        else:
            print("No data received")

        # Close the serial port
        ser.close()

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
