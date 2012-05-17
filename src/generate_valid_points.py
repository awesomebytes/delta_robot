#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
import rospy
import math
from delta_construct import create_delta_simulation, set_initial_delta_pose
from delta_kinematics import *
from transformations import *
import numpy as np
import random




generatedpoints = 0

try:
    f = open('valid_points_generated.txt', 'a')
    onlyone = True
    while not rospy.is_shutdown():         
        initialx = random.uniform(-0.08, 0.08)
        initialy = random.uniform(-0.08, 0.08)
        initialz = random.uniform(0.13, 0.28)
        
        angles = delta_calcInverse(initialx, initialy, initialz)
        if angles[0] > -1 and angles[1] > 0 and angles[2] > 0 and angles[3] > 0:
            #initializedMarkerArray = move_simulation_to_point(initialx, initialy, initialz, initializedMarkerArray)
            f.write(str(initialx) + ", " + str(initialy) + ", " + str(initialz) + "\n")
            generatedpoints += 1
            if generatedpoints % 50 == 0:
                print "Already generated %d points." %(generatedpoints)
    
except KeyboardInterrupt:
  # do nothing here
  f.close()
  pass
