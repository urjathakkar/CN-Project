import socket
import threading
import os

l=[]
def RetrFile(name, sock):
    flag=0
    lof=''
    username=sock.recv(1024)
    print(username)
    password=sock.recv(1024)
    if(username.decode()=='E' and password.decode()=='123'):
        path = "/Users/yaagniraolji/Downloads"
        dirs = os.listdir( path )
        for file in dirs:
            print("EMPLOYEE")
            lof=lof+file+"\n"
            l.append(file)
        print(lof)
        sock.send(lof.encode())
    elif(username=='M' and password=='456'):
        print("MANAGER")
        path = "/Users/yaagniraolji/Documents"
        dirs = os.listdir(path)
        for file in dirs:
            lof=lof+file+"\n"
            print (file)
            l.append(file)
        sock.send(lof.encode())
    else:
        print("NOT ACCESSIBLE!")
    filename = sock.recv(1024)
    filename=filename.decode()
    print(filename)
    if os.path.isfile(filename):
        for f in l:
            if f==filename:
                 print("Exists")
                 sock.send(("EXISTS " + str(os.path.getsize(filename))).encode())
                 flag=1
                 #filesize = data[6:]
                 userResponse = sock.recv(1024)
                 userResponse = userResponse.decode()
                 if userResponse[:2] == 'OK':
                      with open(filename, 'rb') as f:
                           bytesToSend = f.read(1024)
                           sock.send(bytesToSend)
                           while bytesToSend != "":
                                bytesToSend = f.read(1024)
                                sock.send(bytesToSend)
                 else:
                    sock.send("ERR".encode())
    if flag==0:
         print("file not found")
    sock.close()

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print ("Server Started.")
while True:
   c, addr = s.accept()
   print ("client connedted ip:<" + str(addr) + ">")
   t = threading.Thread(target=RetrFile, args=("RetrThread", c))
   t.start()

s.close()
