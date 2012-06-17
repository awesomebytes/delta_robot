from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
from delta_kinematics import *
from math import *
from transformations import *
import numpy as np



    # Creates the model of the system
def create_delta_simulation():
    print "Creating simulation"
    markerArray = MarkerArray()
    width = 0.005 
    
    
    # Point of first dynamixel
    base1 = Marker()
    base1.header.frame_id = "/map"
    base1.type = base1.SPHERE
    base1.action = base1.ADD
    base1.scale.x = width
    base1.scale.y = width
    base1.scale.z = width
    base1.color.a = 1.0
    base1.color.r = 1.0
    base1.color.g = 0.0
    base1.color.b = 0.0
    base1.pose.orientation.w = 1.0
    base1.pose.position.x = 0
    base1.pose.position.y = - 0.06 * sqrt(2)
    base1.pose.position.z = 0
    base1.id = 1
    
    # Point of second dynamixel
    base2 = Marker()
    base2.header.frame_id = "/map"
    base2.type = base2.SPHERE
    base2.action = base2.ADD
    base2.scale.x = width
    base2.scale.y = width
    base2.scale.z = width
    base2.color.a = 1.0
    base2.color.r = 0.0
    base2.color.g = 1.0
    base2.color.b = 0.0
    base2.pose.orientation.w = 1.0
    base2.pose.position.x = 0.06
    base2.pose.position.y = 0.06
    base2.pose.position.z = 0
    base2.id = 2
    
    # Point of third dynamixel
    base3 = Marker()
    base3.header.frame_id = "/map"
    base3.type = base3.SPHERE
    base3.action = base3.ADD
    base3.scale.x = width
    base3.scale.y = width
    base3.scale.z = width
    base3.color.a = 1.0
    base3.color.r = 0.0
    base3.color.g = 0.0
    base3.color.b = 1.0
    base3.pose.orientation.w = 1.0
    base3.pose.position.x = - 0.06 
    base3.pose.position.y = 0.06
    base3.pose.position.z = 0
    base3.id = 3
    
    
    
    
    # Arrow from first dynamixel to elbow
    arrow1 = Marker()
    arrow1.header.frame_id = "/map"
    arrow1.type = arrow1.ARROW
    arrow1.action = arrow1.ADD
    arrow1.scale.x = width
    arrow1.scale.y = width
    arrow1.color.a = 1.0
    arrow1.color.r = 1.0
    arrow1.color.g = 0.0
    arrow1.color.b = 0.0
    arrow1.points = [None]*2
    arrow1.points[0] = Point(base1.pose.position.x, base1.pose.position.y, 0.0)
    arrow1.points[1] = Point(base1.pose.position.x, base1.pose.position.y, 0.08)
    arrow1.pose.orientation.w = 1.0
    arrow1.id = 4
    
    
    # Arrow from second dynamixel to elbow
    arrow2 = Marker()
    arrow2.header.frame_id = "/map"
    arrow2.type = arrow2.ARROW
    arrow2.action = arrow2.ADD
    arrow2.scale.x = width
    arrow2.scale.y = width
    arrow2.color.a = 1.0
    arrow2.color.r = 0.0
    arrow2.color.g = 1.0
    arrow2.color.b = 0.0
    arrow2.points = [None]*2
    arrow2.points[0] = Point(base2.pose.position.x, base2.pose.position.y, 0.0)
    arrow2.points[1] = Point(base2.pose.position.x, base2.pose.position.y, 0.08)
    arrow2.pose.orientation.w = 1.0
    arrow2.id = 5
    
    # Arrow from third dynamixel to elbow
    arrow3 = Marker()
    arrow3.header.frame_id = "/map"
    arrow3.type = arrow3.ARROW
    arrow3.action = arrow3.ADD
    arrow3.scale.x = width
    arrow3.scale.y = width
    arrow3.color.a = 1.0
    arrow3.color.r = 0.0
    arrow3.color.g = 0.0
    arrow3.color.b = 1.0
    arrow3.points = [None]*2
    arrow3.points[0] = Point(base3.pose.position.x, base3.pose.position.y, 0.0)
    arrow3.points[1] = Point(base3.pose.position.x, base3.pose.position.y, 0.08)
    arrow3.pose.orientation.w = 1.0
    arrow3.id = 6
    
    # Arrow from  elbow to final for first dynamixel
    arrow4 = Marker()
    arrow4.header.frame_id = "/map"
    arrow4.type = arrow4.ARROW
    arrow4.action = arrow4.ADD
    arrow4.scale.x = width
    arrow4.scale.y = width
    arrow4.color.a = 1.0
    arrow4.color.r = 1.0
    arrow4.color.g = 0.0
    arrow4.color.b = 0.0
    arrow4.points = [None]*2
    arrow4.points[0] = arrow1.points[1]
    arrow4.points[1] = arrow1.points[1]
    arrow4.points[1].z = arrow4.points[1].z + 0.2 # end to elbow dist
    arrow4.pose.orientation.w = 1.0
    arrow4.id = 7
    
    # Arrow from second dynamixel to elbow
    arrow5 = Marker()
    arrow5.header.frame_id = "/map"
    arrow5.type = arrow5.ARROW
    arrow5.action = arrow5.ADD
    arrow5.scale.x = width
    arrow5.scale.y = width
    arrow5.color.a = 1.0
    arrow5.color.r = 0.0
    arrow5.color.g = 1.0
    arrow5.color.b = 0.0
    arrow5.points = [None]*2
    arrow5.points[0] =  arrow2.points[1]
    arrow5.points[1] =  arrow2.points[1]
    arrow5.points[1].z =  arrow2.points[1].z + 0.2
    arrow5.pose.orientation.w = 1.0
    arrow5.id = 8
    
    # Arrow from third dynamixel to elbow
    arrow6 = Marker()
    arrow6.header.frame_id = "/map"
    arrow6.type = arrow6.ARROW
    arrow6.action = arrow6.ADD
    arrow6.scale.x = width
    arrow6.scale.y = width
    arrow6.color.a = 1.0
    arrow6.color.r = 0.0
    arrow6.color.g = 0.0
    arrow6.color.b = 1.0
    arrow6.points = [None]*2
    arrow6.points[0] = arrow3.points[1]
    arrow6.points[1] = arrow3.points[1]
    arrow6.points[1].z = arrow3.points[1].z + 0.2
    arrow6.pose.orientation.w = 1.0
    arrow6.id = 9
    
    
    
    
    floor = Marker()
    floor.header.frame_id = "/map"
    floor.type = floor.CUBE
    floor.action = floor.ADD
    floor.scale.x = .2
    floor.scale.y = .2
    floor.scale.z = width
    floor.color.a = 1.0
    # brown: 205-133-63
    floor.color.r = 205.0 / 255.0
    floor.color.g = 133.0 / 255.0
    floor.color.b = 63.0 / 255.0
    floor.pose.orientation.w = 1
    floor.pose.position.x = 0
    floor.pose.position.y = 0
    floor.pose.position.z = -width
    floor.id = 10
    
    
    # Append marker
    markerArray.markers.append(base1)
    markerArray.markers.append(base2)
    markerArray.markers.append(base3)
    markerArray.markers.append(arrow1)
    markerArray.markers.append(arrow2)
    markerArray.markers.append(arrow3)
    markerArray.markers.append(arrow4)
    markerArray.markers.append(arrow5)
    markerArray.markers.append(arrow6)
    markerArray.markers.append(floor)
    
    return markerArray

    # This functions sets the initial pose of the model of the robot
    # You must pass the MarkerArray of the model of the system
    # hopefully created with: create_delta_simulation()
    # and it returns the updated model of the system
def set_initial_delta_pose(markerArray):
    print "Setting initial pose"
    endpoint = Point(0.0, 0.0, 0.150286912)
    for m in markerArray.markers:
        if m.id == 4: # from dyn1 to elbow1
            m.points[1] = Point(0.0, - 0.06 * sqrt(2) - 0.08, 0.0)
        elif m.id == 5: # from dyn2 to elbow2
            m.points[1] = Point(0.06 + 0.056568542, 0.06 + 0.056568542, 0.0)
        elif m.id == 6: # from dyn3 to elbow3
            m.points[1] = Point(-0.06 - 0.056568542, 0.06 + 0.056568542, 0.0)
        elif m.id == 7: # from elbow1 to end
            m.points[0] = Point(0.0, - 0.06 * sqrt(2) - 0.08, 0.0)
            m.points[1] = endpoint
        elif m.id == 8: # from elbow2 to end
            m.points[0] = Point(0.06 + 0.056568542, 0.06 + 0.056568542, 0.0)
            m.points[1] = endpoint
        elif m.id == 9: # from elbow3 to end
            m.points[0] = Point(-0.06 - 0.056568542, 0.06 + 0.056568542, 0.0)
            m.points[1] = endpoint
    return markerArray  
        
     # You must pass the position (should be valid) on (x,y,z) 
     # and pass on simulationMarkerArray the MarkerArray of the model of the system
     # hopefully created with: create_delta_simulation()
     # it returns the updated model of the robot with the new terminal end position
def move_simulation_to_point(x, y, z, simulationMarkerArray):
    endpoint = Point(x, y, z)
    angles = delta_calcInverse(x, y, z)
    print angles

    for m in simulationMarkerArray.markers:
        if m.id == 4: # from dyn1 to elbow1
            # For dyn1:
            pbase = (0.0, - 0.06 * sqrt(2), 0)
            pfinal = (0.0, - 0.06 * sqrt(2) - 0.08, 0.0)
            vecarrow = (pfinal[0] - pbase[0], pfinal[1] - pbase[1], pfinal[2] - pbase[2])

            #rotate de the vector over an axis by some angle.
            e1 = (1,0,0) # over X axis as dyn1 is over Y axis
            # rotation_matrix( angle, reference axis, point=(optional))
            M = rotation_matrix(np.radians(angles[1]*-1), e1)
            rotvecarrow = numpy.dot(vecarrow, M[:3,:3].T)
            newendpoint = pbase + rotvecarrow
            # We got the new point
            m.points[1] = Point( newendpoint[0], newendpoint[1], newendpoint[2])
            
        elif m.id == 5: # from dyn2 to elbow2
            # For dyn2:
            pbase = (0.06, 0.06, 0.0)
            pfinal = (0.06 + 0.056568542, 0.06 + 0.056568542, 0.0)
            vecarrow = (pfinal[0] - pbase[0], pfinal[1] - pbase[1], pfinal[2] - pbase[2])
            #rotate de the vector over an axis by some angle.
            e1 = (-1,1,0) # over its needed axis
            # rotation_matrix( angle, reference axis, point=(optional))
            M = rotation_matrix(np.radians(angles[2]*-1), e1)
            rotvecarrow = numpy.dot(vecarrow, M[:3,:3].T)
            newendpoint = pbase + rotvecarrow
            # We got the new point
            m.points[1] = Point( newendpoint[0], newendpoint[1], newendpoint[2])
            

        elif m.id == 6: # from dyn3 to elbow3
            # For dyn3:
            pbase = (- 0.06 , 0.06, 0.0)
            pfinal = (-0.06 - 0.056568542, 0.06 + 0.056568542, 0.0)
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
    