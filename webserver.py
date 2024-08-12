from socket import *


def creatserver():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while (1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            data = "HTTP/1.1 200 ok\r\n"
            data += "content-type: text.html: charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>hello world</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)


print("Access http://localhost:9000")
creatserver()
