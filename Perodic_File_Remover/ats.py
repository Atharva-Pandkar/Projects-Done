from sys import *
import os
import hashlib

def hashfile(path,blocksize =1024):
 fd = open(path,'rb') #Read Byte Mode
 hasher = hashlib.md5()
 buf = fd.read(blocksize)
 
 while len(buf) >0 :
  hasher.update(buf)
  buf = fd.read(blocksize)
  
  fd.close()
  
  return hasher.hexdigest()

