import os
from distributions.functions import *
import time

__author__ = 'mrf6'

def _binsearch(target, values):
    # Credit: Alexander Jia, NIST

    def helper(target, left, right, values):
        index = (left + right) // 2
        if index == left:
            return left + 1  # Return the index to the right
        elif index == right:
            return right
        if values[index - 1] < target <= values[index]:
            return index  # Return the index to the right
        elif target < values[index]:
            return helper(target, left, index, values)
        else:
            return helper(target, index, right, values)

    if target < values[0]:
        return 0
    elif target > values[len(values) - 1]:
        return len(values) - 1
    else:
        return helper(target, 0, len(values) - 1, values)


def generate_cdf(filename):
    '''
    Generates the cumulative probability function from "filename"
    Used in tandem with generate_val(cdf).

    :param filename: the file to read the CDF from
    :return: a list object that can be read into generate_val to generate values
    '''

    parent_dir = os.path.abspath(os.path.join(filename, os.pardir)) + '/'
    probs = []
    keys = []
    infos = []
    with open(filename) as f:
        info = f.readline().strip()
        for line in f.readlines():
            line = line.strip().split(' ')
            value, prob = line[0], float(line[1])
            if line[0].endswith('.txt'):
                value = generate_cdf(parent_dir + value)
            keys.append(value)
            probs.append(prob)
            infos.append(info)

    return [keys, probs, infos]

def generate_val(cdf):
    '''
    Generates a random variable from the CDF

    :param cdf:
    :return: a value randomly chosen from the CDF
    '''
    additional = cdf[2][0] # the additional instruction to run after generating a random value

    keys = cdf[0]
    probs = cdf[1]

    randval = np.random.random()
    item = keys[_binsearch(randval, probs)]

    # if the item chosen is a CDF, then use that to generate a value
    if isinstance(item, list):
        item = generate_val(item)

    expr = additional.replace('X', str(item))
    evaluated = eval(expr)
    return evaluated

def mk_generator_from_file(cdf_filename):
    cdf = generate_cdf(cdf_filename)
    while True:
        yield generate_val(cdf)

def mk_generator_from_cdf(cdf):
    while True:
        yield generate_val(cdf)

if __name__ == '__main__':
    pass
