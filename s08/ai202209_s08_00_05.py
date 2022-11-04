#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/04 15:58:51 (CST) daisuke>
#

# importing astroplan module
import astroplan

# making an observer object
observer = astroplan.Observer.at_site ('Palomar', timezone='US/Pacific')

# printing created observer object
print (observer)
