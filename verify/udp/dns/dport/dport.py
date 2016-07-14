import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

sns.set_style('whitegrid')

# filename = 'udp_sim'
# number = '5'
# udp = pd.read_csv('../../../../output/' + filename + number + '.txt', delimiter='|')
#
# dports = udp.dport
# ports, counts = np.unique(dports, return_counts=True)
#
# with open('dport_sim5.txt', 'w') as f:
#     for p, c in zip(ports, counts):
#         print >> f, p, c
# quit()

dportdist = {}

with open('dport_sim5.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        p = int(line[0])
        c = int(line[1])
        dportdist[p] = c

SIM_COLOR = (0.0, 0.4, 1.0)
sns.plt.scatter(dportdist.keys(), dportdist.values(), marker='x', color=SIM_COLOR)
sns.plt.title('Simulated Frequency of Destination Ports\nSimulated Dataset: udp_sim5.txt')
sns.plt.xlabel('port number')
sns.plt.ylabel('frequency')

plt.show()

