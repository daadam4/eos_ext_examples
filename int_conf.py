#!/usr/bin/env python3

# import the pyeapi client which is used to communicated with the eAPI
import pyeapi

# Connect to the Arista EOS device using the function connect within the client module
# For more info on pyeapi checkout the docs @ https://pyeapi.readthedocs.io/en/master/client_modules/client.html
node = pyeapi.client.connect(host='192.168.0.102', username='arista', password='password', transport='https', return_node=True)

# Create a list of commands and store it in the variable "commands"
# The variable name "commands" is arbitrary and could be x
# "commands" was used for clarity
commands = [
    'interface Ethernet1',
    'description Configured by Arista Python script',
    'no shutdown',
]

# Usings the config function to pass the commands to the node that we have connected to
# the commands that are being passed are in the list above
node.config(commands)


# At this point Ethernet1 has been configured with the description we passed in
# The following validation checks are in place for the demo and to ensure it worked as expected
# The variable validate here is the same concept as "commands" above
validate = [
    'show running-config interfaces Ethernet1'
]

# We store the output of the validate configurations to "result"
result = node.run_commands(validate, encoding='text')

# Run a for loop to print the output
for element in result:
    for _, m in element.items():
        print(f"command:\n{validate[0]}\nresult:\n{m}")