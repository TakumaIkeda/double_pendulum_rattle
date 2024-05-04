from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy.linalg import norm

ims = []

d01 = 1.0
d12 = 1.0

r0 = np.array([0.0, 0.0])
r1 = np.array([1.0, 0.0])
r2 = np.array([2.0, 0.0])

p1 = np.array([0.0, 0.0])
p2 = np.array([0.0, -50.0])

m1 = 1.0
m2 = 2.0

step = 0
dt = 0.02
nsteps = 10000
g = 9.8

fig = plt.figure()

def plot(r0, r1, r2, ims):
    im = plt.scatter([r0[0], r1[0], r2[0]], [r0[1], r1[1], r2[1]], c=['red', 'red', 'red'])
    ims.append([im])
    return ims

plot(r0, r1, r2, ims)

def restrain(r1_prev, r2_prev, r1, r2, p1, p2):
  gamma01 = 1.0
  gamma12 = 1.0
  gamma_vel01 = 1.0
  gamma_vel12 = 1.0
  while abs(gamma01) > 1e-10 or abs(gamma12) > 1e-10 or abs(gamma_vel01) > 1e-10 or abs(gamma_vel12) > 1e-10:
    # shake
    a = (norm(r1_prev - r0) / m1) ** 2
    b = 2 * norm(r1 - r0) * norm(r1_prev - r0) / m1
    c = norm(r1 - r0) ** 2 - d01 ** 2
    gamma01 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r1 += gamma01 * (r1_prev - r0) / m1
    a = (1 / m1 + 1 / m2) * (norm(r1_prev) - norm(r2_prev))
    b = 2 * (1 / m1 + 1 / m2) * (norm(r1_prev) - norm(r2_prev)) * (norm(r1) - norm(r2))
    c = (norm(r1) - norm(r2)) ** 2 - d12 ** 2
    gamma12 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r1 += gamma12 * (r1_prev - r2_prev) / m1
    r2 += gamma12 * (r2_prev - r1_prev) / m2

    # rattle
    r10 = r1 - r0
    v_numerator = p1 / m1 + gamma01 * (r1_prev - r0) / (2 * dt * m1)
    v_denominator = r10 / (2 * dt * m1)
    gamma_vel01 = - v_numerator.dot(r10) / v_denominator.dot(r10)
    p1 += (gamma01 * (r1_prev - r0) + gamma_vel01 * (r1 - r0)) / (2 * dt)
    r12 = r1 - r2
    r12_prev = r1_prev - r2_prev
    v1_numerator = p1 / m1 + gamma12 * r12_prev / (2 * dt * m1)
    v2_numerator = p2 / m2 - gamma12 * r12_prev / (2 * dt * m2)
    v_numerator = v1_numerator - v2_numerator
    v1_denominator = r12 / (2 * dt * m1)
    v2_denominator = r12 / (2 * dt * m2)
    v_denominator = v1_denominator - v2_denominator
    gamma_vel12 = - v_numerator.dot(r12) / v_denominator.dot(r12)
    p1 += (gamma12 * r12_prev + gamma_vel12 * r12) / (2 * dt)
    p2 -= (gamma12 * r12_prev + gamma_vel12 * r12) / (2 * dt)

  return r1, r2, p1, p2, gamma01, gamma12, gamma_vel01, gamma_vel12

while step < nsteps:
  V1 = m1 * g * r1[1]
  V2 = m2 * g * r2[1]

  F1 = np.array([0.0, -m1 * g])
  F2 = np.array([0.0, -m2 * g])

  # calculate p(t+dt/2)
  p1 += 0.5 * dt * F1
  p2 += 0.5 * dt * F2

  # calculate r(t+dt)
  r1_prev = r1.copy()
  r2_prev = r2.copy()

  r1 += dt * p1 / m1
  r2 += dt * p2 / m2

  # print(f"r1: {r1}, r2: {r2}")

  # gamma01 = 1 / r1 * (d01 - (r1 + r0))
  # gamma12 = ((r2 - r1).linalg.norm() - d12) / (1 / m1 + 1 / m2) * (r1_prev - r2_prev).linalg.norm()

  F1 = np.array([0.0, -m1 * g])
  F2 = np.array([0.0, -m2 * g])

  # calculate p(t+dt)
  p1 += 0.5 * dt * F1
  p2 += 0.5 * dt * F2

  r1, r2, p1, p2, gamma01, gamma12, gamma_vel01, gamma_vel12 = restrain(r1_prev, r2_prev, r1, r2, p1, p2)

  if step % 100 == 0:
    print(f"step: {step}, r1: {r1}, r2: {r2}, p1: {p1}, p2: {p2}")

  if gamma01 != gamma01 or gamma12 != gamma12 or gamma_vel01 != gamma_vel01 or gamma_vel12 != gamma_vel12:
    break
  # gamma01 == nan or gamma12 == nan

  step += 1
  if step % ((1 / dt) / 10) == 0:
    ims = plot(r0, r1, r2, ims)

print("done")

ani = animation.ArtistAnimation(fig, ims, interval=1)
ani.save('test.gif')