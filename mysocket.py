import socket

target_host = "10.7.7.238"
target_port = 8008

image = "test.jpg"
def sendImage(i):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client.connect((target_host, target_port))

	try:
		file = open(image, 'rb')
		bimg = file.read()
		size = len(bimg)
		
		client.send(str(size).encode())

		response = client.recv(4096)
		print(response)
		client.sendall(bimg)
		response = client.recv(4096)
		print(response)


	finally:
		client.close()

sendImage(1)
