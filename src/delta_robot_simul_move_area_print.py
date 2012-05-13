#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose
from delta_kinematics import *

topic = 'delta_simulation'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('delta_robot')

markerArray = create_delta_simulation()
initializedMarkerArray = set_initial_delta_pose(markerArray)


print "calcInverse"
print "Pose all 0 (0.0, 0.0, 150.286912):"
angles = delta_calcInverse(0.0, 0.0, 150.286912)
print angles

print "Pose a bit more up (0.0, 0.0, 180):"
angles = delta_calcInverse(0.0, 0.0, 180)
print angles

print "delta_calcForward"
print "dynamixels all 0"
posefinal = delta_calcForward(0.0, 0.0, 0.0)
print posefinal

print "dynamixels all to pi/4 45deg"
posefinal = delta_calcForward(math.pi/4, math.pi/4, math.pi/4)
print posefinal
print "\n\n\n"

#theta = math.radians(1)
theta = 1
basetheta = theta 


idcount = 15

maxpoint = 0.0
minpoint = 99999.0

theta1 = 0.0
theta2 = 0.0
theta3 = 0.0

while not rospy.is_shutdown():
    
    while theta1 < 180:
        print "Setting dynamixel1 to " + str(math.degrees(theta1))
        print "Forward kinematics give us: "
        posefinal = delta_calcForward(theta1, theta, theta)
        print posefinal
        print "\n"
        theta1 += basetheta
        #theta += basetheta
        #theta %= math.radians(360)
        
        testpoint = Marker()
        testpoint.header.frame_id = "/map"
        testpoint.type = testpoint.SPHERE
        testpoint.action = testpoint.ADD
        testpoint.scale.x = 0.005
        testpoint.scale.y = 0.005
        testpoint.scale.z = 0.005
        testpoint.color.a = 1.0
        testpoint.color.r = 1.0
        testpoint.color.g = 1.0
        testpoint.color.b = 1.0
        testpoint.pose.orientation.w = 1.0
        testpoint.pose.position.x = posefinal[1] / 1000.0
        testpoint.pose.position.y = posefinal[2] / 1000.0
        testpoint.pose.position.z = posefinal[3] / 1000.0 * -1
        print "Testpoint position:\n" + str(testpoint.pose.position)
        print "\n"
        testpoint.id = idcount
        idcount += 1
        if testpoint.pose.position.z > maxpoint:
            maxpoint = testpoint.pose.position.z
        if testpoint.pose.position.z < minpoint:
            minpoint = testpoint.pose.position.z
        
        print "maxpoint: %f \nminpoint: %f\n" % (maxpoint, minpoint)
            
        
        print "Inverse for this point"
        angles = delta_calcInverse(posefinal[1], posefinal[2], posefinal[3])
        print str(math.degrees(angles[1])) + ", "+ str(math.degrees(angles[2])) + ", "+ str(math.degrees(angles[3]))
        print "\n"
        
        initializedMarkerArray.markers.append(testpoint)
         # Publish the MarkerArray
        publisher.publish(initializedMarkerArray)
        
        
    while  theta2 < 180:
        print "Setting dynamixel2 to " + str(math.degrees(theta2))
        print "Forward kinematics give us: "
        posefinal = delta_calcForward(theta, theta2, theta)
        print posefinal
        print "\n"
        theta2 += basetheta
        #theta += basetheta
        #theta %= math.radians(360)
        
        testpoint = Marker()
        testpoint.header.frame_id = "/map"
        testpoint.type = testpoint.SPHERE
        testpoint.action = testpoint.ADD
        testpoint.scale.x = 0.005
        testpoint.scale.y = 0.005
        testpoint.scale.z = 0.005
        testpoint.color.a = 1.0
        testpoint.color.r = 1.0
        testpoint.color.g = 1.0
        testpoint.color.b = 1.0
        testpoint.pose.orientation.w = 1.0
        testpoint.pose.position.x = posefinal[1] / 1000.0
        testpoint.pose.position.y = posefinal[2] / 1000.0
        testpoint.pose.position.z = posefinal[3] / 1000.0 * -1
        print "Testpoint position:\n" + str(testpoint.pose.position)
        print "\n"
        testpoint.id = idcount
        idcount += 1
        if testpoint.pose.position.z > maxpoint:
            maxpoint = testpoint.pose.position.z
        if testpoint.pose.position.z < minpoint:
            minpoint = testpoint.pose.position.z
        
        print "maxpoint: %f \nminpoint: %f\n" % (maxpoint, minpoint)
            
        
        print "Inverse for this point"
        angles = delta_calcInverse(posefinal[1], posefinal[2], posefinal[3])
        print str(math.degrees(angles[1])) + ", "+ str(math.degrees(angles[2])) + ", "+ str(math.degrees(angles[3]))
        print "\n"
        
        initializedMarkerArray.markers.append(testpoint)
         # Publish the MarkerArray
        publisher.publish(initializedMarkerArray)
    
    
    
        
        
    while  theta3 < 180:
        print "Setting dynamixel3 to " + str(math.degrees(theta3))
        print "Forward kinematics give us: "
        posefinal = delta_calcForward(theta, theta, theta3)
        print posefinal
        print "\n"
        theta3 += basetheta
        #theta += basetheta
        #theta %= math.radians(360)
        
        testpoint = Marker()
        testpoint.header.frame_id = "/map"
        testpoint.type = testpoint.SPHERE
        testpoint.action = testpoint.ADD
        testpoint.scale.x = 0.005
        testpoint.scale.y = 0.005
        testpoint.scale.z = 0.005
        testpoint.color.a = 1.0
        testpoint.color.r = 1.0
        testpoint.color.g = 1.0
        testpoint.color.b = 1.0
        testpoint.pose.orientation.w = 1.0
        testpoint.pose.position.x = posefinal[1] / 1000.0
        testpoint.pose.position.y = posefinal[2] / 1000.0
        testpoint.pose.position.z = posefinal[3] / 1000.0 * -1
        print "Testpoint position:\n" + str(testpoint.pose.position)
        print "\n"
        testpoint.id = idcount
        idcount += 1
        if testpoint.pose.position.z > maxpoint:
            maxpoint = testpoint.pose.position.z
        if testpoint.pose.position.z < minpoint:
            minpoint = testpoint.pose.position.z
        
        print "maxpoint: %f \nminpoint: %f\n" % (maxpoint, minpoint)
            
        
        print "Inverse for this point"
        angles = delta_calcInverse(posefinal[1], posefinal[2], posefinal[3])
        print str(math.degrees(angles[1])) + ", "+ str(math.degrees(angles[2])) + ", "+ str(math.degrees(angles[3]))
        print "\n"
        
        initializedMarkerArray.markers.append(testpoint)
         # Publish the MarkerArray
        publisher.publish(initializedMarkerArray)
        
        
    while  theta < 180:
        print "Setting all dynamixel to " + str(theta)
        print "Forward kinematics give us: "
        posefinal = delta_calcForward(theta, theta, theta)
        print posefinal
        print "\n"
        theta += basetheta

        
        testpoint = Marker()
        testpoint.header.frame_id = "/map"
        testpoint.type = testpoint.SPHERE
        testpoint.action = testpoint.ADD
        testpoint.scale.x = 0.005
        testpoint.scale.y = 0.005
        testpoint.scale.z = 0.005
        testpoint.color.a = 1.0
        testpoint.color.r = 1.0
        testpoint.color.g = 1.0
        testpoint.color.b = 1.0
        testpoint.pose.orientation.w = 1.0
        testpoint.pose.position.x = posefinal[1] / 1000.0
        testpoint.pose.position.y = posefinal[2] / 1000.0
        testpoint.pose.position.z = posefinal[3] / 1000.0 * -1
        print "Testpoint position:\n" + str(testpoint.pose.position)
        print "\n"
        testpoint.id = idcount
        idcount += 1
        if testpoint.pose.position.z > maxpoint:
            maxpoint = testpoint.pose.position.z
        if testpoint.pose.position.z < minpoint:
            minpoint = testpoint.pose.position.z
        
        print "maxpoint: %f \nminpoint: %f\n" % (maxpoint, minpoint)
            
        
        print "Inverse for this point"
        angles = delta_calcInverse(posefinal[1], posefinal[2], posefinal[3])
        print str(math.degrees(angles[1])) + ", "+ str(math.degrees(angles[2])) + ", "+ str(math.degrees(angles[3]))
        print "\n"
        
        initializedMarkerArray.markers.append(testpoint)
         # Publish the MarkerArray
        publisher.publish(initializedMarkerArray)
    
    


    idcount += 1
    rospy.sleep(0.01)
