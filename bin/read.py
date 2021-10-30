import numpy as np


def read():
    with open('data/subsetonelaptops.csv') as laptopsdata:
        laptops = laptopsdata.read().splitlines()
    return laptops
