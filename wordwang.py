import socket

def send_tcp_request(host, port, data_list):
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to the server (host and port)
            sock.connect((host, port))
            
            # Send the data in the specified order
            for data in data_list:
                sock.sendall(data.encode())
                response = sock.recv(1024).decode()
                print("Received response from server:", response)

    except socket.error as e:
        print("Error:", e)

if __name__ == "__main__":
    # Replace 'wordwang.challs.olicyber.it' and 10601 with the target host and port respectively
    host = 'wordwang.challs.olicyber.it'
    port = 10601

    # Specify the data in the order you want to send to the server
    data_list = [
        "speech\n",
        "SPEECH\n",
        "spech\n",
        "SPEECH\n",
        "provide\n",
        "one\n",
        "one\n",
        "one\n",
        "one\n",
        "WORDWANG\n",
        "SPEECH?\n",
        "?SPEECH!\n",
    ]

    send_tcp_request(host, port, data_list)

#era molto più stupida di così, bastava fare il nc e vedere dal wireshark cosa mandare, ossia la parola con ! e ? in caps