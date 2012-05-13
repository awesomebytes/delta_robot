from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point

def create_delta_simulation():
    print "Creating simulation"
    markerArray = MarkerArray()
    width = 0.005 # 0.005
    
    
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
    base1.pose.position.x = 0.051961524227
    base1.pose.position.y = 0
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
    base2.pose.position.x = -0.051961524227
    base2.pose.position.y = -0.06
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
    base3.pose.position.x = -0.051961524227
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
    arrow1.points[0] = Point(0.051961524227, 0.0, 0.0)
    arrow1.points[1] = Point(0.051961524227, 0.0, 0.08)
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
    arrow2.points[0] = Point(-0.051961524227, -0.06, 0.0)
    arrow2.points[1] = Point(-0.051961524227, -0.06, 0.08)
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
    arrow3.points[0] = Point(-0.051961524227, 0.06, 0.0)
    arrow3.points[1] = Point(-0.051961524227, 0.06, 0.08)
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
    arrow4.points[0] = Point(0.051961524227, 0.0, 0.08)
    arrow4.points[1] = Point(0.051961524227, 0.0, 0.2)
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
    arrow5.points[0] = Point(-0.051961524227, -0.06, 0.08)
    arrow5.points[1] = Point(-0.051961524227, -0.06, 0.2)
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
    arrow6.points[0] = Point(-0.051961524227, 0.06, 0.08)
    arrow6.points[1] = Point(-0.051961524227, 0.06, 0.2)
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
    floor.pose.orientation.w = 1.0
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

def set_initial_delta_pose(markerArray):
    print "Setting initial pose"
    endpoint = Point(0.0, 0.0, 0.150286912)
    for m in markerArray.markers:
        if m.id == 4: # from dyn1 to elbow1
            m.points[1] = Point(0.051961524227 + 0.08, 0.0, 0.0)
        elif m.id == 5: # from dyn2 to elbow2
            m.points[1] = Point(-0.051961524227 - 0.056568542, -0.06 - 0.056568542, 0.0)
        elif m.id == 6: # from dyn3 to elbow3
            m.points[1] = Point(-0.051961524227 - 0.056568542, 0.06 + 0.056568542, 0.0)
        elif m.id == 7: # from elbow1 to end
            m.points[0] = Point(0.051961524227 + 0.08, 0.0, 0.0)
            m.points[1] = endpoint
        elif m.id == 8: # from elbow2 to end
            m.points[0] = Point(-0.051961524227 - 0.056568542, -0.06 - 0.056568542, 0.0)
            m.points[1] = endpoint
        elif m.id == 9: # from elbow3 to end
            m.points[0] = Point(-0.051961524227 - 0.056568542, 0.06 + 0.056568542, 0.0)
            m.points[1] = endpoint
    return markerArray  
        
        
    