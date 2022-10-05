import os
from datetime import datetime


def seg_main():
    now = datetime.now()
 
    newpath = f'output/segmentation-{now}' 

    imagedata = newpath+'/imageData.json'
    output = newpath+'/output.out'



    if not os.path.exists(newpath):
        os.makedirs(newpath)

        # IMAGE DATA
    try:
        file = open(imagedata, 'r')
    except FileNotFoundError:
        file = open(imagedata, 'w')

        # OUTPUT DATA
    try:
        file = open(output, 'r')
    except FileNotFoundError:
        file = open(output, 'w')