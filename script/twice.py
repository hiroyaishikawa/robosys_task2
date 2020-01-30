#!/usr/bin/env python
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
