from generator import Generator
import distribution as dist
import flow

class UDPDNSReflectionAttack(Generator):

    def __init__(self):
        super(UDPDNSReflectionAttack, self).__init__('UDP DNS DDoS Attack')

        # paths to the distributions
        path = '/home/pwn/PycharmProjects/mal-fs/profiles/booter1/'
        self._sportdist = path + 'sport/sport.txt'
        self._dportdist = path + 'dport/dport.txt'
        self._sipdist = path + 'sip/sip.txt'
        self._dipdist = path + 'dip/dip.txt'
        self._durdist = path + 'dur/dur.txt'
        self._ppfdist = path + 'ppf/ppf.txt'
        self._bppdist = path + 'bpp/bpp.txt'

        # the generators
        self.sport_generator = dist.mk_generator(self._sportdist)
        self.dport_generator = dist.mk_generator(self._dportdist)
        self.sip_generator = dist.mk_generator(self._sipdist)
        self.dip_generator = dist.mk_generator(self._dipdist)
        self.duration_generator = dist.mk_generator(self._durdist)
        self.ppf_generator = dist.mk_generator(self._ppfdist)
        self.bpp_generator = dist.mk_generator(self._bppdist)

        self.proto = 17

    def mk_flow(self, env):
        #start, duration, proto, sip, dip, sport, dport, packets, bytes, iflags, sflags

        dur = next(self.duration_generator)
        proto = self.proto
        sip = next(self.sip_generator)
        dip = next(self.dip_generator)
        sport = next(self.sport_generator)
        dport = next(self.dport_generator)
        pkts = next(self.ppf_generator)
        bytes = next(self.bpp_generator) * pkts
        iflags = ''
        sflags = ''

        flow_ = flow.Flow(env.now, dur, proto, sip, dip,
                          sport, dport, int(pkts), int(bytes), iflags, sflags)
        return flow_
