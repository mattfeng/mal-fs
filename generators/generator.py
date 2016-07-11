from abc import ABCMeta, abstractmethod

class Generator(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._name = name
        self._sportdist = None
        self._dportdist = None
        self._sipdist = None
        self._dipdist = None
        self._durdist = None
        self._ppfdist = None
        self._bppdist = None

        # the generators
        self.sport_generator = None
        self.dport_generator = None
        self.sip_generator = None
        self.dip_generator = None
        self.duration_generator = None
        self.ppf_generator = None
        self.bpp_generator = None


    @abstractmethod
    def mk_flow(self, env):
        pass
