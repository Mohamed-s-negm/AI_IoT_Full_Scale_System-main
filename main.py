from azure.iot.device import IoTHubDeviceClient, Message
import json
import random
import time

# Your IoT Hub device connection string
conn_str = "HostName=AzureIoTHubGraduationProject.azure-devices.net;DeviceId=graduation-project;SharedAccessKey=9jf98uJwKI4lgjpcCuiHzRqO7J0zTDQIu+x86KaMpIU="

# Create the IoT device client
device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

def send_sensor_data():
    # Simulate sensor data
    temperature = random.uniform(20.0, 40.0)  # Random temperature
    smoke = random.uniform(0.0, 10.0)         # Random smoke level

    # Data to send to the IoT Hub
    data = {
        "temperature": temperature,
        "smoke": smoke
    }

    # Create a message with the data and send it
    message = Message(json.dumps(data))
    device_client.send_message(message)
    print(f"Sent message: {data}")

# Send data every 5 seconds
while True:
    send_sensor_data()
    time.sleep(5)
