from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

ims = []

l0 = 0.0
l1 = 1.0

theta0 = 0.0
theta1 = np.pi

p1 = 0.001

m1 = 1.0

dt = 0.01
g = 9.8

fig = plt.figure()

step = 0
def plot(theta1, ims):
    im = plt.scatter([l0, l1 * np.sin(theta1)], [0, -l1 * np.cos(theta1)], c=['red', 'red'])
    ims.append([im])
    return ims

plot(theta1, ims)

while step < 1000:
  V1 = m1 * g * l1 * (1 - np.cos(theta1))
  F1 = -m1 * g * l1 * np.sin(theta1)
  p1 += 0.5 * dt * F1
  theta1 += dt * p1 / m1
  F1 = -m1 * g * l1 * np.sin(theta1)
  p1 += 0.5 * dt * F1

  step += 1
  if step % 10 == 0:
    ims = plot(theta1, ims)

ani = animation.ArtistAnimation(fig, ims, interval=1)
ani.save('test.gif')