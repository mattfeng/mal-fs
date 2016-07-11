class Flow(object):
    def __init__(self, start, duration, proto, sip, dip, sport,
                 dport, packets, bytes, iflags, sflags):
        self.stime = start
        self.duration = duration
        self.proto = proto
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.pkts = packets
        self.octs = bytes
        self.iflags = iflags
        self.sflags = sflags


    def __str__(self):
        '''Representation of the Flow as a string (for output)'''
        return '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (self.proto,
                                                     self.sip, self.dip,
                                                     self.sport, self.dport,
                                                     self.pkts, self.octs,
                                                     self.stime, self.duration,
                                                     self.iflags, self.sflags)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # testing
    f1 = Flow(0, 0.0, 7, "127.0.0.1", "255.255.255.255", 53, 29381, 100, 6000, '', '')
    print f1