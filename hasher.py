import hashlib
import os

def qgb(path):
    f=open(path,'rb');d=f.read();f.close();return d

def quick(data):
    h = hashlib.sha512()
    h.update(data)
    return h.hexdigest()