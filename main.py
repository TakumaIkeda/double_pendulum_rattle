from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

ims = []

r0 = np.array([0.0, 3.0])
r1 = np.array([0.0, 2.0])
r2 = np.array([0.0, 1.0])

p1 = np.array([0.0, 0.0])
p2 = np.array([-10.0, 0.0])

m1 = 1.0
m2 = 1.0

step = 0
dt = 0.1
g = 9.8

fig = plt.figure()

def plot(r1, r2, ims):
    im = plt.scatter([3, r1[0], r2[0]], [3, r1[1], r2[1]])
    ims.append([im])
    return ims

plot(r1, r2, ims)

while step < 1000:
  V1 = m1 * g * r1[1]
  V2 = m2 * g * r2[1]

  F1 = np.array([0.0, -m1 * g])
  F2 = np.array([0.0, -m2 * g])

  p1 += 0.5 * dt * F1
  p2 += 0.5 * dt * F2

  r1 += dt * p1 / m1
  r2 += dt * p2 / m2

  F1 = np.array([0.0, -m1 * g])
  F2 = np.array([0.0, -m2 * g])

  p1 += 0.5 * dt * F1
  p2 += 0.5 * dt * F2

  step += 1
  ims = plot(r1, r2, ims)

ani = animation.ArtistAnimation(fig, ims, interval=1)
ani.save('test.gif')