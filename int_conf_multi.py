#!/usr/bin/env python3

# This script builds on the int_conf.py script by adding multiple hosts and
# Multiple interfaces. the comments there provide building blocks for this code
import pyeapi

# Create a list of hosts which we will loop through
hosts = ["192.168.0.101", "192.168.0.102"]

# For every item in the hosts list above execute every subsequent line
for ip_address in hosts:
    
    # Connect to the EOS device
    node = pyeapi.client.connect(host=ip_address, username='arista', password='password', transport='https', return_node=True)

    # For every number in the range, do the following
    for interface in range(1,49):
        
        # Same code as int_conf.py except we use a variable input for the interface
        commands = [
        f'interface Ethernet{interface}',
        'description Configured by Arista Python script',
        'no shutdown',
        ]

        node.config(commands)

    # All the same as int_conf.py
    validate = [
        'show running-config interfaces Ethernet1'
    ]

    result = node.run_commands(validate, encoding='text')

    for element in result:
        for _, m in element.items():
            print(f"node: {ip_address}\ncommand: {validate[0]}\noutput:\n{m}")
