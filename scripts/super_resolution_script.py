import os
from datetime import datetime


def sup_main():
    now = datetime.now()
    newpath = f'output/superresolution-{now}' 

    imagedata = newpath+'/imageData.json'
    output = newpath+'/output.out'

    progress_out = newpath+'/progress.out'
    properties_json = newpath+'/properties.json'



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

        # progress out
    try:
        file = open(progress_out, 'r')
    except FileNotFoundError:
        file = open(progress_out, 'w')

        # PROPERTIES DATA
    try:
        file = open(properties_json, 'r')
    except FileNotFoundError:
        file = open(properties_json, 'w')