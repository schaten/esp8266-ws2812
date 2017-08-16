#!/bin/python3
from strip import Strip
import time
import math
import sys

IP="192.168.178.110"
PORT=3000
LENGTH=15

distribution=1
brightness=100
if len(sys.argv)>1:
    brightness=int(sys.argv[1])
if len(sys.argv)>2:
    distribution = int(sys.argv[2])
s=Strip(LENGTH,IP,PORT)
def rgbow(p):
    return [dist(p+0.5)+dist(p-0.5),dist(p+1/6), dist(p-1/6)]

def dist(x):
    return dists[distribution](x)

#how to distribute colours
def dExp(x):
    if(0<=x and x<=1):
        return math.exp(-40*(x-0.5)**2)
    else:
        return 0
def dLin(x):
    if(0<=x and x<=1):
        return mabs(x-0.5,1,4);
    else:
        return 0
def mabs(x, height, slope):
    if x>0:
        a=height-x*slope;
    else:
        a= height+x*slope;
    if a>0:
        return a
    else:
        return 0
dists=[dExp, dLin]

def color(start):
    for i in range(15):
        if(i-start)<0:
            v=rgbow((15+(i-start))/15)
        else:
            v=rgbow((i-start)/15)
        s.set(i,*list(map(lambda x: int(x*brightness), v)))


start=0;
s.show()
while True:
    color(start);
    s.show();
    start+=0.32;
    start=start%15
    time.sleep(0.04)
