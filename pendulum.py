import numpy as np

l = 1.0
theta = np.pi / 2 * 3
thetadot = np.pi * 3 / 2
m1 = 1.0
g = 9.8

dt = 0.01
step = 0

coordinatefile = open("coordinate.dat", "w")
potentialfile = open("potential.dat", "w")
kineticfile = open("kinetic.dat", "w")
lagrangianfile = open("lagrangian.dat", "w")
hamiltonianfile = open("hamiltonian.dat", "w")
sudoLagrangianfile = open("sudoLagrangian.dat", "w")

def plot(theta, step, V, T):
    if step % 10 == 0:
      coordinatefile.write(f"0 0\n{l * np.sin(theta)} {-l * np.cos(theta)}\n\n\n")
    potentialfile.write(f"{step * dt} {V}\n")
    kineticfile.write(f"{step * dt} {T}\n")
    lagrangianfile.write(f"{step * dt} {T - V}\n")
    hamiltonianfile.write(f"{step * dt} {T + V}\n")
    sudoLagrangianfile.write(f"{step * dt} {T + m1 * g * l * (1 - np.cos(np.pi / 2))}\n")



# plot(theta, step, -m1 * g * l * (1 - np.cos(theta)), 0.5 * m1 * ((l * thetadot * np.cos(theta)) ** 2 + (l * thetadot * np.sin(theta)) ** 2))

while step < 1000:
  theta2dot = -g / l * np.sin(theta)
  thetadot += theta2dot * dt / 2
  theta += thetadot * dt
  theta2dot = -g / l * np.sin(theta)
  thetadot += theta2dot * dt / 2

  V = m1 * g * l * (1 - np.cos(theta))
  T = m1 * ((l * thetadot * np.cos(theta)) ** 2 + (l * thetadot * np.sin(theta)) ** 2) / 2

  step += 1
  # if step % 10 == 0:
  plot(theta, step, V, T)

coordinatefile.close()
potentialfile.close()
kineticfile.close()
lagrangianfile.close()
hamiltonianfile.close()
