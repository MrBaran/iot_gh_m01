''' IoT Greenhouse - Activity 01
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
print("House Number:" + number)
print("House Name:" + name)

#Get greenhouse data and report
print()
tempF = ghs.temperature.get_inside_temp_F()
print("House temperature is " + str(tempF))
state = ghs.servo.get_status()
print("House state is " + state)

ghs.web_service.post_greenhouse()
