#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/28 13:33:55 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_micron   = astropy.units.micron
u_Hz       = astropy.units.Hz
u_GHz      = astropy.units.GHz
u_spectral = astropy.units.spectral ()

# wavelength
wl = 850 * u_micron

# frequency corresponding to EM wave of wavelength 850 micron
freq     = wl.to (u_Hz, equivalencies=u_spectral)
freq_GHz = wl.to (u_GHz, equivalencies=u_spectral)

# printing result
print (f'wavelength = {wl:g}  ==>  frequency = {freq:g} = {freq_GHz:g}')
