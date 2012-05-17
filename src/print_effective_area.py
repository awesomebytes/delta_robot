#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose
from delta_kinematics import *
import csv


topic = 'delta_simulation'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('delta_robot')

markerArray = create_delta_simulation()
initializedMarkerArray = set_initial_delta_pose(markerArray)


idcount = 100

pointwidth = 0.005



with open('valid_points_generated.txt', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if idcount < 50000:
                if len(row) > 0:
                    testpoint = Marker()
                    testpoint.header.frame_id = "/map"
                    testpoint.type = testpoint.SPHERE
                    testpoint.action = testpoint.ADD
                    testpoint.scale.x = pointwidth
                    testpoint.scale.y = pointwidth
                    testpoint.scale.z = pointwidth
                    testpoint.color.a = 1.0
                    testpoint.color.r = 1.0
                    testpoint.color.g = 1.0
                    testpoint.color.b = 1.0
                    testpoint.pose.orientation.w = 1.0
                    testpoint.pose.position.x = float(row[0])
                    testpoint.pose.position.y = float(row[1])
                    testpoint.pose.position.z = float(row[2])
                    testpoint.id = idcount
                    idcount += 1
                    initializedMarkerArray.markers.append(testpoint)
        

print "Finished loading points"

while not rospy.is_shutdown():
    
        

     # Publish the MarkerArray
    publisher.publish(initializedMarkerArray)
    

    rospy.sleep(0.02)
