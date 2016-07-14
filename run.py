#!/usr/bin/env python

import simpy as sp
import signal
import sys
from generators.udp_dns_reflection import UDPDNSReflectionAttack
import time

def SIGINTHandler(signal, frame):
    print '[x] Simulation aborted. SIGINT received.'
    sys.exit(1)

def parse_config(env):
    pass

def main():
    # Set the handler for SIGINT
    signal.signal(signal.SIGINT, SIGINTHandler)

    env = sp.Environment()
    parse_config(env)

    udp = UDPDNSReflectionAttack('UDP Attack 1', env, sol=0, eol=300)

    # Begin simulation
    start = time.time()
    print '[i] Simulation start time: %s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    env.run(until=300)

    end = time.time()
    print '[i] Simulation start time: %s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print '[i] Time elapsed: %s' % (end - start)

if __name__ == '__main__':
    main()
