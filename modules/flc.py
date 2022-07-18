
"""
==================================
The Tipping Problem - The Hard Way
==================================
 Note: This method computes everything by hand, step by step. For most people,
 the new API for fuzzy systems will be preferable. The same problem is solved
 with the new API `in this example <./plot_tipping_problem_newapi.html>`_.
The 'tipping problem' is commonly used to illustrate the power of fuzzy logic
principles to generate complex behavior from a compact, intuitive set of
expert rules.
Input variables
---------------
A number of variables play into the decision about how much to tip while
dining. Consider two of them:
* ``quality`` : Quality of the food
* ``service`` : Quality of the service
Output variable
---------------
The output variable is simply the tip amount, in percentage points:
* ``tip`` : Percent of bill to add as tip
For the purposes of discussion, let's say we need 'high', 'medium', and 'low'
membership functions for both input variables and our output variable. These
are defined in scikit-fuzzy as follows
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from modules import contimedate as convtd

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points


#generate variable
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)
#var input
x_portutil = np.arange(0, 101, 1)
x_numconn = np.arange(0, 101, 1)
x_minbw = np.arange(0, 81, 1)
x_curtime = np.arange(0, 25, 1)
x_curday = np.arange(0, 8, 1)
#var output
x_numport = np.arange(0, 9, 1)


# Generate fuzzy membership functions
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

#mf input
portutil_lo = fuzz.trapmf(x_portutil, [0, 0, 20, 40])
portutil_md = fuzz.trapmf(x_portutil, [20, 45, 65, 80])
portutil_hi = fuzz.trapmf(x_portutil, [60, 80, 100, 100])
numconn_lo = fuzz.trapmf(x_numconn, [0, 0, 15, 40])
numconn_md = fuzz.trapmf(x_numconn, [10, 40, 65, 80])
numconn_hi = fuzz.trapmf(x_numconn, [65, 80, 105, 145])
minbw_lo = fuzz.trapmf(x_minbw, [0, 0, 15, 30])
minbw_md = fuzz.trapmf(x_minbw, [15, 30, 50, 75])
minbw_hi = fuzz.trapmf(x_minbw, [50, 70, 80, 80])
curtime_dh = fuzz.gbellmf(x_curtime, 2.4, 2.5, 1)
curtime_ph = fuzz.gbellmf(x_curtime, 2.4, 2.5, 4.774)
curtime_si = fuzz.gbellmf(x_curtime, 2.4, 2.5, 9.6)
curtime_so = fuzz.gbellmf(x_curtime, 2.4, 2.5, 14.4)
curtime_mh = fuzz.gbellmf(x_curtime, 2.4, 2.5, 19.2)
curtime_tm = fuzz.gbellmf(x_curtime, 2.4, 2.5, 24)
curday_wd = fuzz.trapmf(x_curday, [0, 0, 5, 6])
curday_we = fuzz.trapmf(x_curday, [5, 6, 7, 7])
#mf output
numport_lo = fuzz.trapmf(x_numport, [0, 0, 1, 2])
numport_ml = fuzz.trapmf(x_numport, [1, 2, 3, 5])
numport_mh = fuzz.trapmf(x_numport, [3, 5, 6, 7])
numport_hi = fuzz.trapmf(x_numport, [6, 7, 8, 8])







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
    
    global x_qual
    global x_serv
    global x_tip

    global x_portutil
    global x_numconn
    global x_minbw
    global x_curtime
    global x_curday
    global x_numport

    # Generate fuzzy membership functions
    global qual_lo
    global qual_md
    global qual_hi
    global serv_lo
    global serv_md
    global serv_hi
    global tip_lo
    global tip_md
    global tip_hi

    global portutil_lo
    global portutil_md
    global portutil_hi
    global numconn_lo
    global numconn_md
    global numconn_hi
    global minbw_lo
    global minbw_md
    global minbw_hi
    global curtime_dh
    global curtime_ph
    global curtime_si
    global curtime_so
    global curtime_mh
    global curtime_tm
    global curday_wd
    global curday_we
    global numport_lo
    global numport_ml
    global numport_mh
    global numport_hi

    vars_out = 0
    return vars_out
    

def view_mf_input():

    fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(8, 9))

    ax0.plot(x_portutil, portutil_lo, 'g', linewidth=1.5, label='Low')
    ax0.plot(x_portutil, portutil_md, 'y', linewidth=1.5, label='Mid')
    ax0.plot(x_portutil, portutil_hi, 'r', linewidth=1.5, label='Hi')
    ax0.set_title('Port Utilization [%]')
    ax0.legend()

    ax1.plot(x_numconn, numconn_lo, 'g', linewidth=1.5, label='Low')
    ax1.plot(x_numconn, numconn_md, 'y', linewidth=1.5, label='Mid')
    ax1.plot(x_numconn, numconn_hi, 'r', linewidth=1.5, label='Hi')
    ax1.set_title('Number Connection [Thousand]')
    ax1.legend()

    ax2.plot(x_minbw, minbw_lo, 'g', linewidth=1.5, label='Low')
    ax2.plot(x_minbw, minbw_md, 'y', linewidth=1.5, label='Mid')
    ax2.plot(x_minbw, minbw_hi, 'r', linewidth=1.5, label='Hi')
    ax2.set_title('Minimum Bandwidth [Gbps]')
    ax2.legend()

    ax3.plot(x_curtime, curtime_dh, 'b', linewidth=0.5, label='Dini Hari')
    ax3.plot(x_curtime, curtime_ph, 'y', linewidth=0.5, label='Pagi')
    ax3.plot(x_curtime, curtime_si, 'b', linewidth=0.5, label='Siang')
    ax3.plot(x_curtime, curtime_so, 'm', linewidth=0.5, label='Sore')
    ax3.plot(x_curtime, curtime_mh, 'c', linewidth=0.5, label='Malam')
    ax3.plot(x_curtime, curtime_tm, 'b', linewidth=0.5, label='Tengah Malam')
    ax3.set_title('Current Time 24hours')
    ax3.legend()

    ax4.plot(x_curday, curday_wd, 'y', linewidth=1.5, label='Weekday')
    ax4.plot(x_curday, curday_we, 'r', linewidth=1.5, label='Weekend')
    ax4.set_title('Current Day')
    ax4.legend()


    # Turn off top/right axes
    for ax in (ax0, ax1, ax2, ax3, ax4):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    asf_ret = "bsc"
    plt.tight_layout()
    plt.show()
    return asf_ret


def view_mf_output():


    fig, ax5 = plt.subplots(nrows=1, figsize=(8, 9))


    ax5.plot(x_numport, numport_lo, 'r', linewidth=1.5, label='Low')
    ax5.plot(x_numport, numport_ml, 'y', linewidth=1.5, label='MidLo')
    ax5.plot(x_numport, numport_mh, 'b', linewidth=1.5, label='MidHi')
    ax5.plot(x_numport, numport_hi, 'g', linewidth=1.5, label='High')
    ax5.set_title('Number of Port')
    ax5.legend()



    # Turn off top/right axes
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.get_xaxis().tick_bottom()
    ax5.get_yaxis().tick_left()

    asf_ret = "bsc"
    plt.tight_layout()
    plt.show()
    return asf_ret

def view_rules():
    print("yep")
    asf_ret = "bsc"
    return asf_ret