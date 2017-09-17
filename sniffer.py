#-*- coding: utf-8 -*-
'''
Created on 2017. 1. 5.

@author: P005271
'''
import socket

host = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 3)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

logfile = open('capture.log', 'w')

while True:
    data = s.recvfrom(10000)
    
    # data[1][0]은 source이므로, 곧 나가는 패킷만 가로채겠다는 의미
    if data[1][0] == host:
        try:
            fragment = data[0][40:].decode('utf-8')
            print(fragment + '\n' + '*' * 100)
        except:
            pass