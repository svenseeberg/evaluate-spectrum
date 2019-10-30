#!/usr/bin/env python
 
from __future__ import with_statement
from PIL import Image
import sys
 
im = Image.open(sys.argv[1]) #relative path to file
 
#load the pixel info
pix = im.load()
 
#get a tuple of the x and y dimensions of the image
width, height = im.size
print(width, height)
 
#open a file to write the pixel data
with open(sys.argv[1]+'.csv', 'w+') as f:
  f.write('AVG R,AVG G,AVG B,SUM\n')
 
  #iterate through the x axis
  for x in range(width):
    #iterate through the y axis and sum rgb values:
    r = 0
    b = 0
    g = 0
    for y in range(height):
      r = r + pix[x,y][0]
      g = g + pix[x,y][1]
      b = b + pix[x,y][2]
    #calculate average brightness
    r = r / height
    g = g / height
    b = b / height
    print(x,(r,g,b))
    f.write('{0},{1},{2},{3}\n'.format(r,g,b,sum([r,g,b]))
