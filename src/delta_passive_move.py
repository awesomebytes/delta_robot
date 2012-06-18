#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from dynamixel_msgs.msg import JointState
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose, move_simulation_to_point
from delta_kinematics import *
from transformations import *
import numpy as np
import random

global motor1_pos
motor1_pos = 0
global motor2_pos
motor2_pos = 0
global motor3_pos
motor3_pos = 0
global initializedMarkerArray
global trailMarkerArray
trailMarkerArray = MarkerArray()

global max_trail_points
max_trail_points = 100
global current_trail_point
current_trail_point = 600
global current_trail_point_qtty
current_trail_point_qtty = 0

def generate_last_visited_point(x, y, z):
    global max_trail_points
    global current_trail_point
    
    testpointscale = 0.005
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
    testpoint.pose.position.x = x
    testpoint.pose.position.y = y
    testpoint.pose.position.z = z
    testpoint.id = current_trail_point
    if current_trail_point - 600 >= max_trail_points:
        current_trail_point = 601
    current_trail_point += 1
    return testpoint


def callback_1(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    global trailMarkerArray
    global current_trail_point
    global current_trail_point_qtty
    global max_trail_points
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor1_pos = math.degrees(data.current_pos)#-500.0)/ 350.0 * 90.0
    #print "Motor1 in pos: %d" % (motor1_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
    point = generate_last_visited_point(posefinal[1], posefinal[2], posefinal[3])
    current_trail_point_qtty += 1
    if current_trail_point_qtty >= max_trail_points:
        trailMarkerArray.markers.pop(0) # the 11th element is the first testpoint always
        current_trail_point_qtty -= 1
    trailMarkerArray.markers.append(point)
    #publisher.publish(trailMarkerArray)
    
def callback_2(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    global trailMarkerArray
    global current_trail_point
    global current_trail_point_qtty
    global max_trail_points
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor2_pos = math.degrees(data.current_pos)#(data.position-500.0)/ 350.0 * 90.0
    #print "Motor2 in pos: %d" % (motor2_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
    point = generate_last_visited_point(posefinal[1], posefinal[2], posefinal[3])
    current_trail_point_qtty += 1
    if current_trail_point_qtty >= max_trail_points:
        trailMarkerArray.markers.pop(0) # the 11th element is the first testpoint always
        current_trail_point_qtty -= 1
    trailMarkerArray.markers.append(point)
    #publisher.publish(trailMarkerArray)
    
def callback_3(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    global trailMarkerArray
    global current_trail_point
    global current_trail_point_qtty
    global max_trail_points
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor3_pos = math.degrees(data.current_pos)#(data.position-500.0)/ 350.0 * 90.0
    #print "Motor3 in pos: %d" % (motor3_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
    point = generate_last_visited_point(posefinal[1], posefinal[2], posefinal[3])
    current_trail_point_qtty += 1
    if current_trail_point_qtty >= max_trail_points:
        trailMarkerArray.markers.pop(0) # the 11th element is the first testpoint always
        current_trail_point_qtty -= 1
    trailMarkerArray.markers.append(point)
    #publisher.publish(trailMarkerArray)

def motors_listener():
    rospy.Subscriber('/motor1/state', JointState, callback_1)
    rospy.Subscriber('/motor2/state', JointState, callback_2)
    rospy.Subscriber('/motor3/state', JointState, callback_3)



topic = 'delta_simulation'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('delta_robot')

markerArray = create_delta_simulation()
initializedMarkerArray = set_initial_delta_pose(markerArray)



print "starting motors_listener"
motors_listener()

while not rospy.is_shutdown():
        
    #initializedMarkerArray.markers.append(testpoint)
    # Publish the MarkerArray
    publisher.publish(initializedMarkerArray)
    publisher.publish(trailMarkerArray)

    #print "publishing %d number of markers on initializedMarkerArray" % (len(initializedMarkerArray.markers))
    #print "publishing %d number of markers on trailMarkerArray" % (len(trailMarkerArray.markers))
    print "number of points in current_trail_point: %d" %(current_trail_point)
    rospy.sleep(0.02)
       
