#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/09 13:58:31 (CST) daisuke>
#

# importing scipy module
import scipy.constants

#
# some physical constants
#

# speed of light in vacuum
c = scipy.constants.c

# Planck constant
h = scipy.constants.h

# gravitational constant
G = scipy.constants.G

# Avogadro constant
N_A = scipy.constants.N_A

# Boltzmann constant
k = scipy.constants.k

# Stefan-Boltzmann constant
sigma = scipy.constants.sigma

# electron mass
m_e = scipy.constants.m_e

# proton mass
m_p = scipy.constants.m_p

# printing constants
print (f'c     = {c:g}')
print (f'h     = {h:g}')
print (f'G     = {G:g}')
print (f'N_A   = {N_A:g}')
print (f'k     = {k:g}')
print (f'sigma = {sigma:g}')
print (f'm_e   = {m_e:g}')
print (f'm_p   = {m_p:g}')
