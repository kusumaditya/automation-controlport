import telnetlib



cmd = 'configure terminal'
tn = telnetlib.Telnet(host='10.0.128.2', port=33793, timeout=10)
tn.write(cmd.encode('ascii')+b"\n")
Output = tn.read_very_lazy()
OC = Output.decode('UTF-8')
print(OC)
print(Output)