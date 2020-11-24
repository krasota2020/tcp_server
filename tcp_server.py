import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 6000
BUFFER_SIZE = 1024

w,h = 900, 900
IMAGE_SIZE = w*h

PARTS_COUNT = int(IMAGE_SIZE / BUFFER_SIZE)
LAST_BUFFER = IMAGE_SIZE - PARTS_COUNT*BUFFER_SIZE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen(10)

print ('');
print ('-----------------------------------------');
print ('Starting Server: '+SERVER_ADDRESS+':'+str(SERVER_PORT))
print ('-----------------------------------------');
print ('Parts count - '+str(PARTS_COUNT));
print ('Image size - '+str(w)+'x'+str(h)+' - '+str(IMAGE_SIZE)+' байт.')
print ('LastBuffer - '+str(LAST_BUFFER));

def recvall(sock,count):
    buf=b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return b'#0'
        buf += newbuf
        count -= len(newbuf)
    return buf

while True:
    
    conn, addr = server.accept()
    print ("Client connected from: ", addr)
    receive = False

    while conn:

        
 
        start = conn.recv(4)
        if not start:
            break
        size = int.from_bytes(start, byteorder='little')
              

        if size == IMAGE_SIZE:
            

            data = b''
            output = b''
            data = recvall(conn,IMAGE_SIZE)
            if not data:
                break

            if data !=b'#0':
                output+=data
            

            if len(output) == IMAGE_SIZE:
                try:
                  print("RECEIVED")
                except:
                    pass

    conn.close()
    print ("Client disconnected: ", addr)
