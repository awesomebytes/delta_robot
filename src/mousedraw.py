#!/usr/bin/env python

import numpy as np
import cv2
import cv

#http://blog.damiles.com/2008/11/basic-painter-in-opencv/
#event is a constant that give this values and define the mouse event:
#define CV_EVENT_MOUSEMOVE      0
#define CV_EVENT_LBUTTONDOWN    1
#define CV_EVENT_RBUTTONDOWN    2
#define CV_EVENT_MBUTTONDOWN    3
#define CV_EVENT_LBUTTONUP      4
#define CV_EVENT_RBUTTONUP      5
#define CV_EVENT_MBUTTONUP      6
#define CV_EVENT_LBUTTONDBLCLK  7
#define CV_EVENT_RBUTTONDBLCLK  8
#define CV_EVENT_MBUTTONDBLCLK  9

#x, y: integer mouse position in our image

#flag is another constant value:
#define CV_EVENT_FLAG_LBUTTON   1
#define CV_EVENT_FLAG_RBUTTON   2
#define CV_EVENT_FLAG_MBUTTON   4
#define CV_EVENT_FLAG_CTRLKEY   8
#define CV_EVENT_FLAG_SHIFTKEY  16
#define CV_EVENT_FLAG_ALTKEY    32


class MouseDraw(object):
    def __init__(self):
        cv2.namedWindow('CaptureMouse')
        cv.MoveWindow('CaptureMouse', 0, 0)
        cv2.setMouseCallback('CaptureMouse', self.onmouse)
        self.drag_start = False
        self.image = cv.LoadImageM("blank_800x800.jpg")
        self.pointlist = []
        
    def onmouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE and self.drag_start:
            print "Moving mouse!"
            x, y = np.int16([x, y]) # BUG
            print "( %d, %d) " % (x, y)
            self.pointlist.append((x,y))
        if event == cv2.EVENT_LBUTTONDOWN:
            print " buttondown!"
            print len(self.pointlist)
            if len(self.pointlist) > 0:
                self.pointlist = []
                self.image = cv.LoadImageM("blank_800x800.jpg")
            self.drag_start = True
            self.pointlist.append((x,y))
        if self.drag_start and event == cv2.EVENT_LBUTTONUP: 
            print " buttonup!"
            self.drag_start = False
            self.pointlist.append((x,y))

    def run(self):
        while True:
            #print self.pointlist
            for i in range(0,len(self.pointlist)-1):
                #print self.pointlist[i]
                cv.Circle(self.image, self.pointlist[i], 1, (0, 0, 255))
                
            cv.ShowImage('CaptureMouse', self.image)

            ch = cv2.waitKey(30)
            if ch == 27 or ch == 1310819 or ch == 1048603:
                f = open('drawingpointlist.txt', 'w')
                for i in range(0, len(self.pointlist)):
                    f.write("" + str(self.pointlist[i][0]) + ","  + str(self.pointlist[i][1]) + "\n")
                f.close()
                cv.SaveImage('drawingimage.jpg',self.image)
                break
                

if __name__ == '__main__':
    import sys
    MouseDraw().run()
