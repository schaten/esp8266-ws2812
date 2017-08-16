#!/bin/python3
from strip import Strip
import time
import math
import sys

IP="192.168.178.110"
PORT=23
LENGTH=15

mode=0
brightness=100
if len(sys.argv)>1:
    brightness=int(sys.argv[1]);
if len(sys.argv)>2:
    mode=int(sys.argv[2]);

s=Strip(LENGTH,IP,PORT)
def gauss(pos,color):
    for i in range(15):
        v = list(map( lambda x: int(x*brightness*math.exp(-0.5*(i-pos)**2)), color))
        s.set(i,*v)
def rgbow(p):
    return [dist(p+1/3)+dist(p-2/3),dist(p), dist(p-1/3)]
def dist(x):
    if(0<=x and x<=2/3):
        return math.exp(-50*(x-1/3)**2)
    else: return 0
pos=0
back=False
s.show()
count=0;
color=[0,0,0]
if(mode<3):
    color[mode]=1;
while True:
    if(mode==3):
        gauss(pos,rgbow(count/100))
        count+=1;
        count=count%90;
    else:
        gauss(pos,color)
    s.show()
    time.sleep(0.04)
    if(pos<=0): back=False
    if(pos>=14): back=True
    if(back):
        pos-=0.4
    else:
        pos+=0.4

