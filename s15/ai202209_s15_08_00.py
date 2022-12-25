#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/26 01:26:10 (CST) daisuke>
#

# import astropy module
import astropy.cosmology

# use preloaded cosmology model
cosmo_planck2015 = astropy.cosmology.Planck15

# Hubble constant and density parameters
H0   = cosmo_planck2015.H0
Ode0 = cosmo_planck2015.Ode0
Om0  = cosmo_planck2015.Om0
Odm0 = cosmo_planck2015.Odm0
Ob0  = cosmo_planck2015.Ob0
Og0  = cosmo_planck2015.Ogamma0
Onu0 = cosmo_planck2015.Onu0

Ot0  = Ode0 + Om0 + Og0 + Onu0

# printing parameters
print ("Parameters from Planck 2015")
print ("  H0   =", H0)
print ("  Ode0 =", Ode0)
print ("  Om0  =", Om0)
print ("  Odm0 =", Odm0)
print ("  Ob0  =", Ob0)
print ("  Og0  =", Og0)
print ("  Onu0 =", Onu0)
print ("  Ot0  =", Ot0)
