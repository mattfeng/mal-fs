from abc import ABCMeta, abstractmethod
import distribution as distri

class Generator(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, env, sol, eol, featureset):

        self._name = name

        self.features = featureset

        self._IAT_UPDATE_COOLDOWN = 0.5

        # simulation times
        self.start_of_life = sol
        self.end_of_life = eol
        self.ofile = open('./output/output_flows.txt', 'w')
        flow_header = 'pro|sip|dip|sport|dport|pkt|oct|stime|dur|iflags|sflags\n'
        self.ofile.write(flow_header)

    @abstractmethod
    def mk_flow(self, env):
        pass

    # TODO: UPDATE THE FEATURE DISTRIBUTIONS ACCORDING TO TIME
    def run(self, env):
        print '[%s] [init] *G "%s" initialized' % (env.now, self._name)

        # waiting until Start of Life
        yield env.timeout(self.start_of_life - env.now)

        # run until EOLife
        print '[%s] [active] *G "%s" started' % (env.now, self._name)

        iat = 0
        iat_last_update = -1000

        while env.now < self.end_of_life:

            # update feature distributions
            for feature, feature_obj in self.features.iteritems():
                times_list = feature_obj.updates
                if len(times_list) != 0:
                    # next_dist = (time, cdf)
                    next_dist = times_list[0]
                    next_dist_start_time = next_dist[0]
                    next_dist_cdf = next_dist[1]

                    if env.now >= next_dist_start_time:
                        print '[%s] [distchange] *G "%s" feature "%s" switched to time dist %s' % \
                              (env.now, self._name, feature, next_dist_start_time)
                        self.features[feature].generator = distri.mk_generator_from_cdf(next_dist_cdf)
                        # don't know if this is OK: times_list.pop(0)
                        self.features[feature].updates.pop(0)


            # update IAT if self._IAT_UPDATE_COOLDOWN elapsed
            if env.now - iat_last_update > self._IAT_UPDATE_COOLDOWN:
                iat = next(self.features['iat'].generator)
                iat_last_update = env.now

            generated_flow = self.mk_flow(env)
            # write the flow to file
            self.ofile.write(str(generated_flow) + '\n')

            yield env.timeout(iat)

        print '[%s] [inactive] *G "%s" stopped' % (env.now, self._name)
