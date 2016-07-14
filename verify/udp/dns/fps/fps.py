import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from time import strptime, mktime
import matplotlib.patches as mpatches
import os

def stime2epoch(t):
    time_ = t.split(' ')[1].split('.')
    if len(time_) == 1:
        ms = 0.0
    else:
        ms = float('.' + time_[1])
    minutes = mktime(strptime(time_[0], '%H:%M:%S'))

    return minutes + ms + 2208927600

st2e = np.vectorize(stime2epoch)

# GET DATA
# udp = pd.read_csv('../../../../output/udp_sim4_ANALYZE.txt', delimiter='|')
# udp['st'] = st2e(udp.stime)
#
# stimes = udp.st
#
# fps = {}
# STEP = 1
#
# for i in udp.st:
#     try:
#         fps[int(i)] += 1
#     except:
#         fps[int(i)] = 1
#
# ofile = open('fps.dat', 'w')
# for k, v in fps.iteritems():
#     print >> ofile, k, v
# ofile.close()

fps = {}
with open('./fps_sim.dat') as f:
    f.readline()
    for line in f:
        line = [int(i) for i in line.strip().split(' ')]
        fps[line[0]] = line[1]

fps_real = {}
with open('./fps_real.dat') as f:
    for line in f:
        line = line.strip().translate(None, '(),')
        line = [int(i) for i in line.split(' ')]
        fps_real[line[0]] = line[1]

#
# for i in range(0, 300, STEP):
#     ST = i
#     ET = i + STEP
#     flows_between_times = udp[ (udp >= ST) & (udp.st < ET) ]
#     print len(flows_between_times)
#     fps[i] = len(flows_between_times)

flowmin = min(fps.values())

SIM_COLOR = (0.0, 0.4, 1.0)
REAL_COLOR = (1.0, 0.6, 0.0)

plt.plot(fps.keys(), fps.values(), linewidth=0.5, color=SIM_COLOR)
plt.plot(fps_real.keys(), fps_real.values(), linewidth=0.5, color=REAL_COLOR)

realpatch = mpatches.Patch(color=REAL_COLOR, label='real')
simpatch = mpatches.Patch(color=SIM_COLOR, label='simulated')
plt.legend(handles=[realpatch, simpatch])

title = 'Simulated Flows Per Second (fps,f/s)\nSimulated Dataset File: udp_sim4_ANALYZE.txt'
plt.title(title)
plt.xlabel('time (s)')
plt.ylabel('number of flows')

plt.show()

