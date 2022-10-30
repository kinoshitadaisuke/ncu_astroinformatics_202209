#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/28 16:08:10 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_nm         = astropy.units.nm
u_km         = astropy.units.km
u_sec        = astropy.units.s
u_km_per_sec = u_km / u_sec
u_spectral   = astropy.units.spectral ()

# wavelength of H-alpha at rest frame
wl_rest = 656.28 * u_nm

# observed wavelength of H-alpha
wl_obs = 656.12 * u_nm

# calculation of velocity
H_alpha  = astropy.units.doppler_optical (wl_rest)
velocity = wl_obs.to (u_km_per_sec, equivalencies=H_alpha)

# printing result
print (f'rest frame wavelength  = {wl_rest}')
print (f'observed wavelength    = {wl_obs}')
print (f'line-of-sight velocity = {velocity}')
