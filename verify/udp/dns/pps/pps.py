import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from time import mktime, strptime

# def stime2epoch(t):
#     time_ = t.split(' ')[1].split('.')
#     if len(time_) == 1:
#         ms = 0.0
#     else:
#         ms = float('.' + time_[1])
#     minutes = mktime(strptime(time_[0], '%H:%M:%S'))
#
#     return minutes + ms + 2208927600
#
# st2e = np.vectorize(stime2epoch)
#
# # GET DATA
# udp = pd.read_csv('../../../../output/udp_sim5.txt', delimiter='|')
# udp['st'] = st2e(udp.stime)
# udp.sort_values(by='st', inplace=True)
#
# pps = {}
#
# for i in range(0, int(max(udp.st))):
#     ST = i
#     ET = i + 1
#     flows_between = udp[ (udp.st >= ST) & (udp.st < ET) ]
#     pps[i] = sum(flows_between.pkt)
#
# with open('pps_sim.dat', 'w') as f:
#     for t, pkts in pps.iteritems():
#         print >> f, t, pkts
#
# quit()

sim = {}
with open('pps_sim5.dat') as f:
    for line in f:
        line = line.strip().split(' ')
        t = int(line[0])
        nbytes = int(line[1])
        sim[t] = nbytes


real = {}
with open('pps_real.dat') as f:
    for line in f:
        line = line.strip().split(' ')
        t = int(line[0])
        nbytes = int(line[1])
        real[t] = nbytes


SIM_COLOR = (0.0, 0.4, 1.0)
REAL_COLOR = (1.0, 0.6, 0.0)
realpatch = mpatches.Patch(color=REAL_COLOR, label='real')
simpatch = mpatches.Patch(color=SIM_COLOR, label='simulated')
plt.legend(handles=[realpatch, simpatch])

plt.plot(sim.keys(), sim.values(), color=SIM_COLOR, linewidth=0.5)
plt.plot(real.keys(), real.values(), color=REAL_COLOR, linewidth=0.5)

title = 'Simulated Packets Per Second (pps)\nSimulated Dataset File: udp_sim5.txt'
plt.title(title)
plt.xlabel('time (s)')
plt.ylabel('number of packets')

plt.show()
