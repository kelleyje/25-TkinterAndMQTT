"""
Using a Brickman (robot) as the receiver of messages.
"""

# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.

import mqtt_remote_method_calls as com
import time
import bring


class DelegateThatReceives(object):

    def __init__(self, robot):
        self.robot = robot

    def say_it(self, message):
        print("Message received!", message)

    def forward(self, arg1, arg2):
        self.robot.go(arg1, arg2)

def main():
    note = bring.DriveSystem()

    name1 = 'subscriber'
    name2 = 'publisher'

    my_delegate = DelegateThatReceives(note)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()