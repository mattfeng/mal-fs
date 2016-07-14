import numpy as np
import scipy.stats as sp

def uniform(a, b):
    return np.random.uniform(a, b)

def normal(mean, std):
    return np.random.normal(mean, std)

def randint(a, b):
    return np.random.randint(a, b)

def rnd(a, deci):
    return np.around(a, deci)


if __name__ == '__main__':
    pass