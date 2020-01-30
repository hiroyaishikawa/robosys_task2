#[input.py]
#
#Copyright (c) 2020 hiroya ishikawa
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php
#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Int32

rospy.init_node('input')
pub = rospy.Publisher('input', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0

while not rospy.is_shutdown():
	print('input >>')
	n = input()
	pub.publish(n)
	rate.sleep()
