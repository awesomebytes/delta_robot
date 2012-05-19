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
        cv2.setMouseCallback('CaptureMouse', self.onmouse)
        self.drag_start = False
        self.image = cv.LoadImageM("lena.jpg")

    def onmouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE and self.drag_start:
            print "Moving mouse!"
            x, y = np.int16([x, y]) # BUG
            print "( %d, %d) " % (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            print " buttondown!"
            self.drag_start = True
        if self.drag_start and event == cv2.EVENT_LBUTTONUP: 
            print " buttonup!"
            self.drag_start = False

    def run(self):
        while True:
            cv.ShowImage('CaptureMouse', self.image)

            ch = cv2.waitKey(30)
            if ch == 27 or ch == 1310819:
                break

if __name__ == '__main__':
    import sys
    MouseDraw().run()
