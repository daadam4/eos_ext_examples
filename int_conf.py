#!/usr/bin/env python3
import pyeapi

# Connect to the Arista EOS device
node = pyeapi.client.connect(host='192.168.0.102', username='arista', password='password', transport='https', return_node=True)

# Configure interface Ethernet1
commands = [
    'interface Ethernet1',
    'description Configured by Arista Python script',
    'no shutdown',
]

node.config(commands)

validate = [
    'show running-config interfaces Ethernet1'
]

result = node.run_commands(validate, encoding='text')

for element in result:
    for _, m in element.items():
        print(f"command:\n{validate[0]}\nresult:\n{m}")