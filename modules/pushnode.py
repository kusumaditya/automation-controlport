import telnetlib



def pushtonode(numport):
	scpt_nsh = []
	scpt_conf = []
	scpt_sht = []
	if numport == "1":
		scpt_conf=["interface ethernet 1/1",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/2-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "2":
		scpt_conf=["interface ethernet 1/1-2",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/3-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "3":
		scpt_conf=["interface ethernet 1/1-3",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/4-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "4":
		scpt_conf=["interface ethernet 1/1-4",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/5-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "5":
		scpt_conf=["interface ethernet 1/1-5",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/6-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "6":
		scpt_conf=["interface ethernet 1/1-6",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/7-8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "7":
		scpt_conf=["interface ethernet 1/1-7",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=["interface ethernet 1/8",
						"no channel-group 8",
						"shutdown"]
	elif numport == "8":
		scpt_conf=["interface ethernet 1/1-8",
						"no shutdown",
						"channel-group 8 force mode on"]
		scpt_sht=[]
	else:
		print("no")

	"""
	print(scpt_nsh)
	print(scpt_conf)
	print(scpt_sht)
	"""
	for i in range(len(scpt_conf)):
		#print(scpt_conf[i])
		cmd = scpt_conf[i]
		tn1.write(cmd.encode('ascii')+b"\n")
		tn2.write(cmd.encode('ascii')+b"\n")

	for j in range(len(scpt_sht)):
		#print(scpt_sht[j])
		cmd = scpt_sht[j]
		tn1.write(cmd.encode('ascii')+b"\n")
		tn2.write(cmd.encode('ascii')+b"\n")

	cmd = "exit"
	tn1.write(cmd.encode('ascii')+b"\n")
	tn2.write(cmd.encode('ascii')+b"\n")
	retval = "OK"
	return retval





#telnet to SWLab1
tn1 = telnetlib.Telnet(host='10.0.4.64', port=35202, timeout=10)
#telnet to SWLab2
tn2 = telnetlib.Telnet(host='10.0.4.64', port=35201, timeout=10)

"""
numport = "3"
asign = pushtonode(numport)
print(asign)
"""