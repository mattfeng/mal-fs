import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from time import strptime, mktime
import matplotlib.patches as mpatches
import seaborn as sns

sns.set_style('whitegrid')
# plot the number of unique IPs as a function of time

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

udp = pd.read_csv('../../../../output/udp_sim5.txt', delimiter='|')
print len(np.unique(udp.sip))
# udp['st'] = st2e(udp.stime)

# stimes = udp.st
#
# sipps = {}
# STEP = 1
#
# for i in range(0, 300):
#     ST = i
#     ET = i + 1
#     flows_between = udp[ (udp.st >= ST) & (udp.st < ET) ]
#     uniq_ips = np.unique(flows_between.sip)
#     sipps[i] = len(uniq_ips)

# ofile = open('sipps.dat', 'w')
# for k, v in sipps.iteritems():
#     print >> ofile, k, v
# ofile.close()

# TODO: THIS FEATURE IS A FAILURE

quit()

# sipps = {}
#
# with open('sipps.dat') as f:
#     for line in f:
#         line = [int(i) for i in line.strip().split(' ')]
#         sec = line[0]
#         num_uniq_ips = line[1]
#         sipps[sec] = num_uniq_ips
#
# SIM_COLOR = (0.0, 0.4, 1.0)
# sns.plt.plot(sipps.keys(), sipps.values(), color=SIM_COLOR, lw=0.5)
# sns.plt.title('Simulated Number of Unique IPs for Each Second\nSimulated Dataset: udp_sim5.txt')
# sns.plt.xlabel('time (s)')
# sns.plt.ylabel('number of unique IPs')
# plt.show()
