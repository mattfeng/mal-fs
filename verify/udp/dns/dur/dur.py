import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

sns.set_style('whitegrid')

def create_timeline(feature, filename, number):
    number = str(number)
    def stime2epoch(t):
        from time import mktime, strptime
        time_ = t.split(' ')[1].split('.')
        if len(time_) == 1:
            ms = 0.0
        else:
            ms = float('.' + time_[1])
        minutes = mktime(strptime(time_[0], '%H:%M:%S'))

        return minutes + ms + 2208927600

    st2e = np.vectorize(stime2epoch)

    # GET DATA
    udp = pd.read_csv('../../../../output/' + filename + number + '.txt', delimiter='|')
    udp['st'] = st2e(udp.stime)
    udp.sort_values(by='st', inplace=True)

    timeline = {}

    for i in range(0, int(max(udp.st))):
        ST = i
        ET = i + 1
        flows_between = udp[ (udp.st >= ST) & (udp.st < ET) ]
        # TODO: NEED TO CHANGE THIS
        timeline[i] = flows_between['dur'].mean()

    with open(feature + '_sim' + number + '.dat', 'w') as f:
        for t, dat in timeline.iteritems():
            print >> f, t, dat

def time_based_graph():
    sim = {}
    with open(feature + '_sim' + number + '.dat') as f:
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            data = float(line[1])
            sim[t] = data


    real = {}
    with open(feature + '_real.dat') as f:
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            data = float(line[1])
            real[t] = data

    print sim
    print real

    SIM_COLOR = (0.0, 0.4, 1.0)
    REAL_COLOR = (1.0, 0.6, 0.0)
    realpatch = mpatches.Patch(color=REAL_COLOR, label='real')
    simpatch = mpatches.Patch(color=SIM_COLOR, label='simulated')
    plt.legend(handles=[realpatch, simpatch])

    plt.plot(sim.keys(), sim.values(), color=SIM_COLOR, linewidth=0.5)
    plt.plot(real.keys(), real.values(), color=REAL_COLOR, linewidth=0.5)

    title = 'Simulated Average Duration for Each Second (dur)\nSimulated Dataset File: udp_sim5.txt'
    plt.title(title)
    plt.xlabel('time (s)')
    plt.ylabel('duration (s)')

    plt.show()

feature = 'dur'
filename = 'udp_sim'
number = str(5)

#create_timeline(feature, filename, number)

time_based_graph()
quit()

udp = pd.read_csv('../../../../output/' + filename + number + '.txt', delimiter='|')
most = udp[ udp.dur < 3 ]
print float(len(most)) / len(udp)

sns.plt.hist(most.dur, bins=1000)
sns.plt.title('Simulated Distribution of Durations\nSimulated Dataset: udp_sim5.txt')
sns.plt.xlabel('duration')
sns.plt.ylabel('number of flows')
sns.plt.xlim([0, 0.25])
plt.show()

