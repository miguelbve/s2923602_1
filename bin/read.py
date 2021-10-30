import numpy as np


def read():
    with open('data/laptops.csv') as laptopsdata:
        laptops = laptopsdata.read().splitlines()
    return laptops
