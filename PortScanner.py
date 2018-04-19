# Port Checker/Scanner that checks a number of different ports

import socket

def check_port(address, port):
    try:
        # Connect a TCP Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the Timeout to 5, so we don't hang on connection attempt
        s.settimeout(2)
        
        # Get the name of the port/service we are testing
        try:
            service = socket.getservbyport(port)
        except:
            print "Cannot find service name"
            return
        
        # Attempt to connect to the port
        check = s.connect_ex((address, port))
        # If our check passed, print the port and service
        if check == 0:
            print "Port: %d => service %s" %(port, service)
        
        # Finally close our socket
        s.close()
    
    except socket.error, err_msg:
        print "%s: %s" %(address, err_msg)
    
def check_ports(address):
    # Ports we are checking
    ports = [21, 22, 23, 25, 80, 110, 119, 443]
    
    # Check the ports
    for i in range(0, len(ports)):
        check_port(address, ports[i])


if __name__ == '__main__':
    print "Starting Port Scanner"
    
    # Check local host loopback
    check_ports('127.0.0.1')
    
    # Check remote host: google
    #check_ports(socket.gethostbyname('www.google.org'))

    print "Finished Port Scanner"