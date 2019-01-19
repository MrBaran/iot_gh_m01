from time import sleep
from datetime import datetime
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

def test_lamps():
    LAMP_ON_DELAY = 3
    LAMP_OFF_DELAY = 3
    print()
    print("Testing lamps...")
    print("Note: jumper must be positioned on J1 for Red LED to light.")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            ghs.lamps.red.on() 
            print("Red", ghs.lamps.red.get_status())
            sleep(LAMP_ON_DELAY)
            ghs.lamps.red.off() 
            print("Red", ghs.lamps.red.get_status())
            sleep(LAMP_OFF_DELAY)
            ghs.lamps.white.on() 
            print("White", ghs.lamps.white.get_status())
            sleep(LAMP_ON_DELAY)
            ghs.lamps.white.off() 
            print("White", ghs.lamps.white.get_status())
            sleep(LAMP_OFF_DELAY)
            ghs.lamps.dual.on_green() 
            print("Dual", ghs.lamps.dual.get_status())
            sleep(LAMP_ON_DELAY)
            ghs.lamps.dual.off() 
            print("Dual", ghs.lamps.dual.get_status())
            sleep(LAMP_OFF_DELAY)
            ghs.lamps.dual.on_yellow() 
            print("Dual", ghs.lamps.dual.get_status())
            sleep(LAMP_ON_DELAY)
            ghs.lamps.dual.off() 
            print("Dual", ghs.lamps.dual.get_status())
            sleep(LAMP_OFF_DELAY)
    except KeyboardInterrupt:
        ghs.lamps.dual.off()
        ghs.lamps.red.off() 
        ghs.lamps.white.off() 
    print("Lamp test done.")
    print()

def test_switches():
    #from iot_gh.GHSwitches import GHSwitch
    print()
    print("Testing switches. PB activates Red LED, Toggle activates White LED.")
    print("Use Ctrl+C to end test.")
    last_pb_state = None
    last_toggle_state = None
    print()    
    try:
        while True:
            new_pb_state = ghs.switches.push_button.get_state()
            if new_pb_state != last_pb_state:
                print("PB Switch", ghs.switches.push_button.get_status())
                ghs.lamps.red.toggle()
                last_pb_state = new_pb_state

            new_toggle_state = ghs.switches.toggle.get_state()
            if new_toggle_state != last_toggle_state:
                print("Toggle Switch", ghs.switches.toggle.get_status())
                ghs.lamps.white.toggle()
                last_toggle_state = new_toggle_state

            sleep(.5)
    except KeyboardInterrupt:
        pass
    print("Switch test done.")
    print()

def test_fan():
    print()
    print("Testing fan.")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            ghs.fan.on()
            print("Fan", ghs.fan.get_status())
            sleep(5)
            ghs.fan.off()
            print("Fan", ghs.fan.get_status())
            sleep(5)
    except KeyboardInterrupt:
        ghs.fan.off()
    print("Fan test done.")
    print()

def test_buzzer():
    print()
    print("Testing buzzer.")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            ghs.buzzer.on()
            print("Buzzer", ghs.buzzer.get_status())
            sleep(1)
            ghs.buzzer.off()
            print("Buzzer", ghs.buzzer.get_status())
            sleep(1)
    except KeyboardInterrupt:
        ghs.buzzer.off()
    print("Buzzer test done.")
    print()

def test_servo():
    print()
    print("Testing servo.")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            pos = .5
            ghs.servo.move(pos)
            print("Servo", ghs.servo.get_status())
            sleep(1)
            pos = 1
            ghs.servo.move(pos)
            print("Servo", ghs.servo.get_status())
            sleep(1)
            pos = .5
            ghs.servo.move(pos)
            print("Servo", ghs.servo.get_status())
            sleep(1)
            pos = 0
            ghs.servo.move(pos)
            print("Servo", ghs.servo.get_status())
            sleep(1)
    except KeyboardInterrupt:
        pos = 0
        ghs.servo.move(pos)
    print("Servo test done.")
    print()

def test_temperature():
    print()
    print("Testing temp sensor.")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            print("i temp F: %d" % ghs.temperature.get_inside_temp_F())
            print("o temp F: %d" % ghs.temperature.get_outside_temp_F())
            sleep(1)
    except KeyboardInterrupt:
        pass
    print("Temp sensor test done.")
    print()    

def test_analog():
    print()
    print("Testing analog inputs")
    print("Use Ctrl+C to end test.")
    try:
        while True:
            print()
            print("Pot value: %i" % ghs.analog.pot.get_value())
            print("Light value:" + str(ghs.analog.light.get_value()))
            print("Aux value:" + str(ghs.analog.aux.get_value()))
            sleep(1)
    except KeyboardInterrupt:
        pass
    print("Analog test done.")
    print()
        
def show_menu():
    print("IoT Greenhouse integration testing.")
    print()
    print("\t0\tExit Tests")
    print("\t1\tTest Lamps")
    print("\t2\tTest Switches")
    print("\t3\tTest Fan")
    print("\t4\tTest Buzzer")
    print("\t5\tTest Servo")
    print("\t6\tTest Temperature")
    print("\t7\tTest Potentiometer")
        

def main():
    test_complete = False
    while not test_complete:
        show_menu()
        user_entry = input("Enter test number: ")
        if not user_entry.isdigit():
            print("Invalid entry. Try again.\n")
        else:
            user_choice = int(user_entry)
            if user_choice == 0:
                test_complete = True
            elif user_choice == 1:
                test_lamps()
            elif user_choice == 2:
                test_switches()
            elif user_choice == 3:
                test_fan()
            elif user_choice == 4:
                test_buzzer()
            elif user_choice == 5:
                test_servo()
            elif user_choice == 6:
                test_temperature()
            elif user_choice == 7:
                test_analog()
            elif user_choice == 8:
                pass
            elif user_choice == 9:
                pass
            else:
                print("Invalid entry.")
    print("Done.")

if __name__ == "__main__":
    main()



