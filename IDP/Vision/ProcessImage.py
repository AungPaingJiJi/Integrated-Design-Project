# Importing necessary packages
import numpy as np
import cv2

# ProcessImage Class for preprocessing images
# using computer vision techniques
class ProcessImage(object):
    
    '''return a crop image for the region_of_interest   
    Boundry value will need to be decided by the user
    '''    
    def region_of_interest(img,boundry=np.array([[]])):
        mask = np.zeros_like(img)
        cv2.fillPoly(mask,boundry,255)
        masked_image = cv2.bitwise_and(mask,img)
        return masked_image
    
    '''return a warp(perspective change view of the image)
    The src and dest should be in the format of np.float32()'''
    def warp(img ,src,dest):
        M = cv2.getPerspectiveTransform(src,dest)
        warped= cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
        return warped

