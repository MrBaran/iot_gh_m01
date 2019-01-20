''' IoT Greenhouse - Module 1: Activity 04
    Keith E. Kelly
    K2 Creatives, LLC
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService
from iot_gh.GHTextingService import GHTextingService

print("\nGroupMe SMS Texting for IoT Greenhouse.\n")
#Enter house name and GroupMe token when prompted.
name = input("Enter a short name for your greenhouse: ")
print("\nOpen your dev.groupme.com page. Access your token and copy here.")
token = input("GroupMe token: ")
print()

last_message_id = None

ghs = IoTGreenhouseService()
ts = GHTextingService(token, ghs)

while True:
    message = ts.last_message
    if message.id != last_message_id:
        print(message.name + "   " + message.text)
        print()

        last_message_id = message.id
    sleep(.5)
