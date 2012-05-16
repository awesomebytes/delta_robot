#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from dynamixel_msgs.msg import MotorState
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose
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


def move_simulation_to_point(x, y, z, simulationMarkerArray):
    endpoint = Point(x, y, z)
    angles = delta_calcInverse(x, y, z)
    print angles



    for m in simulationMarkerArray.markers:
        if m.id == 4: # from dyn1 to elbow1
            # For dyn1:
            # 0.051961524227, 0, 0
            # 0.051961524227 + 0.08, 0.0, 0.0
            pbase = (0.051961524227, 0, 0)
            pfinal = (0.051961524227 + 0.08, 0.0, 0.0)
            vecarrow = (pfinal[0] - pbase[0], pfinal[1] - pbase[1], pfinal[2] - pbase[2])

            #rotate de the vector over an axis by some angle.
            e1 = (0,1,0) # over Y axis as dyn1 is over X axis
            # rotation_matrix( angle, reference axis, point=(optional))
            M = rotation_matrix(np.radians(angles[1]*-1), e1)
            rotvecarrow = numpy.dot(vecarrow, M[:3,:3].T)
            newendpoint = pbase + rotvecarrow
            # We got the new point
            m.points[1] = Point( newendpoint[0], newendpoint[1], newendpoint[2])
            
        elif m.id == 5: # from dyn2 to elbow2
            # For dyn2:
            # -0.051961524227, -0.06, 0.0
            # -0.051961524227 - 0.056568542, -0.06 - 0.056568542, 0.0
            pbase = (-0.051961524227, -0.06, 0.0)
            pfinal = (-0.051961524227 - 0.056568542, -0.06 - 0.056568542, 0.0)
            vecarrow = (pfinal[0] - pbase[0], pfinal[1] - pbase[1], pfinal[2] - pbase[2])
            #rotate de the vector over an axis by some angle.
            e1 = (1,-1,0) # over its needed axis
            # rotation_matrix( angle, reference axis, point=(optional))
            M = rotation_matrix(np.radians(angles[2]*-1), e1)
            rotvecarrow = numpy.dot(vecarrow, M[:3,:3].T)
            newendpoint = pbase + rotvecarrow
            # We got the new point
            m.points[1] = Point( newendpoint[0], newendpoint[1], newendpoint[2])
            

        elif m.id == 6: # from dyn3 to elbow3
            # For dyn3:
            # -0.051961524227, 0.06, 0.0
            # -0.051961524227 - 0.056568542, 0.06 + 0.056568542, 0.0
            pbase = (-0.051961524227, 0.06, 0.0)
            pfinal = (-0.051961524227 - 0.056568542, 0.06 + 0.056568542, 0.0)
            vecarrow = (pfinal[0] - pbase[0], pfinal[1] - pbase[1], pfinal[2] - pbase[2])
            #rotate de the vector over an axis by some angle.
            e1 = (1,1,0) 
            # rotation_matrix( angle, reference axis, point=(optional))
            M = rotation_matrix(np.radians(angles[3]), e1)
            rotvecarrow = numpy.dot(vecarrow, M[:3,:3].T)
            newendpoint = pbase + rotvecarrow
            # We got the new point
            m.points[1] = Point( newendpoint[0], newendpoint[1], newendpoint[2])
        elif m.id == 7: # from elbow1 to end
             m.points[0] = simulationMarkerArray.markers[3].points[1] # index is number -1
             m.points[1] = endpoint
        elif m.id == 8: # from elbow2 to end
             m.points[0] = simulationMarkerArray.markers[4].points[1]
             m.points[1] = endpoint
        elif m.id == 9: # from elbow3 to end
             m.points[0] = simulationMarkerArray.markers[5].points[1]
             m.points[1] = endpoint

    return simulationMarkerArray

def callback_1(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor1_pos = (data.position-500.0)/ 350.0 * 90.0
    print "Motor1 in pos: %d" % (motor1_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
    
    
def callback_2(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor2_pos = (data.position-500.0)/ 350.0 * 90.0
    print "Motor2 in pos: %d" % (motor2_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)
    
def callback_3(data):
    global motor1_pos
    global motor2_pos
    global motor3_pos
    global initializedMarkerArray
    # we move from 500 to 850 so we need to adapt the data (1023 is max pos)
    motor3_pos = (data.position-500.0)/ 350.0 * 90.0
    print "Motor3 in pos: %d" % (motor3_pos)
    posefinal = delta_calcForward(motor1_pos, motor2_pos, motor3_pos)
    initializedMarkerArray = move_simulation_to_point(posefinal[1], posefinal[2], posefinal[3], initializedMarkerArray)

def motors_listener():
    rospy.Subscriber('/motor1/status', MotorState, callback_1)
    rospy.Subscriber('/motor2/status', MotorState, callback_2)
    rospy.Subscriber('/motor3/status', MotorState, callback_3)
    # set torque off in motors
    pub1 = rospy.Publisher('/motor1/joint_torque_limit', Float64)
    pub1.publish(Float64(0.0))
    pub2 = rospy.Publisher('/motor2/joint_torque_limit', Float64)
    pub2.publish(Float64(0.0))
    pub3 = rospy.Publisher('/motor3/joint_torque_limit', Float64)
    pub3.publish(Float64(0.0))


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
    rospy.sleep(0.02)
       
