import socket
import threading
from queue import Queue
import time

# Number of threads to use
N_THREADS = 200

# Lock for synchronizing print statements
print_lock = threading.Lock()

# Cache for service resolution
service_cache = {}

# Examples of known vulnerabilities (illustrative purposes)
vulnerability_db = {
    'vsftpd 2.3.4': 'CVE-2011-2523: Backdoor vulnerability',
    'Apache 2.2.8': 'CVE-2010-1452: Directory traversal vulnerability',
    # Add more known vulnerabilities here
}

def get_service_name(port, protocol):
    """Get the service name for a given port and protocol."""
    if (port, protocol) in service_cache:
        return service_cache[(port, protocol)]
    try:
        service_name = socket.getservbyport(port, protocol)
    except:
        service_name = 'Unknown'
    service_cache[(port, protocol)] = service_name
    return service_name

def banner_grab(sock):
    """Attempt to grab the banner of a service."""
    try:
        # Try various ways to get banner information
        sock.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
        return sock.recv(1024).decode().strip()
    except:
        try:
            sock.sendall(b'HELLO\r\n')
            return sock.recv(1024).decode().strip()
        except:
            return ''

def check_vulnerability(service_info):
    """Check if the service info matches known vulnerabilities."""
    for known_service, vuln_info in vulnerability_db.items():
        if known_service.lower() in service_info.lower():
            return f"Potential Vulnerability: {vuln_info}"
    return "No known vulnerabilities detected."

def scan_port(ip, port):
    """Scan a single port and return a formatted result."""
    result = ""
    
    # Check TCP
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(1)
        tcp_socket.connect((ip, port))
        banner = banner_grab(tcp_socket)
        service_name = get_service_name(port, 'tcp')
        vulnerability_info = check_vulnerability(banner)
        result += f"{port}/tcp   open   {service_name}   {banner}   {vulnerability_info}\n"
        tcp_socket.close()
    except (socket.timeout, ConnectionRefusedError):
        pass

    # Check UDP
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(2)
        udp_socket.sendto(b"Hello", (ip, port))
        data, _ = udp_socket.recvfrom(1024)
        service_name = get_service_name(port, 'udp')
        result += f"{port}/udp   open   {service_name}   {data.decode().strip()}\n"
        udp_socket.close()
    except (socket.timeout, ConnectionRefusedError):
        pass

    return result.strip() if result else None

def worker(ip):
    """Thread worker function to scan ports from the queue."""
    while not q.empty():
        port = q.get()
        result = scan_port(ip, port)
        if result:
            with print_lock:
                print(result)
                results.append(result)
        q.task_done()

def port_scanner(ip, start_port, end_port):
    """Main function to initialize the scanning process."""
    print(f"Starting scan on {ip}...")
    
    # Resolve DNS if possible
    try:
        domain_name = socket.gethostbyaddr(ip)[0]
        print(f"Resolved {ip} to {domain_name}")
    except socket.herror:
        print(f"Could not resolve domain name for {ip}")

    # Prepare the queue
    global q
    global results
    q = Queue()
    results = []
    for port in range(start_port, end_port + 1):
        q.put(port)

    # Start threads
    for _ in range(N_THREADS):
        t = threading.Thread(target=worker, args=(ip,))
        t.daemon = True
        t.start()

    q.join()
    print("Scan complete.")

    # Save results to a file
    with open(f"scan_results_{ip}_{start_port}-{end_port}.txt", 'w') as f:
        for line in results:
            f.write(line + '\n')
    print(f"Results saved to scan_results_{ip}_{start_port}-{end_port}.txt")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    port_range = input("Enter port range (e.g., 1-1024): ").split('-')
    start_port, end_port = int(port_range[0]), int(port_range[1])
    start_time = time.time()
    port_scanner(target_ip, start_port, end_port)
    print(f"Scan completed in {time.time() - start_time:.2f} seconds.")
