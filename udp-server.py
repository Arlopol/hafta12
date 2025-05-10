import socket

localIP = socket.gethostname()
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Simulated database
di = {
    'omer': 'abc',
    '17BEC0647': 'shikhar',
    '17BEC0150': 'tanveer',
    '17BCE2119': 'sahil',
    '17BIT0123': 'sidhant'
}

while True:
    # Receive username
    name, addr1 = UDPServerSocket.recvfrom(bufferSize)
    # Receive password
    pwd, addr1 = UDPServerSocket.recvfrom(bufferSize)

    name = name.decode()
    pwd = pwd.decode()

    # Validate credentials
    if name not in di:
        msg = 'name does not exist'
    elif di[name] == pwd:
        msg = 'pwd match'
    else:
        msg = 'pwd wrong'

    # Send response
    UDPServerSocket.sendto(msg.encode(), addr1)
