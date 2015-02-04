#!/usr/bin/env python
import roslib; roslib.load_manifest('second_tutorials')
import rospy
from turtlesim.msg import Velocity

def callback(data):
        rospy.loginfo("I heard linear %f", data.linear)
	rospy.loginfo("I heard angular %f", data.angular)

def listener():
        rospy.init_node('TedyGanteng', anonymous=True)
        rospy.Subscriber("turtle1/command_velocity", Velocity, callback)
        rospy.spin()
if __name__=='__main__':
        listener()
