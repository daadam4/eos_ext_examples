import pyeapi

# Connect to the Arista EOS device
node = pyeapi.client.connect(host='192.168.0.102', username='arista', password='password', transport='http', return_node=True)

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

for line in str(result).split():
    print(line)
