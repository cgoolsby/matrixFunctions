#!/usr/bin/python
import sys
import numpy as np
#calculate the RMSD between the function and the FE plot
k = 10
def func(x):
  return k / 4 * (x**2 - 1)**2
#from -1.5 to 1.5
MAX = 1.5
MIN = -1.5

for i in range(len(sys.argv)-1):
  file = open(sys.argv[i+1])
  n = 1.0
  diff = 0
  xvalues = []
  values = []

  for line in file.xreadlines():
    ar = line.split()
    if(len(ar)==2 and MAX>=float(ar[0]) and float(ar[0])>=MIN):
      xvalues.append(ar[0])
      values.append(ar[1]) 
      n += 1 
  minim=100000
  for i in range(len(values)):
    if(float(values[i])<minim):
        minim=float(values[i])
  for i in range(len(values)):
    values[i] = float(values[i]) - minim
    expected = func(float(xvalues[i]))
    diff += (expected - float(values[i]))**2

  rmsd = np.sqrt(diff/n)

#  print sys.argv[i+1], "rmsd: ",rmsd
print("%-10s  "%rmsd),
