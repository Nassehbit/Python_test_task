import os

def extra_main():
    newpath = 'output/extra' 

    fn = newpath+'/output.out'

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    try:
        file = open(fn, 'r')
    except FileNotFoundError:
        file = open(fn, 'w')