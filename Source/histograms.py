#!/usr/src/env python3

import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(1)

mu, sigma = 2, 0.5

v = rg.normal(mu, sigma,1000)

plt.hist(v, bins=50, density=1)
(n, bins) = np.histogram(v, bins=50, density=True)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()