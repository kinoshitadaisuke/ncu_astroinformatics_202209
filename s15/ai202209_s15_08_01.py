#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/26 01:30:19 (CST) daisuke>
#

# import astropy module
import astropy.cosmology

# making your own cosmology model
cosmo = astropy.cosmology.FlatLambdaCDM (H0=70.0, Om0=0.30, Ob0=0.04)

# Hubble constant and density parameters
H0   = cosmo.H0
Ode0 = cosmo.Ode0
Om0  = cosmo.Om0
Odm0 = cosmo.Odm0
Ob0  = cosmo.Ob0
Og0  = cosmo.Ogamma0
Onu0 = cosmo.Onu0

Ot0  = Ode0 + Om0 + Og0 + Onu0

# Hubble time
hubble_time = cosmo.hubble_time

# printing parameters
print ("Parameters of your own cosmology model")
print ("  H0   =", H0)
print ("  Ode0 =", Ode0)
print ("  Om0  =", Om0)
print ("  Odm0 =", Odm0)
print ("  Ob0  =", Ob0)
print ("  Og0  =", Og0)
print ("  Onu0 =", Onu0)
print ("  Ot0  =", Ot0)
print ("  Hubble time =", hubble_time)
