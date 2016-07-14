import distribution

class Feature(object):
    def __init__(self, name, distribution_folder):
        self.name = name
        self.featuredist = distribution_folder.rstrip('/') + '/info.txt'
        self.generator = None

        # (time to update, distribution) -> make the distributions before hand
        self.updates = []
        self.get_dist_update_times_and_distributions()

    #TODO: FINISH WRITING THE FEATURE CLASS
    #TODO: REWRITE GENERATOR CLASS USING FEATURES
    def get_dist_update_times_and_distributions(self):
        with open(self.featuredist) as f:
            for line in f:
                line = line.strip().split(' ')
                t = float(line[0])
                t_dist_cdf = distribution.generate_cdf(line[1])
                self.updates.append((t, t_dist_cdf))
