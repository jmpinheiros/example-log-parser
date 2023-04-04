# Description
Please parse the key=value-style log text in the sample input below, and output its contents in a JSON structure (don’t need to actually create a file containing JSON, a string will do). The solution should be able to handle any number of keys (not just the ones in the sample input) and follow the parsing rules laid out below. The output should be sorted by the id field of each line.

# Parsing Rules
 - You can expect each log entry to be correctly formatted, no unmatched " or keys without values, so there is no need to code defensively.
- Keys contain alphanumeric characters only, no special characters.
- Values can contain any character (including =), but if they contain spaces, they will be wrapped in quotes.
- If a value is wrapped in quotes, quotes within that value are not expected or should be handled. For example, you are NOT expected to parse something like (key="test "value"") or (key="test \"value\"")
- There are no spaces on either side of = in a (key=value) pair.
    Essentially, spaces can only be found between key-value pairs and within quoted values, and equal signs can only be found between keys and values and within quoted values.
- You can use the sample input and/or output to validate and exercise your code.
# Output Requirements
- All keys found in all lines should be uniquely represented in an array called (fields) in the JSON output
- All parsed log line objects should be represented in an array called (lines) in the JSON output, and ordered by the id value of each line object.
- All keys found in all lines should be represented in each object of the lines array in the JSON output. Keys that do not have values for each parsed line should still be present in the object, with a value of null
- The order of the **keys** in each (line) object in the JSON output **does not have to be sorted** and **may vary**.
# Allowances
- You may use any of the available packages to CodeSignal (and for the JSON part, it's highly encouraged).
- The challenge can be developed using any programming language available to CodeSignal.
- You can run your code and use debug/print statements as much as you need. Brownie points for testing using unit tests!
- Researching online for language-specific syntax and library calls is allowed and encouraged, copy-pasting answers from Stack Overflow is not.
- Unless you're **feeling really** confident in your **Regular Expression** abilities (including capture groups), using regex to solve this challenge is fairly complex and generally discouraged (but not disallowed).
- Done is better than perfect.
# Sample Input (in Python)
```
logs = """
timestamp="Tue Feb 22 22:22:01 PDT 2022" id=1 message="Error in NVMe driver" class=kernel subsystem=storage type=error
timestamp="Tue Feb 22 22:22:03 PDT 2022" id=3 message="Network interfaces initialized" class=init subsystem=ip type=info interfaces="lo eth0 eth1"
timestamp="Tue Feb 22 22:22:02 PDT 2022" id=2 message="Error in dbus system" class=init subsystem=dbus type=error socket=/var/run/dbus=1.sock output="Could not access socket"
timestamp="Tue Feb 22 22:22:05 PDT 2022" id=5 message="dnsmasq failed to parse configuration" class=init subsystem=dnsmasq type=error config_path=/etc/dnsmaq/dnsmasq.conf error="Invalid characters encountered in config file"
timestamp="Tue Feb 22 22:22:04 PDT 2022" id=4 message="dnsmasq parsing configuration" class=init subsystem=dnsmasq type=info config_path=/etc/dnsmaq/dnsmasq.conf lines_parsed=41
timestamp="Tue Feb 22 22:22:10 PDT 2022" id=10 message="ufw iptables initializing" class=kernel subsystem=iptables type=info config_path=/etc/ufw/ufw.conf enabled=true
timestamp="Tue Feb 22 22:22:08 PDT 2022" id=8 message="sshd failed to read known hosts file" class=init subsystem=sshd type=warn config_path=/etc/ssh/sshd_known_hosts error="Invalid characters encountered" line=1
timestamp="Tue Feb 22 22:22:11 PDT 2022" id=11 message="ufw iptables initialized with an empty configuration" class=kernel subsystem=iptables type=warn
timestamp="Tue Feb 22 22:22:12 PDT 2022" id=12 message="nodejs simple server failed to start" class=init subsystem=node type=error config_path=/etc/nodejs/simple-server.conf.js error="{'success': false, 'reason':'invalid characters encountered in file (str: xUD)'}"
""".strip()
```
# Sample Output
```
{
 "fields": [
   "type",
   "timestamp",
   "message",
   "interfaces",
   "lines_parsed",
   "subsystem",
   "enabled",
   "config_path",
   "id",
   "class",
   "output",
   "line",
   "error",
   "socket"
 ],
 "lines": [
   {
     "timestamp": "Tue Feb 22 22:22:01 PDT 2022",
     "id": "1",
     "message": "Error in NVMe driver",
     "class": "kernel",
     "subsystem": "storage",
     "type": "error",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "config_path": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:02 PDT 2022",
     "id": "2",
     "message": "Error in dbus system",
     "class": "init",
     "subsystem": "dbus",
     "type": "error",
     "socket": "/var/run/dbus=1.sock",
     "output": "Could not access socket",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "config_path": null,
     "line": null,
     "error": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:03 PDT 2022",
     "id": "3",
     "message": "Network interfaces initialized",
     "class": "init",
     "subsystem": "ip",
     "type": "info",
     "interfaces": "lo eth0 eth1",
     "lines_parsed": null,
     "enabled": null,
     "config_path": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:04 PDT 2022",
     "id": "4",
     "message": "dnsmasq parsing configuration",
     "class": "init",
     "subsystem": "dnsmasq",
     "type": "info",
     "config_path": "/etc/dnsmaq/dnsmasq.conf",
     "lines_parsed": "41",
     "interfaces": null,
     "enabled": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:05 PDT 2022",
     "id": "5",
     "message": "dnsmasq failed to parse configuration",
     "class": "init",
     "subsystem": "dnsmasq",
     "type": "error",
     "config_path": "/etc/dnsmaq/dnsmasq.conf",
     "error": "Invalid characters encountered in config file",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "output": null,
     "line": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:08 PDT 2022",
     "id": "8",
     "message": "sshd failed to read known hosts file",
     "class": "init",
     "subsystem": "sshd",
     "type": "warn",
     "config_path": "/etc/ssh/sshd_known_hosts",
     "error": "Invalid characters encountered",
     "line": "1",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "output": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:10 PDT 2022",
     "id": "10",
     "message": "ufw iptables initializing",
     "class": "kernel",
     "subsystem": "iptables",
     "type": "info",
     "config_path": "/etc/ufw/ufw.conf",
     "enabled": "true",
     "interfaces": null,
     "lines_parsed": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:11 PDT 2022",
     "id": "11",
     "message": "ufw iptables initialized with an empty configuration",
     "class": "kernel",
     "subsystem": "iptables",
     "type": "warn",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "config_path": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:12 PDT 2022",
     "id": "12",
     "message": "nodejs simple server failed to start",
     "class": "init",
     "subsystem": "node",
     "type": "error",
     "config_path": "/etc/nodejs/simple-server.conf.js",
     "error": "{'success': false, 'reason':'invalid characters encountered in file (str: xUD)'}",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "output": null,
     "line": null,
     "socket": null
   },
   {
     "timestamp": "Tue Feb 22 22:22:12 PDT 2022",
     "id": "12",
     "message": "nodejs simple server failed to start",
     "class": "init",
     "subsystem": "node",
     "type": "error",
     "interfaces": null,
     "lines_parsed": null,
     "enabled": null,
     "config_path": null,
     "output": null,
     "line": null,
     "error": null,
     "socket": null
   }
 ]
}
```
