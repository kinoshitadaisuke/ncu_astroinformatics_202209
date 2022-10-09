#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/09 13:58:37 (CST) daisuke>
#

# importing scipy module
import scipy.constants

#
# some more physical constants
#

# atomic mass unit
amu = scipy.constants.physical_constants['atomic mass constant']

# Bohr radius
a_0 = scipy.constants.physical_constants['Bohr radius']

# Boltzmann constant
k = scipy.constants.physical_constants['Boltzmann constant']

# electron mass
m_e = scipy.constants.physical_constants['electron mass']

# electron volt
eV = scipy.constants.physical_constants['electron volt']

# Planck constant
h = scipy.constants.physical_constants['Planck constant']

# proton mass
m_p = scipy.constants.physical_constants['proton mass']

# speed of light in vacuum
c = scipy.constants.physical_constants['speed of light in vacuum']

# standard atmospheric pressure
atm = scipy.constants.physical_constants['standard atmosphere']

# electric permittivity in vacuum
epsilon_0 = scipy.constants.physical_constants['vacuum electric permittivity']

# magnetic permeability in vacuum
mu_0 = scipy.constants.physical_constants['vacuum mag. permeability']

# printing constants
print (f'amu  = {amu[0]:g} +/- {amu[2]:g} [{amu[1]}]')
print (f'a_0  = {a_0[0]:g} +/- {a_0[2]:g} [{a_0[1]}]')
print (f'k    = {k[0]:g} +/- {k[2]:g} [{k[1]}]')
print (f'm_e  = {m_e[0]:g} +/- {m_e[2]:g} [{m_e[1]}]')
print (f'eV   = {eV[0]:g} +/- {eV[2]:g} [{eV[1]}]')
print (f'h    = {h[0]:g} +/- {h[2]:g} [{h[1]}]')
print (f'm_p  = {m_p[0]:g} +/- {m_p[2]:g} [{m_p[1]}]')
print (f'c    = {c[0]:g} +/- {c[2]:g} [{c[1]}]')
print (f'atm  = {atm[0]:g} +/- {atm[2]:g} [{atm[1]}]')
print (f'eps0 = {epsilon_0[0]:g} +/- {epsilon_0[2]:g} [{epsilon_0[1]}]')
print (f'mu0  = {mu_0[0]:g} +/- {mu_0[2]:g} [{mu_0[1]}]')
