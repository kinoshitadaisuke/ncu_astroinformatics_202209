#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 20:37:35 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing astropy module
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
unit_K = astropy.units.K
unit_micron = astropy.units.micron

# temperature of blackbody
T = 3000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of wavelength (from 10**-8 m to 10**-3 m)
wavelength_min = -8.0
wavelength_max = -3.0

# wavelength in micron
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=5001, \
                             dtype=numpy.longdouble) * 10**6 * unit_micron

# blackbody radiation
bb3000  = astropy.modeling.models.BlackBody (temperature=T)
bb_data = bb3000 (wavelength)

# printing blackbody radiation
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Blackbody radiation:')
print (f'{bb_data}')
