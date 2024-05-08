import numpy as np

plotfilename = 'double_pendulum.dat'

nsteps = 1000
dt = 0.01
g = 9.8
l1 = 2.0
l2 = 1.0

m1 = 1.0
m2 = 1.0

theta1 = 0
theta2 = 0

theta1dot = 1.0
theta2dot = 0.0

def plot(step, theta1, theta2, file):
  file.write(f"# Step: {step}\n")
  file.write(f"0 0\n")
  file.write(f"{l1 * np.sin(theta1)} {l1 * np.cos(theta1)}\n")
  file.write(f"{l1 * np.sin(theta1) + l2 * np.sin(theta2)} {l1 * np.cos(theta1) + l2 * np.cos(theta2)}\n\n\n")

plotfile = open(plotfilename, 'w')

plot(0, theta1, theta2, plotfile)

for i in range(nsteps):
  dLdtheta1 = m2 * l1 * l2 * theta1dot * theta2dot * np.sin(theta2 - theta1) - (m1 - m2) * g * l1 * np.sin(theta1)
  dLdtheta2 = m2 * l1 * l2 * theta1dot * theta2dot * np.sin(theta1 - theta2) - m2 * g * l2 * np.sin(theta2)

  theta1dot += dLdtheta1 * dt / (2 * m1)
  theta2dot += dLdtheta2 * dt / (2 * m2)

  theta1 += theta1dot * dt
  theta2 += theta2dot * dt

  dLdtheta1 = m2 * l1 * l2 * theta1dot * theta2dot * np.sin(theta2 - theta1) - (m1 - m2) * g * l1 * np.sin(theta1)
  dLdtheta2 = m2 * l1 * l2 * theta1dot * theta2dot * np.sin(theta1 - theta2) - m2 * g * l2 * np.sin(theta2)

  theta1dot += dLdtheta1 * dt / (2 * m1)
  theta2dot += dLdtheta2 * dt / (2 * m2)
  if i % 10 == 0:
    plot(i + 1, theta1, theta2, plotfile)

plotfile.close()