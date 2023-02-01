#!/usr/bin/env python3

# This script builds on the int_conf_multi.py script by adding all ATD hosts, using lldp output,
# and configuring multiple interfaces. The comments there provide building blocks for this code

import pyeapi
import time

# List of that we will connect to and run commands against
hosts = ['192.168.0.10','192.168.0.11','192.168.0.12','192.168.0.13','192.168.0.14','192.168.0.15','192.168.0.16','192.168.0.17','192.168.0.20','192.168.0.21',
         '192.168.0.22','192.168.0.23','192.168.0.24','192.168.0.25','192.168.0.26','192.168.0.27','192.168.0.100','192.168.0.101','192.168.0.102','192.168.0.103',
         '192.168.0.200','192.168.0.201','192.168.0.202','192.168.0.203']

print('Please wait while the interfaces are configured...\n')

time.sleep(6)

print('Example: The following is output for s2-core2.atd.lab\n')
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
        
        if ip_address == hosts[-1]:

            validation = [
                f'show running-config interfaces {port}'
            ]
            result = node.run_commands(validation, encoding='text')
            
            for element in result:
                for _, m in element.items():
                    print(f"command: {validation[0]}\noutput:\n{m}")
        else:
            continue
