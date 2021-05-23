import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import math
import numpy as np
import PIL
import random as rng


image_path = r"C:\Users\User\Desktop\22979050_15.tiff" # original satellite image
result_path = r"C:\Users\User\Desktop\output.jpg" # result of committing AI model
output_path = r"C:\Users\User\Desktop\proposal\output.jpg" # path that save jpg file converted from tiff
scale = 1000 # int, this map suppose the scale is 1:1000
desired_area = 10000 # int, How much area the Custermer want to build fire station


