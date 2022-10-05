import os

newpath = 'output' 

imagedata = newpath+'/imageData.json'
nikon_raw = newpath+'/Nikon-D4-Shotkit.raw'

def root_main():


    try:
        file = open(imagedata, 'r')
    except FileNotFoundError:
        file = open(imagedata, 'w')

        # OUTPUT DATA
    try:
        file = open(nikon_raw, 'r')
    except FileNotFoundError:
        file = open(nikon_raw, 'w')