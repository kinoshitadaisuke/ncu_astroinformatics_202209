#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 16:12:25 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# units
u_m = astropy.units.m

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# location of observer: Greenwich Observatory
longitude = '-0d00m05s'
latitude  = '+51d28m40s'
height    = 45.0 * u_m

# making a location object using Astropy
location = astropy.coordinates.EarthLocation.from_geodetic (lon=longitude, \
                                                            lat=latitude, \
                                                            height=height)

# making an observer object
observer = astroplan.Observer (location=location, name='Greenwich', \
                               timezone='UTC')

# printing created observer object
print (observer)

# end of evening twilight
twilight_evening_guess = astropy.time.Time ('2022-11-07 18:00:00', \
                                            format='iso', scale='utc')
twilight_evening = observer.twilight_evening_astronomical \
    (twilight_evening_guess, which='nearest', n_grid_points=500)

# printing end of evening twilight
print (f'end of evening twilight = JD {twilight_evening.jd}', \
       f'= {twilight_evening.iso}')

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', twilight_evening, \
                                    location=location)

# conversion from equatorial into horizontal
altaz     = astropy.coordinates.AltAz (obstime=twilight_evening, \
                                       location=location)
sun_altaz = sun.transform_to (altaz)
sun_alt   = sun_altaz.alt
sun_az    = sun_altaz.az

# printing altitude and azimuth
print (f'position of the Sun at the end of evening twilight:')
print (f'  alt = {sun_alt}')
print (f'  az  = {sun_az}')
