#!/usr/bin/env python
#[twice.py]
#
#Copyright (c) 2020 hiroya ishikawa
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

import rospy
from std_msgs.msg import Int32

add = 0

def callback(message):
	global add
	rospy.loginfo(message.data)
	#print(message.data)
	add = add + message.data
	print(add)

if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('input', Int32, callback)
	rospy.spin()
