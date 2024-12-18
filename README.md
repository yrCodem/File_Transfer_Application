# Client-Server File Transfer Implementation
Overview
This project demonstrates a basic client-server file transfer implementation using Python. The server listens for incoming connections, and the client initiates a connection to request a specific file. The server checks if the file exists, sends its size, and then transfers the file in chunks.
Getting Started
## Prerequisites

    Python 3.x installed on your system

## Running the Application

    Create a file named "example.txt" in the same directory as the server script.
    Run the server script on one terminal using python server.py.
```bash
    python server.py
 ```
    Run the client script on another terminal using python client.py.
```bash
python client.py
```

The client will request "example.txt" from the server, and if the file exists, it will be transferred and saved as "received_example.txt" in the client's directory.
Implementation Details

    The server listens for incoming connections on localhost.
    The client initiates a connection and requests a specific file.
    The server checks if the file exists, sends its size, and then transfers the file in chunks.
    The client receives the file size, creates a new file, and receives the data in chunks until the entire file is transferred.

Limitations

    This is a basic implementation and doesn't include error handling, security measures, or support for multiple simultaneous connections.
    In a production environment, you'd want to add these features and possibly use higher-level libraries or frameworks for more robust file transfer capabilities.
