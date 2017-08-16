import socket

class Strip:
    def __init__(self, l, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.target = (ip, port)
        self.leds=[[0,0,0] for a in range(l)]
        self.length=l
        self.prev=[[0,0,0] for a in range(l)]
        self.diff=False
        self.age=0
        self.mes=""
    def set(self, led, r,g,b):
        self.leds[led]=[r,g,b]
    def show(self):
        self.encode();
        for (i,x) in enumerate(self.leds):
            for j in range(3):
                self.prev[i][j]=self.leds[i][j]
        self.send();
    def encode(self):
        self.mes="";
        if(not self.diff):
            for led in self.leds:
                for color in led:
                    if not (0<=color and color<=254):
                        color=254
                    self.mes+=chr(color+1)
            self.mes+="\0\0"
#            print("uncompressed")
            self.age=0
        else:
            if self.age>20:
#                print("age!")
                self.diff=False
                self.encode()
            diff={};
            count=0;
            flow=False;
            begin=0;
            for (i,x) in enumerate(self.leds):
                if x!=self.prev[i]:
                    if(not flow):
                        diff[i]=x;
                        begin=i
                        flow=True;
                        count+=1
                    else:
                        diff[begin]+=x;
                else:
                    flow=False
            if(count*2<=self.length):
                for led in diff:
                    color=diff[led]
                    self.mes+="\0#"+chr(led+1)+"\0"
#                    print(str(led)+":")
                    for value in color:
                        self.mes+=chr(value+1)
#                       print(value)
                self.mes+="\0\0"
#                print("compressed!")
                self.age+=1
            else:
                self.diff=False
                self.encode();
    def send(self):
        self.sock.sendto(self.mes.encode('latin-1'),self.target)
        self.diff=True
        #print(self.mes.encode('latin-1'))
