import os.path
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np


with open('test.txt') as f:
    lines=f.readlines()
#    lines = [line.rstrip() for line in f]

for line in lines:
    line=line.rstrip()
    campos=line.split(',')
    directory = campos[0]
    srcview = int(campos[1])
    x_src = int(campos[2])
    y_src = int(campos[3])
    x_target = int(campos[4])
    y_target = int(campos[5])

    
    srcimagename = 'IM'+str(srcview+1).zfill(2)+'-' + directory + '.png'
    targetimagename = directory + '_map.png'

    srcimagename = os.path.join(directory,srcimagename)
    targetimagename = os.path.join(directory,targetimagename)
    print("Dir: ", directory, srcimagename, targetimagename)
    srcimg = imread(srcimagename)
    targetimg = imread(targetimagename)
    

    f, axs = plt.subplots(2, 2)
    axs[0,0].imshow(srcimg)
    axs[1,0].imshow(srcimg)
    axs[1,0].plot(x_src,y_src,'ow')

    axs[0,0].set_title('Source Point')
    axs[0,1].imshow(targetimg)
    axs[1,1].imshow(targetimg)    
    axs[1,1].plot(x_target,y_target,'*w')
    axs[0,1].set_title('FFTMap')
 
    plt.show()
