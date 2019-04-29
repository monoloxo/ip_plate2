import cv2
from hyperlpr import *
import time
from time import sleep

import socket
c=1
timeF = 20
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#frames=[]
#cap = cv2.VideoCapture('rtsp://192.168.199.22/stream2')#/dev/video0')#args.src)
cap1 = cv2.VideoCapture('rtsp://admin:admin123@192.168.199.67:554/cam/realmonitor?channel=4&subtype=0&unicast=true&proto=Onvif')
#cap2 = cv2.VideoCapture('rtsp://admin:admin123@192.168.199.67:554/cam/realmonitor?#channel=2&subtype=0&unicast=true&proto=Onvif')
while True:
    has_frame1, frame1 = cap1.read()
    #has_frame2, frame2 = cap2.read()
    #frames.append(frame)
    #cv2.imshow('video',frame)
    #out = HyperLPR_PlateRecogntion(frame)
    #print(out)
    #if cv2.waitKey(1000) ==27:
    #cv2.waitKey(100000)
    if (c%timeF==1):
        out1 = HyperLPR_PlateRecogntion(frame1)
        #out2 = HyperLPR_PlateRecogntion(frame2)
        if len(out1)>0:#,len(out2)
            if len(out1[0])>0:#,len(out2[0])
                if (out1[0][1])>0.96:#,(out2[0][1])
                    if (len(out1[0][0]))==7 or 8:#,(len(out2[0][0]))

                        #print('id1'+out1[0][0])
                        #print('id2'+out2[0][0])
                        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        #print ("本地时间为 :", localtime)
                        #rts = rtsp[65:67]
                        #if rtsp[66]=='&':
                            #rts = rtsp[65]
            
                        data = 'id4',out1,localtime
                        #data = str('id'+rtsp[65]+str(out)+str(localtime))
                        #print(data)
                        data2 = str(data)
                        s.sendto(data2.encode(),('192.168.199.237',1717))#78,1712
                        print(data2)
                        #print(s.recv(1024))
                        s.close
    c = c+1
    #cv2.waitKey(1)
    #break
   
