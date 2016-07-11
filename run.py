#!/usr/bin/env python

import simpy as sp
import signal
import sys
import datetime
from generators.udp_dns_reflection import UDPDNSReflectionAttack

def sim2realtime(secs):
    global __start
    return __start + datetime.timedelta(seconds=secs)

def SIGINTHandler(signal, frame):
    print '[x] Simulation aborted. SIGINT received.'
    sys.exit(1)

def InboundFlow(env, name, interval):
    udp_dns = UDPDNSReflectionAttack()
    while True:
        #start, duration, proto, sip, dip, sport, dport, packets, bytes, iflags, sflags
        gen_flow = udp_dns.mk_flow(env)
        print gen_flow
        yield env.timeout(interval)


def OutboundFlow(env):
    pass

# Set the handler for SIGINT
signal.signal(signal.SIGINT, SIGINTHandler)

# Configurable simulation start time to represent real world times (24 hour time)
SIMULATION_START_TIME = '09/07/2016 12:00:00'
__start = datetime.datetime.strptime(SIMULATION_START_TIME, '%d/%m/%Y %H:%M:%S')

env = sp.Environment()
env.process(InboundFlow(env, 'inflow', 1.3))
env.run(until=60)
