#coding:utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('172.0.0.1',9999))

print('-->>'+s.recv(1024).decode('utf-8'))

s.send(b'Hello,I am client')

print('-->>'+s.recv(1024).decode('utf-8'))

s.send(b'exit')


s.close()


