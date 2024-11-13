# Port Scanner

A simple port scanner written in Python, designed for educational and authorized security testing purposes. This tool can scan a range of TCP ports and display the open ones.

## Features

- **Multi-threaded Scanning**: Efficient and fast scanning with multi-threading support.
- **Port Scanning**: Scans a range of TCP ports (1-10000 by default).
- **Custom Timeouts**: Configurable timeout for each connection attempt.
- **Result Display**: Lists open ports in a clear format.
- **Simple Usage**: Easy to use from the command line with minimal configuration.

## Installation

To get started, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/C4rbo/port-scanner.git
cd port-scanner
```

This project relies solely on Python's standard libraries, so no additional dependencies are required.

## Usage

Run the provided Bash script to interactively input the target IP address and the timeout value. The Python script will handle the port scanning based on the input from the Bash script.

### Bash Script

```bash
./index.sh
```

This will prompt you to enter the IP address you want to scan and the timeout value for each connection attempt. The script will then call the Python script to perform the port scan.

### Example

```bash
Hey user, insert the IP that you want me to scan: 
192.168.1.1
How many seconds the socket is going to wait until timeout: 
1
Waiting for the scan...

$Result
```

The Python script will scan the ports on the target IP `192.168.1.1` with a timeout of 1 second for each connection attempt, and the open ports will be displayed.

## Legal Disclaimer

**Use responsibly and legally.** This tool is designed for educational purposes and authorized security testing only. Unauthorized scanning of networks and devices is illegal and unethical. Always obtain explicit permission from the network owner before using this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request on GitHub.

## Author

- C4rbo (https://github.com/C4rbo)
