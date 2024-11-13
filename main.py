import sys
import socket
import threading
from queue import Queue

def TCP_connect(ip, port_number, delay, output_queue):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output_queue.put(f'{port_number}: Listening')
    except:
        pass

def scan_ports(ip, delay):
    threads = []
    output_queue = Queue()

    print("Scanning ports...")

    for i in range(1, 10001):
        t = threading.Thread(target=TCP_connect, args=(ip, i, delay, output_queue))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results = []
    while not output_queue.empty():
        result = output_queue.get()
        if result:
            results.append(result)

    if results:
        print("\nThe following ports are open:")
        print("\n".join(results))
    else:
        print("No open ports found.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <ip_address> <timeout_in_seconds>")
        sys.exit(1)

    ip = sys.argv[1]
    delay = int(sys.argv[2])
    scan_ports(ip, delay)

if __name__ == "__main__":
    main()
