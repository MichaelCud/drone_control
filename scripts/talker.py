#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

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
