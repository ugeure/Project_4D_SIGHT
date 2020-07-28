# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:35:10 2020

@author: ugur-ilhan
"""

import cv2
import numpy as np
star_map = cv2.imread("StarMap.png")
start_map = cv2.imread("StarMap.png",0)
small_area = cv2.imread("Small_area.png",0)
small_area_rotated = cv2.imread("Small_area_rotated.png",0)


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)

  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

w, h = small_area.shape[::-1]
i=0
while(i<360):
    
    res = cv2.matchTemplate(start_map,rotate_image(small_area_rotated,i),cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(star_map, pt, (pt[0] + w, pt[1] + h), (0,0,255), 3)
        cv2.imwrite('output.png',star_map)
    i+=1


