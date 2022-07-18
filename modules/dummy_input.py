from openpyxl import load_workbook
import os

cwd = os.path.abspath('')

def dumm(no_var):
	no_var = no_var
	try:
		file_task = cwd+"/dmpinput/dmp_input.xlsx"
		open_book_task = load_workbook(file_task, data_only=True)
		input_coll = open_book_task["Sheet1"]
		excel_count = 1 + no_var
		input_ls = []
		input_ls.append({
				"time" : str(input_coll["B"+str(excel_count)].value),
				"day" : str(input_coll["C"+str(excel_count)].value),
				"port_util" : str(input_coll["D"+str(excel_count)].value),
				"num_conn" : str(input_coll["E"+str(excel_count)].value),
				"min_bw" : str(input_coll["F"+str(excel_count)].value)
				})
		#print (input_ls)
		return input_ls
	except FileNotFoundError:
		print("""
			#################################
			#    SCRIPT EXCEL NOT FOUND     #
			#	PLEASE CROSSCHECK AGAIN		#
			#################################
			""")