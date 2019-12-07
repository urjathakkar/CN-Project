import socket
import os


l=[]
host = '127.0.0.1'
port = 5000
flag=0
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

username=input("enter username:")
s.send(username.encode())
password=input("enter password: ")
s.send(password.encode())

files=s.recv(1024)
print(files.decode())
filename = input("Filename? -> ")
s.send(filename.encode())

data = s.recv(1024)
data = data.decode()
print(data)
if data[:6] == 'EXISTS':
     print(data[6:])
     filesize = float(data[6:])
     message = input("File exists, " +"Bytes, download? (Y/N)? -> ")
     if message == 'Y':
          s.send(("OK").encode())
          f = open('new_'+filename, 'wb')
          data = s.recv(1024)
          totalRecv = len(data)
          f.write(data)
          while totalRecv < filesize:
              data = s.recv(1024)
              totalRecv += len(data)
              f.write(data)
              print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
          print ("Download Complete!")
          flag=1
     f.close()
if flag==0:
     print("file not found")
s.close()
