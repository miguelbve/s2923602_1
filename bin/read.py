import numpy as np


def read():
    with open('data/subsetonelaptops.csv') as laptopsdata:
        laptops = laptopsdata.read().splitlines()
        laptopsheader = laptops[0]
        laptops = laptops[1:]
        laptopsarray = np.array(laptops)
    return laptopsarray
