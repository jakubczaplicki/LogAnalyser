import os, sys
import struct

fname = 'BM2v1Records'
f = open(fname, 'r')
fhex = []
try:
    byte = f.read(1)
    while byte != "":
        fhex.append(byte.encode("hex"))
        byte = f.read(1)
finally:
    f.close()

# Get only the most recent result
fps = fhex[0] + fhex[1] + fhex[2] + fhex[3] 
print struct.unpack('!f', fps.decode('hex'))[0]
