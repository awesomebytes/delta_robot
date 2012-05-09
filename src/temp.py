#! /usr/bin/env python
import roslib; roslib.load_manifest('delta_robot')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
from geometry_msgs.msg import Point

topic = 'delta_marker_array'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('delta_sim')

markerArray = MarkerArray()



# Point of first dynamixel
base1 = Marker()
base1.header.frame_id = "/map"
base1.type = base1.SPHERE
base1.action = base1.ADD
base1.scale.x = .1
base1.scale.y = .1
base1.scale.z = .1
base1.color.a = 1.0
base1.color.r = 1.0
base1.color.g = 0.0
base1.color.b = 0.0
base1.pose.orientation.w = 1.0
base1.pose.position.x = 0.51961524227
base1.pose.position.y = 0
base1.pose.position.z = 0
base1.id = 1

# Point of second dynamixel
base2 = Marker()
base2.header.frame_id = "/map"
base2.type = base2.SPHERE
base2.action = base2.ADD
base2.scale.x = .1
base2.scale.y = .1
base2.scale.z = .1
base2.color.a = 1.0
base2.color.r = 0.0
base2.color.g = 1.0
base2.color.b = 0.0
base2.pose.orientation.w = 1.0
base2.pose.position.x = -0.51961524227
base2.pose.position.y = -0.6
base2.pose.position.z = 0
base2.id = 2

# Point of third dynamixel
base3 = Marker()
base3.header.frame_id = "/map"
base3.type = base3.SPHERE
base3.action = base3.ADD
base3.scale.x = .1
base3.scale.y = .1
base3.scale.z = .1
base3.color.a = 1.0
base3.color.r = 0.0
base3.color.g = 0.0
base3.color.b = 1.0
base3.pose.orientation.w = 1.0
base3.pose.position.x = -0.51961524227
base3.pose.position.y = 0.6
base3.pose.position.z = 0
base3.id = 3




# Arrow from first dynamixel to elbow
arrow1 = Marker()
arrow1.header.frame_id = "/map"
arrow1.type = arrow1.ARROW
arrow1.action = arrow1.ADD
arrow1.scale.x = .1
arrow1.scale.y = .1
arrow1.color.a = 1.0
arrow1.color.r = 1.0
arrow1.color.g = 0.0
arrow1.color.b = 0.0
arrow1.points = [None]*2
arrow1.points[0] = Point(0.51961524227, 0.0, 0.0)
arrow1.points[1] = Point(0.51961524227, 0.0, 0.8)
arrow1.id = 4

# Arrow from second dynamixel to elbow
arrow2 = Marker()
arrow2.header.frame_id = "/map"
arrow2.type = arrow2.ARROW
arrow2.action = arrow2.ADD
arrow2.scale.x = .1
arrow2.scale.y = .1
arrow2.color.a = 1.0
arrow2.color.r = 0.0
arrow2.color.g = 1.0
arrow2.color.b = 0.0
arrow2.points = [None]*2
arrow2.points[0] = Point(-0.51961524227, -0.6, 0.0)
arrow2.points[1] = Point(-0.51961524227, -0.6, 0.8)
arrow2.id = 5

# Arrow from third dynamixel to elbow
arrow3 = Marker()
arrow3.header.frame_id = "/map"
arrow3.type = arrow3.ARROW
arrow3.action = arrow3.ADD
arrow3.scale.x = .1
arrow3.scale.y = .1
arrow3.color.a = 1.0
arrow3.color.r = 0.0
arrow3.color.g = 0.0
arrow3.color.b = 1.0
arrow3.points = [None]*2
arrow3.points[0] = Point(-0.51961524227, 0.6, 0.0)
arrow3.points[1] = Point(-0.51961524227, 0.6, 0.8)
arrow3.id = 6



# Append marker
markerArray.markers.append(base1)
markerArray.markers.append(base2)
markerArray.markers.append(base3)
markerArray.markers.append(arrow1)
markerArray.markers.append(arrow2)
markerArray.markers.append(arrow3)

while not rospy.is_shutdown():

   # Publish the MarkerArray
   publisher.publish(markerArray)

   rospy.sleep(0.01)
