from generator import Generator
import distribution as dist
import flow
from feature import Feature
from time import time
import numpy as np

class UDPDNSReflectionAttack(Generator):

    def __init__(self, name, env, sol, eol):

        # paths to the distributions
        self._profile = '/home/pwn/PycharmProjects/mal-fs/profiles/booter1/'
        self._sportdist = self._profile + 'sport/sport.txt'
        self._dportdist = self._profile + 'dport/dport.txt'

        self._oct1dist = self._profile + 'sip/oct1.txt'
        self._oct2dist = self._profile + 'sip/oct2.txt'
        self._oct3dist = self._profile + 'sip/oct3.txt'
        self._oct4dist = self._profile + 'sip/oct4.txt'

        self._dipdist = self._profile + 'dip/dip.txt'
        self._durdist = self._profile + 'dur/dur.txt'
        self._ppfdist = self._profile + 'ppf/ppf.txt'
        self._bppdist = self._profile + 'bpp/bpp.txt'

        # the features that characterize this attack -- creates the generators
        self.features = {}
        self.features['sport'] = Feature('sport', self._profile + 'sport/')
        self.features['dport'] = Feature('dport', self._profile + 'dport/')
        self.features['dip'] = Feature('dip', self._profile + 'dip/')
        self.features['dur'] = Feature('dur', self._profile + 'dur/')
        self.features['ppf'] = Feature('ppf', self._profile + 'ppf/')
        self.features['bpp'] = Feature('bpp', self._profile + 'bpp/')
        self.features['iat'] = Feature('iat', self._profile + 'iat/')
        self.sip_generator = self.mk_sip_generator(self._oct1dist, self._oct2dist,
                                                   self._oct3dist, self._oct4dist)


        super(UDPDNSReflectionAttack, self).__init__(name, env, sol, eol, self.features)

        self.proto = 17
        self.action = env.process(self.run(env))

    def mk_flow(self, env):
        #start, duration, proto, sip, dip, sport, dport, packets, bytes, iflags, sflags

        dur = next(self.features['dur'].generator)
        proto = self.proto
        sip = next(self.sip_generator)
        dip = next(self.features['dip'].generator)
        sport = next(self.features['sport'].generator)
        dport = next(self.features['dport'].generator)
        pkts = next(self.features['ppf'].generator)
        bytes = next(self.features['bpp'].generator) * pkts

        stime = np.around(env.now, 3)

        iflags = ''
        sflags = ''

        flow_ = flow.Flow(stime, dur, proto, sip, dip,
                          sport, dport, int(pkts), int(bytes), iflags, sflags)

        return flow_

    def mk_sip_generator(self, oct1dist, oct2dist, oct3dist, oct4dist):
        oct1gen = dist.mk_generator_from_file(oct1dist)
        oct2gen = dist.mk_generator_from_file(oct2dist)
        oct3gen = dist.mk_generator_from_file(oct3dist)
        oct4gen = dist.mk_generator_from_file(oct4dist)

        while True:
            oct1next = next(oct1gen)
            oct2next = next(oct2gen)
            oct3next = next(oct3gen)
            oct4next = next(oct4gen)

            yield '%s.%s.%s.%s' % (oct1next, oct2next, oct3next, oct4next)


