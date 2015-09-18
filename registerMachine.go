// +build linux

package main

import (
	"encoding/hex"
	"encoding/json"
	"log"
	"os"

	"github.com/godbus/dbus"
)

var conn *dbus.Conn

func main() {
	var jmap map[string]interface{}
	json.NewDecoder(os.Stdin).Decode(&jmap)
	pid := jmap["pid"].(float64)
	id := jmap["id"].(string)
	root_directory := jmap["root"].(string)
	name := id

	// ensure id is a hex string at least 32 chars
	passId, err := Validate(id)
	if err != nil {
		log.Fatalf(err.Error())
	}

	if os.Args[0] ==  "prestart" {
		if err = RegisterMachine(name, passId, int(pid), root_directory); err != nil {
			log.Fatalf("Register machine failed: %v", err)
		}
	}

	if os.Args[0] == "poststop" {
		if err := TerminateMachine(name); err != nil {
			log.Fatalf("TerminateMachine failed: %v", err)
		}
	}
}

func Validate(id string) (string, error) {
	for len(id) < 32 {
		id += "0"
	}
	return hex.EncodeToString([]byte(id)), nil
}

// RegisterMachine with systemd on the host system
func RegisterMachine(name string, id string, pid int, root_directory string) error {
	var (
		av  []byte
		err error
	)
	if conn == nil {
		conn, err = dbus.SystemBus()
		if err != nil {
			return err
		}
	}

	av, err = hex.DecodeString(id[0:32])
	if err != nil {
		return err
	}
	obj := conn.Object("org.freedesktop.machine1", "/org/freedesktop/machine1")
	return obj.Call("org.freedesktop.machine1.Manager.RegisterMachine", 0, name, av, "runc.service", "container", uint32(pid), root_directory).Err
	return nil
}

// TerminateMachine registered with systemd on the host system
func TerminateMachine(name string) error {
	var err error
	if conn == nil {
		conn, err = dbus.SystemBus()
		if err != nil {
			return err
		}
	}
	obj := conn.Object("org.freedesktop.machine1", "/org/freedesktop/machine1")
	return obj.Call("org.freedesktop.machine1.Manager.TerminateMachine", 0, name).Err
	return nil
}
