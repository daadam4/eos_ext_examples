package main

import (
	"fmt"
	"github.com/aristanetworks/goeapi"
)

func main() {
	node, err := goeapi.ConnectTo("dut")
	if err != nil {
		fmt.Println(err)
		return
	}

	// Configure interface Ethernet1
	conf_commands := []string{
		"configure",
		"interface Ethernet1",
		"description Configured by Arista Go script",
		"no shutdown",
	}
	// Run the commands against the dut
	_, err = node.RunCommands(conf_commands, "text")
	if err != nil {
		fmt.Println(err)
		return
	}

	validate := []string{"show running-config interfaces Ethernet1"}

	result, err := node.Enable(validate)
	if err != nil {
		panic(err)
	}

	for _, m := range result {
		for k, v := range m {
			fmt.Printf("%s:\n%s\n", k, v)
		}
	}
}
