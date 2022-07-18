import os
import sys
import time
from modules import dummy_input as dumm_input
from modules import flc as flc
from modules import aflc as aflc
from modules import randval as randval
#from modules import pushnode as pushnode


#####################################################################
#                 ADITYA KUSUMA PROGRAM FILES                       #
#   NETWORK AUTOMATION FOR CONTROL PORT WITH FUZZY LOGIC ALGORIRM   #
#                       COPYRIGHT 2022                              #
#####################################################################



class Menu():
    def __init__(self):
        self.choices = {
        "1" : self.input_dum,
        "2" : self.flc,
        "3" : self.contflc,
        "4" : self.rvflc,
        "11" : self.dsp_mf_input,
        "12" : self.dsp_mf_output,
        "13" : self.dsp_rules,
        "14" : self.dsp_result,
        "00" : self.quit,
        "0" : self.clear
        }

    def run(self):
        while True:
            self.dsp_menus()
            choice = input("Choose the Menu: ")
            if choice == "2":
                action = self.choices.get(choice)
                asp = action(dmp_var)
            elif choice == "1":
                action = self.choices.get(choice)
                dmp_var, no_var = action()
            elif choice == "3":
                action = self.choices.get(choice)
                asp = action(no_var)
            else:
                action = self.choices.get(choice)
                asp = action()
            
            #print(dmp_var, no_var)
            
    def input_dum(self):
        no_var = int(input("input dummy excel : "))
        dmp_vars = []
        dmp_vars = dumm_input.dumm(no_var)
        
        #Get data from bundle input dummy
        dmp_var = dmp_vars[0]
        input_time = dmp_var["time"]
        input_day = dmp_var["day"]
        input_port_util = dmp_var["port_util"]
        input_num_conn = dmp_var["num_conn"]
        input_min_bw = dmp_var["min_bw"]
        #print(dmp_var)
        return dmp_var, no_var


    def dsp_mf_output(self):
        print("test dsp_mf_output")
        get_view_output = flc.view_mf_output()
        print(get_view_output)

    def dsp_mf_input(self):
        print("test dsp_mf_input")
        get_view_input = flc.view_mf_input()
        print(get_view_input)

    def dsp_rules(self):
        print("test dsp_rules")
        get_view_rules = flc.view_rules()
        print(get_view_rules)

    def dsp_result(self):
        print("test dsp_result")
        get_view_result = aflc.view_res_out()
        print(get_view_result)

    def dsp_menus(self):
        print("""
            \t#####################################################################
            \t#                 ADITYA KUSUMA PROGRAM FILES                       #
            \t#   NETWORK AUTOMATION FOR CONTROL PORT WITH FUZZY LOGIC ALGORITM   #
            \t#                       COPYRIGHT 2022                              #
            \t#####################################################################

            \tNetwork Automation with Fuzzy Logic
            \tThis is the menu :
            \t1. Choose input Dummy Data from Excel
            \t2. Run Fuzzy Logic Controller [one by one]
            \t3. Continues Run Fuzzy
            \t4. Continues Run Fuzzy with Random Input Parameter
            \t11. View the Membership Function of Input
            \t12. View the Membership Function of Output
            \t13. View the rules
            \t14. View result out
            \t0. Clear Windows
            \t00.Quit the Application
            """)
    #FUNCTION FUZZY ONE BY ONE
    def flc(self, dmp_var):
        print("\t======================= PARAMETER INPUT FUZZY =======================")
        print(dmp_var)
        run_flc = aflc.run_flc(dmp_var)
        print("##### RESULT OUTPUT FUZZY #####")
        print(int(run_flc), " PORTS active required to handle the traffic")
        print("TRY PUSH CONFIGURATION TO NODE")
        """
        ##### NEXT FOR PUSH SSH FUNCTION #####
        telptn = pushnode.pushtonode(str(int(run_flc)))
        print(telptn)
        """


        time.sleep(2) #delay for make sure connection to node establish
    

    #FUNCTION FUZZY CONTINOUS UNTIL BREAK
    def contflc(self, no_var):
        try:
            while True:
                dmp_vars = dumm_input.dumm(no_var)
                dmp_var = dmp_vars[0]
                print("\t======================= PARAMETER INPUT FUZZY =======================")
                print(dmp_var)
                run_flc = aflc.run_flc(dmp_var) #Get output fuzzy function
                print("##### RESULT OUTPUT FUZZY #####")
                print(int(run_flc), " PORTS active required to handle the traffic")
                print("TRY PUSH CONFIGURATION TO NODE")
                """
                ##### NEXT FOR PUSH SSH FUNCTION #####
                telptn = pushnode.pushtonode(str(int(run_flc)))
                print(telptn)
                """


                time.sleep(2) #delay for make sure connection to node establish
                no_var = no_var+1                
        except KeyboardInterrupt:
            Menu().run()
            

    def rvflc(self):
        try:
            while True:
                dmp_var = randval.rval()
                print("\t======================= PARAMETER INPUT FUZZY =======================")
                print(dmp_var)
                run_flc = aflc.run_flc(dmp_var) #Get output fuzzy function
                print("##### RESULT OUTPUT FUZZY #####")
                print(int(run_flc), " PORTS active required to handle the traffic")
                print("TRY PUSH CONFIGURATION TO NODE")
                """
                ##### NEXT FOR PUSH SSH FUNCTION #####
                telptn = pushnode.pushtonode(str(int(run_flc)))
                print(telptn)
                """


                time.sleep(2) #delay for make sure connection to node establish
        except KeyboardInterrupt:
            Menu().run()



    def quit(self):
        while True:
            confirm = input('Are you sure to close this program? [y/n]: ')
            if confirm == 'y' or confirm == 'Y':
                print('\nProgram closed!\n')
                sys.exit(0)
                self.run()
            elif confirm == 'n' or confirm == 'N':
                self.run()
            else:
                confirm
    def clear(self):
        cmd = 'clear-host'
        os.system(cmd)


         

if __name__ == '__main__':
    Menu().run()
