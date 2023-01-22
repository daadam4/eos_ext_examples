#!/usr/bin/env python3
import pyeapi

# List of that we will connect to and run commands against
hosts = ['192.168.0.10','192.168.0.11','192.168.0.12','192.168.0.13','192.168.0.14','192.168.0.15','192.168.0.16','192.168.0.17','192.168.0.20','192.168.0.21',
         '192.168.0.22','192.168.0.23','192.168.0.24','192.168.0.25','192.168.0.26','192.168.0.27','192.168.0.100','192.168.0.101','192.168.0.102','192.168.0.103',
         '192.168.0.200','192.168.0.201','192.168.0.202','192.168.0.203']

for ip_address in hosts:
    # For every item in list, do X or in our case for IP address in host list, connect to the Arista EOS device
    # Pass pyeapi client the connection parameters
    node = pyeapi.client.connect(host=ip_address, username='arista', password='password', transport='https', return_node=True)

    show_commands = [
        'show lldp neighbors',
    ]

    # Store the output of the 'show lldp neighbors detail' command to the variable lldp_neighbors_sum
    lldp_neighbors_sum = node.enable(show_commands)

    # JSON response parsing just for brevity
    parsed_result = lldp_neighbors_sum[0]["result"]["lldpNeighbors"]

    # Finally for every interface on every host use the lldp neighbor information to configure the interface
    for interface in range(len(parsed_result)):
        port = parsed_result[interface]["port"]
        neighborDevice = parsed_result[interface]["neighborDevice"]
        neighborPort = parsed_result[interface]["neighborPort"]
        
        configure_commands = [
            f'interface {port}',
            f'description Connected to {neighborDevice} on remote port {neighborPort}',
            'no shutdown',
            ]
            
        node.config(configure_commands)
        