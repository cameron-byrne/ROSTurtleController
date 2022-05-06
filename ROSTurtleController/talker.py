#!/usr/bin/env python

import socket
import rospy
import _thread
from std_msgs.msg import String
from geometry_msgs.msg import Twist

data = ''

def talk(pub, rate, movement_message):
    pub.publish(movement_message)
    rate.sleep()

def listening_thread():
    UDP_IP = "192.168.56.101"  # 75.30.236.75
    UDP_PORT = 17484

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    global data  # data needs to be defined as global inside the thread
    while True:
        data_raw, addr = sock.recvfrom(1024)
        data = data_raw.decode()    # My test message is encoded


def main():
    global data
    is_turning_right = False
    is_turning_left = False
    is_moving_forward = False
    is_moving_backward = False

    try:
        _thread.start_new_thread(listening_thread, ())
    except:
        print("Error: unable to start thread")
        quit()

    while True:

        # UDP recvfrom is a blocking function: therefore the bot needs to be running on another thread!


        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(100)  # update rate in hz

        # Here, set up the command for what the turtle should be doing based on current instruction state
        command_message = Twist()
        if is_turning_left:
            command_message.angular.z = 1
        if is_turning_right:
            command_message.angular.z = -1
        if is_moving_forward:
            command_message.linear.x = 1

        # Send that command to the turtle controller
        try:
            talk(pub, rate, command_message)
        except rospy.ROSInterruptException:
            print("oopsies, interrupted")


        # if we receive a message, start sending to robot:
        if data != '':

            # parse the received input, modify variables accordingly
            if data == "go":
                is_moving_forward = True
                is_moving_backward = False
            if data == "turn_right":
                is_turning_right = True
                is_turning_left = False
            if data == "turn_left":
                is_turning_right = False
                is_turning_left = True
            if data == "stop":
                is_turning_right = False
                is_turning_left = False
                is_moving_forward = False
                is_moving_backward = False
            if data == "stop_turn":
                is_turning_right = False
                is_turning_left = False
            if data == "stop_motion":
                is_moving_forward = False
                is_moving_backward = False
            data = ''



if __name__ == '__main__':
    main()
