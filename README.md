
# Port Scanner

An port scanner written in Python, designed for educational and authorized security testing purposes. This tool can scan both TCP and UDP ports, identify services, and check for known vulnerabilities using service banners.

## Features

- **Multi-threaded Scanning**: Efficient and fast scanning with multi-threading support.
- **Extended Banner Grabbing**: Uses multiple methods to grab banners for more accurate service detection.
- **Service Identification**: Identifies services running on open ports using standard ports and protocol data.
- **Vulnerability Detection**: Checks for potential vulnerabilities based on service version banners.
- **Custom Timeouts**: Separate configurable timeouts for TCP and UDP scans.
- **DNS Resolution**: Resolves IP addresses to domain names when available.
- **Result Saving**: Saves scan results to a text file for further analysis.

## Installation

To get started, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/advanced-port-scanner.git
cd advanced-port-scanner
```

This project relies solely on Python's standard libraries, so no additional dependencies are required.

## Usage

Run the script using Python 3. You'll be prompted to enter the target IP address and the range of ports you want to scan.

```bash
python scanner.py
```

### Inputs

- **Target IP Address**: The IP address of the machine you want to scan.
- **Port Range**: The range of ports to scan, specified in the format `start-end` (e.g., `1-1024`).

### Example

```
Enter target IP address: 192.168.1.1
Enter port range (e.g., 1-1024): 20-80
```

The script will output the status of each port, including whether it is open, the service name (if identifiable), any banner information, and known vulnerabilities related to the service. Results will also be saved to a file named `scan_results_<ip>_<start_port>-<end_port>.txt`.

## Legal Disclaimer

**Use responsibly and legally.** This tool is designed for educational purposes and authorized security testing only. Unauthorized scanning of networks and devices is illegal and unethical. Always obtain explicit permission from the network owner before using this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request on GitHub.

## Author

- C4rbo (https://github.com/C4rbo)
