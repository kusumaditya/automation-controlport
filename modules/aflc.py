import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from modules import contimedate as convtd

#generate variable
#var input
x_portutil = np.arange(0, 101, 1)
x_numconn = np.arange(0, 101, 1)
x_minbw = np.arange(0, 81, 1)
x_curtime = np.arange(0, 25, 1)
x_curday = np.arange(0, 8, 1)
#var output
x_numport = np.arange(0, 9, 1)

# New Antecedent/Consequent objects hold universe variables and membership
# functions
#input
portutil = ctrl.Antecedent(x_portutil, 'portutil')
numconn = ctrl.Antecedent(x_numconn, 'numconn')
minbw = ctrl.Antecedent(x_minbw, 'minbw')
curtime = ctrl.Antecedent(x_curtime, 'curtime')
curday = ctrl.Antecedent(x_curday, 'curday')
#output
numport = ctrl.Consequent(x_numport, 'numport')


# Auto-membership function population is possible with .automf(3, 5, or 7)
portutil['lo'] = fuzz.trapmf(portutil.universe, [0, 0, 20, 40])
portutil['md'] = fuzz.trapmf(portutil.universe, [20, 45, 65, 80])
portutil['hi'] = fuzz.trapmf(portutil.universe, [60, 80, 100, 100])
numconn['lo'] = fuzz.trapmf(numconn.universe, [0, 0, 15, 40])
numconn['md'] = fuzz.trapmf(numconn.universe, [10, 40, 65, 80])
numconn['hi'] = fuzz.trapmf(numconn.universe, [65, 80, 105, 145])
minbw['lo'] = fuzz.trapmf(minbw.universe, [0, 0, 15, 30])
minbw['md'] = fuzz.trapmf(minbw.universe, [15, 30, 50, 75])
minbw['hi'] = fuzz.trapmf(minbw.universe, [50, 70, 80, 80])
curtime['dh'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 1)
curtime['ph'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 4.774)
curtime['si'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 9.6)
curtime['so'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 14.4)
curtime['mh'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 19.2)
curtime['tm'] = fuzz.gbellmf(curtime.universe, 2.4, 2.5, 24)
curday['wd'] = fuzz.trapmf(curday.universe, [0, 0, 5, 6])
curday['we'] = fuzz.trapmf(curday.universe, [5, 6, 7, 7])



# Custom membership functions can be built interactively with a familiar,
# Pythonic API
numport['lo'] = fuzz.trapmf(numport.universe, [0, 0, 1, 2])
numport['ml'] = fuzz.trapmf(numport.universe, [1, 2, 3, 5])
numport['mh'] = fuzz.trapmf(numport.universe, [3, 5, 6, 7])
numport['hi'] = fuzz.trapmf(numport.universe, [6, 7, 8, 8])


#behavior normal
rule1  = ctrl.Rule(portutil['hi'] & numconn['hi'] & minbw['md'], numport['hi'])
rule2  = ctrl.Rule(portutil['hi'] & numconn['md'] & minbw['md'], numport['hi'])
rule3  = ctrl.Rule(portutil['hi'] & numconn['lo'] & minbw['md'], numport['hi'])
rule4  = ctrl.Rule(portutil['md'] & numconn['hi'] & minbw['md'], numport['hi'])
rule5  = ctrl.Rule(portutil['md'] & numconn['md'] & minbw['md'], numport['mh'])
rule6  = ctrl.Rule(portutil['md'] & numconn['lo'] & minbw['md'], numport['ml'])
rule7  = ctrl.Rule(portutil['lo'] & numconn['hi'] & minbw['md'], numport['ml'])
rule8  = ctrl.Rule(portutil['lo'] & numconn['md'] & minbw['md'], numport['lo'])
rule9  = ctrl.Rule(portutil['lo'] & numconn['lo'] & minbw['md'], numport['lo'])
#behavior weekday
rule10 = ctrl.Rule(portutil['hi'] & curtime['dh'] & curday['wd'], numport['hi'])
rule11 = ctrl.Rule(portutil['md'] & curtime['dh'] & curday['wd'], numport['ml'])
rule12 = ctrl.Rule(portutil['lo'] & curtime['dh'] & curday['wd'], numport['lo'])
rule13 = ctrl.Rule(portutil['hi'] & curtime['ph'] & curday['wd'], numport['hi'])
rule14 = ctrl.Rule(portutil['md'] & curtime['ph'] & curday['wd'], numport['ml'])
rule15 = ctrl.Rule(portutil['lo'] & curtime['ph'] & curday['wd'], numport['ml'])
rule16 = ctrl.Rule(portutil['hi'] & curtime['si'] & curday['wd'], numport['hi'])
rule17 = ctrl.Rule(portutil['md'] & curtime['si'] & curday['wd'], numport['mh'])
rule18 = ctrl.Rule(portutil['lo'] & curtime['si'] & curday['wd'], numport['mh'])
rule19 = ctrl.Rule(portutil['hi'] & curtime['so'] & curday['wd'], numport['hi'])
rule20 = ctrl.Rule(portutil['md'] & curtime['so'] & curday['wd'], numport['ml'])
rule21 = ctrl.Rule(portutil['lo'] & curtime['so'] & curday['wd'], numport['ml'])
rule22 = ctrl.Rule(portutil['hi'] & curtime['mh'] & curday['wd'], numport['hi'])
rule23 = ctrl.Rule(portutil['md'] & curtime['mh'] & curday['wd'], numport['mh'])
rule24 = ctrl.Rule(portutil['lo'] & curtime['mh'] & curday['wd'], numport['mh'])
rule25 = ctrl.Rule(portutil['hi'] & curtime['tm'] & curday['wd'], numport['hi'])
rule26 = ctrl.Rule(portutil['md'] & curtime['tm'] & curday['wd'], numport['ml'])
rule27 = ctrl.Rule(portutil['lo'] & curtime['tm'] & curday['wd'], numport['lo'])
#behavior weekend
rule28 = ctrl.Rule(portutil['hi'] & curtime['dh'] & curday['we'], numport['hi'])
rule29 = ctrl.Rule(portutil['md'] & curtime['dh'] & curday['we'], numport['mh'])
rule30 = ctrl.Rule(portutil['lo'] & curtime['dh'] & curday['we'], numport['ml'])
rule31 = ctrl.Rule(portutil['hi'] & curtime['ph'] & curday['we'], numport['hi'])
rule32 = ctrl.Rule(portutil['md'] & curtime['ph'] & curday['we'], numport['ml'])
rule33 = ctrl.Rule(portutil['lo'] & curtime['ph'] & curday['we'], numport['lo'])
rule34 = ctrl.Rule(portutil['hi'] & curtime['si'] & curday['we'], numport['hi'])
rule35 = ctrl.Rule(portutil['md'] & curtime['si'] & curday['we'], numport['ml'])
rule36 = ctrl.Rule(portutil['lo'] & curtime['si'] & curday['we'], numport['lo'])
rule37 = ctrl.Rule(portutil['hi'] & curtime['so'] & curday['we'], numport['hi'])
rule38 = ctrl.Rule(portutil['md'] & curtime['so'] & curday['we'], numport['ml'])
rule39 = ctrl.Rule(portutil['lo'] & curtime['so'] & curday['we'], numport['lo'])
rule40 = ctrl.Rule(portutil['hi'] & curtime['mh'] & curday['we'], numport['hi'])
rule41 = ctrl.Rule(portutil['md'] & curtime['mh'] & curday['we'], numport['ml'])
rule42 = ctrl.Rule(portutil['lo'] & curtime['mh'] & curday['we'], numport['lo'])
rule43 = ctrl.Rule(portutil['hi'] & curtime['tm'] & curday['we'], numport['hi'])
rule44 = ctrl.Rule(portutil['md'] & curtime['tm'] & curday['we'], numport['mh'])
rule45 = ctrl.Rule(portutil['lo'] & curtime['tm'] & curday['we'], numport['ml'])
#behavior normal (minbw = lo)
rule46 = ctrl.Rule(portutil['hi'] & numconn['hi'] & minbw['lo'], numport['hi'])
rule47 = ctrl.Rule(portutil['hi'] & numconn['md'] & minbw['lo'], numport['hi'])
rule48 = ctrl.Rule(portutil['hi'] & numconn['lo'] & minbw['lo'], numport['hi'])
rule49 = ctrl.Rule(portutil['md'] & numconn['hi'] & minbw['lo'], numport['mh'])
rule50 = ctrl.Rule(portutil['md'] & numconn['md'] & minbw['lo'], numport['ml'])
rule51 = ctrl.Rule(portutil['md'] & numconn['lo'] & minbw['lo'], numport['ml'])
rule52 = ctrl.Rule(portutil['lo'] & numconn['hi'] & minbw['lo'], numport['ml'])
rule53 = ctrl.Rule(portutil['lo'] & numconn['md'] & minbw['lo'], numport['lo'])
rule54 = ctrl.Rule(portutil['lo'] & numconn['lo'] & minbw['lo'], numport['lo'])
#behavior normal (minbw = hi)
rule55 = ctrl.Rule(portutil['hi'] & numconn['hi'] & minbw['hi'], numport['hi'])
rule56 = ctrl.Rule(portutil['hi'] & numconn['md'] & minbw['hi'], numport['hi'])
rule57 = ctrl.Rule(portutil['hi'] & numconn['lo'] & minbw['hi'], numport['hi'])
rule58 = ctrl.Rule(portutil['md'] & numconn['hi'] & minbw['hi'], numport['hi'])
rule59 = ctrl.Rule(portutil['md'] & numconn['md'] & minbw['hi'], numport['hi'])
rule60 = ctrl.Rule(portutil['md'] & numconn['lo'] & minbw['hi'], numport['hi'])
rule61 = ctrl.Rule(portutil['lo'] & numconn['hi'] & minbw['hi'], numport['hi'])
rule62 = ctrl.Rule(portutil['lo'] & numconn['md'] & minbw['hi'], numport['mh'])
rule63 = ctrl.Rule(portutil['lo'] & numconn['lo'] & minbw['hi'], numport['mh'])


numberpt_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,
                                    rule4, rule5, rule6,
                                    rule7, rule8, rule9,
                                    rule10, rule11, rule12,
                                    rule13, rule14, rule15,
                                    rule16, rule17, rule18,
                                    rule19, rule20, rule21,
                                    rule22, rule23, rule24,
                                    rule25, rule26, rule27,
                                    rule29, rule28, rule30,
                                    rule31, rule32, rule33,
                                    rule34, rule35, rule36,
                                    rule37, rule38, rule39,
                                    rule40, rule41, rule42,
                                    rule43, rule44, rule45,
                                    rule46, rule47, rule48,
                                    rule49, rule50, rule51,
                                    rule52, rule53, rule54,
                                    rule55, rule56, rule57,
                                    rule58, rule59, rule60,
                                    rule61, rule62, rule63])
numberpt = ctrl.ControlSystemSimulation(numberpt_ctrl)



def run_flc(vars_input):
   val_time = vars_input["time"]
   val_day = vars_input["day"]
   val_portutil = vars_input["port_util"]
   val_numconn = vars_input["num_conn"]
   val_minbw = vars_input["min_bw"]

   #conversion time and day format
   val_time = convtd.timeConv(val_time)
   val_day = convtd.dayConv(val_day)
   #print(val_time, val_day, val_portutil, val_numconn, val_minbw)
      
   

   numberpt.input['portutil'] = int(val_portutil)
   numberpt.input['numconn'] = int(val_numconn)
   numberpt.input['minbw'] = int(val_minbw)
   numberpt.input['curtime'] = float(val_time)
   numberpt.input['curday'] = int(val_day)
   numberpt.compute()
   print("Calculate Fuzzy: ", numberpt.output['numport'])
   out_numport = float(numberpt.output['numport'])
   pout = np.ceil(out_numport)
   print("Pembulatan Fuzzy: ", pout)

   """
   numport.view(sim=numberpt)
   plt.show()
   """
   #pout = "OK!!"
   vars_out = pout
   return vars_out

def view_res_out():
   numport.view(sim=numberpt)
   plt.show()