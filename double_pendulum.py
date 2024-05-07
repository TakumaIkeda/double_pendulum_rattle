import numpy as np

nsteps = 1000
dt = 0.01
g = 9.8

m1 = 1.0
m2 = 1.0

l1 = 2.0
l2 = 1.0

q1 = np.array([l1, 0.0])
q2 = np.array([l1 + l2, 0.0])

p1 = np.array([0.0, -10.0])
p2 = np.array([0.0, 0.0])

F1 = np.array([0.0, 0.0])
F2 = np.array([0.0, 0.0])

for i in range(nsteps):
  theta1 = np.arcsin(q1[0]/l1)
  theta2 = np.arcsin((q2[0]-q1[0])/l2)