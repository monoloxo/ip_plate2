#!/home/mf/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os
#import Smail
#import time

for i in range(1,2):
    
    process = "/home/mf/yolo2019/ip_plate2/id%d.lock" % i
    os.system("ps -ef|grep id%d.py|grep -v grep >%s" % (i,process))
    if not(os.path.getsize(process)):
        os.system("python /home/mf/yolo2019/ip_plate2/id%d.py &" % i)
        
