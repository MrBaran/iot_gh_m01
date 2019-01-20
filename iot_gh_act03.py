''' IoT Greenhouse - Module 1: Activity 03
    Keith E. Kelly
    K2 Creatives, LLC
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

print("IoT Greenhouse.\n")
#Enter house name when prompted.
name = input("Please enter a short name for your greenhouse: ")

#Set up service and identifiers
ghs = IoTGreenhouseService()
ghs.greenhouse.name = name
group = ghs.greenhouse.group_id
number = ghs.greenhouse.house_number

#Provide identifiers to user
print()
print("Group ID: " + group)
print("House Number: " + number)
print("House Name: " + name)

#Get greenhouse data and report
print()
tempF = ghs.temperature.get_inside_temp_F()
print("House temperature is " + str(tempF))
state = ghs.servo.get_status()
print("House state is " + state)

ghs.web_service.post_greenhouse()

print("Use heat gun and coolant to modify internal temperature.")
print("Greenhouse status updates based on threshold temp value.\n")

threshold = tempF + 5
print("Threshold set to " + str(threshold))
print()

while True:
    tempF = ghs.temperature.get_inside_temp_F()
    status = ghs.servo.get_status()
    print("temp = " + str(tempF))
    if tempF > threshold and status == "CLOSED":
        print("opening")
        ghs.servo.move(1)
    elif tempF < threshold and status == "OPEN":
        print("closing")
        ghs.servo.move(0)
        
    ghs.web_service.post_greenhouse()
    sleep(5)
