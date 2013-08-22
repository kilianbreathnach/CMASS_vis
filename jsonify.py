import json
import numpy as np


cart = np.loadtxt("cartesian.dat")

f = open("jcart.json", mode='w')

json.dump(cart.tolist(), f)

f.close()
