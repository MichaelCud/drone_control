#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from time import sleep
import keyboard

def talker():
    takeoff = rospy.Publisher('/tello/takeoff', Empty)
    land = rospy.Publisher('/tello/land', Empty)
    velocity_publisher = rospy.Publisher('/tello/cmd_vel', Twist)
    vel_msg = Twist()
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    is_fly = False
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        if keyboard.is_pressed(" ") and not is_fly:
            is_fly = True
            takeoff.publish()
        if keyboard.is_pressed(" ") and is_fly:
            is_fly = False
            land.publish()
        if keyboard.is_pressed("w"):
            vel_msg.linear.y = 1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.y = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("s"):
            vel_msg.linear.y = -1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.y = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("a"):
            vel_msg.linear.x = -1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.x = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("d"):
            vel_msg.linear.x = 1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.x = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("up"):
            vel_msg.linear.z = 1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.z = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("down"):
            vel_msg.linear.z = -1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.linear.z = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("left"):
            vel_msg.angular.z = -1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
        if keyboard.is_pressed("right"):
            vel_msg.angular.z = 1
            velocity_publisher.publish(vel_msg)
            sleep(0.1)
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
