import numpy as np
import scipy.special as sc

# circled 1
x = np.linspace(0, 1, 100)
mu = np.linspace(-1, 1, 8)
psi_array = np.array([])
for m in mu:
    if m > 0:
        psi = 1 - np.exp(- x / m)
    else:
        psi = 1 - np.exp(- (x - 1) / m)
    psi_array = np.concatenate((psi_array, psi))
psi_x = np.concatenate((x, psi_array)).reshape(9, 100).transpose()
np.savetxt("psi_x.txt", psi_x)
# circled 2
mu = np.linspace(-1, 1, 100)
x_array = np.array([0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 1.0])
psi_array = np.array([])
for x in x_array:
    psi1 = 1 - np.exp(- (x - 1) / mu[mu < 0])
    psi2 = 1 - np.exp(- x / mu[mu > 0])
    psi = np.concatenate((psi1, psi2))
    psi_array = np.concatenate((psi_array, psi))
psi_mu = np.concatenate((mu, psi_array)).reshape(8, 100).transpose()
np.savetxt("psi_mu.txt", psi_mu)
# phi_x
def inc_gamma(a, x):
        return sc.exp1(x) if a == 0 else sc.gamma(a)*sc.gammaincc(a, x)
x = np.linspace(0.01, 0.99, 100)
uicgamma1 = inc_gamma(0, 1-x)
uicgammax = inc_gamma(0, x)
#print(uicgamma1, uicgammax)
phi = 2 * np.pi * (2 - np.exp(x - 1) - np.exp(-x) + (1 - x) * uicgamma1 + x * uicgammax)
phi_x = np.concatenate((x, phi)).reshape(2, 100).transpose()
np.savetxt("phi_x.txt", phi_x)

