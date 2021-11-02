import socket

# HOST = '127.0.0.1'
HOST = '0.0.0.0'
PORT = 9999

# AF_INET: 소켓 생성시 사용되는 인자 도메인 중 주소체계 인자 값 중 하나. IPv4 프로토콜 체계를 사용하도록함
# SOCK_STREAM: TCP 소켓을 할당할 때 사용되는 인자 값
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOL_SOCKET: setsockopt 옵션의 종류. 보통 SOL_SOCKET와 IPPROTO_TCP 중 하나를 사용함
# SO_REUSEADDR: 이미 사용된 주소를 재사용 하도록 함
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind(): 서버 소켓 바인딩
server_socket.bind((HOST, PORT))
# listen: 클라이언트 연결 요청 대기
server_socket.listen()
# accept: 클라이언트 연결 수립
client_socket, addr = server_socket.accept()
print('Connected by', addr)

while True:
    # receive
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received from", addr, data.decode())
    # send
    client_socket.sendall(data)

client_socket.close()
server_socket.close()


