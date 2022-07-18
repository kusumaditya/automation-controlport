

def timeConv(timevar):
	#print(timevar)
	time_hr = int(timevar[0:2])
	time_mn = int(timevar[3:5])

	rsmn = time_mn/60

	rettime = time_hr+rsmn

	return str(rettime)



def dayConv(dayvar):
	#print(dayvar)
	if dayvar == "Senin":
		return "1"
	elif dayvar == "Selasa":
		return "2"
	elif dayvar == "Rabu":
		return "3"
	elif dayvar == "Kamis":
		return "4"
	elif dayvar == "Jumat":
		return "5"
	elif dayvar == "Sabtu":
		return "6"
	elif dayvar == "Minggu":
		return "7"
	else :
		return "Error"


