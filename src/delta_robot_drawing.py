#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose, move_simulation_to_point
from delta_kinematics import *
from transformations import *
import numpy as np
import random
import csv

global pub1
pub1 = rospy.Publisher('/motor1/command', Float64)
global pub2
pub2 = rospy.Publisher('/motor2/command', Float64)
global pub3
pub3 = rospy.Publisher('/motor3/command', Float64)


def move_dynamixels(alpha, beta, theta):
    global pub1
    pub1.publish(Float64(math.radians(alpha)))
    global pub2
    pub2.publish(Float64(math.radians(beta)))
    global pub3
    pub3.publish(Float64(math.radians(theta)))



topic = 'delta_simulation'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('delta_robot')

markerArray = create_delta_simulation()
initializedMarkerArray = set_initial_delta_pose(markerArray)


try:
    f = open('drawingpointlist.txt', 'rb')
    reader = csv.reader(f)
    idcount = 500
    drawingz = 0.20
    testpointscale = 0.005
    for row in reader:
        print row
        
        #Calculate equivalent positions from the image to the robot
        myx = (float(row[0]) * 2.0 / 10000.0) - 0.08
        myy = (float(row[1]) * 2.0 / 10000.0) - 0.08
        angles = delta_calcInverse(myx, myy, drawingz)
        print str(angles[1]) + ", "+ str(angles[2]) + ", "+ str(angles[3])
        posefinal = delta_calcForward(angles[1], angles[2], angles[3])
        
        testpoint = Marker()
        testpoint.header.frame_id = "/map"
        testpoint.type = testpoint.SPHERE
        testpoint.action = testpoint.ADD
        testpoint.scale.x = testpointscale
        testpoint.scale.y = testpointscale
        testpoint.scale.z = testpointscale
        testpoint.color.a = 1.0
        testpoint.color.r = 1.0
        testpoint.color.g = 1.0
        testpoint.color.b = 1.0
        testpoint.pose.orientation.w = 1.0
        testpoint.pose.position.x = posefinal[1] 
        testpoint.pose.position.y = posefinal[2] 
        testpoint.pose.position.z = posefinal[3]
        print "Testpoint position:\n" + str(testpoint.pose.position)
        print "\n"
        testpoint.id = idcount
        idcount += 1
    
        # Llamar a funcion que mueve los motores move_dynamixels( alpha, beta, theta)
        move_dynamixels(angles[1], angles[2], angles[3])
        initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
            
        
        initializedMarkerArray.markers.append(testpoint)
         # Publish the MarkerArray
        publisher.publish(initializedMarkerArray)
        rospy.sleep(0.02)

    while not rospy.is_shutdown():
        publisher.publish(initializedMarkerArray)
        rospy.sleep(0.02)
    
except KeyboardInterrupt:
  # do nothing here
  f.close()
  pass
