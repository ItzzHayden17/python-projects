import numpy as py

data = list(range(20, 100, 5))

q1 = py.quantile(data,0.25)
q2 = py.quantile(data,0.50)
q3 = py.quantile(data,0.75)

deviation = (q3-q1)/2

print(deviation)