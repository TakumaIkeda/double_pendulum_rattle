import numpy as np

plotfilename = 'double_pendulum.dat'

nsteps = 10000
dt = 0.01
g = 9.8
l1 = 2.0
l2 = 1.0

m1 = 1.0
m2 = 1.0

theta1 = np.pi / 2
theta2 = np.pi / 2

theta1dot = 1.0
theta2dot = -5.0

def plot(step, theta1, theta2, file):
  file.write(f"# Step: {step}\n")
  file.write(f"0 0\n")
  file.write(f"{l1 * np.sin(theta1)} {-l1 * np.cos(theta1)}\n")
  file.write(f"{l1 * np.sin(theta1) + l2 * np.sin(theta2)} {-l1 * np.cos(theta1) - l2 * np.cos(theta2)}\n\n\n")

def calc_acceleration(theta1, theta2, theta1dot, theta2dot):
  coef1 = (m1 + m2) * l1 * l1
  coef2 = m2 * l1 * l2 * np.cos(theta1 - theta2)
  coef3 = -m2 * l1 * l2 * np.sin(theta1 - theta2) * theta2dot * theta2dot - (m1 + m2) * g * l1 * np.sin(theta1)
  coef4 = m2 * l1 * l2 * np.cos(theta1 - theta2)
  coef5 = m2 * l2 * l2
  coef6 = m2 * l1 * l2 * np.sin(theta1 - theta2) * theta1dot * theta1dot - m2 * g * l2 * np.sin(theta2)

  return (coef3 * coef5 - coef2 * coef6) / (coef1 * coef5 - coef2 * coef4), (coef3 * coef4 - coef1 * coef6) / (coef2 * coef4 - coef1 * coef5)

plotfile = open(plotfilename, 'w')

plot(0, theta1, theta2, plotfile)

for i in range(nsteps):
  theta1dotdot, theta2dotdot = calc_acceleration(theta1, theta2, theta1dot, theta2dot)

  theta1dot += theta1dotdot * dt / 2
  theta2dot += theta2dotdot * dt / 2

  theta1 += theta1dot * dt
  theta2 += theta2dot * dt

  theta1dotdot, theta2dotdot = calc_acceleration(theta1, theta2, theta1dot, theta2dot)

  theta1dot += theta1dotdot * dt / 2
  theta2dot += theta2dotdot * dt / 2

  if i % 10 == 0:
    plot(i + 1, theta1, theta2, plotfile)

plotfile.close()