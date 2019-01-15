"""
We have at least 3 places where the trip fees for various trips
need to be kept in sync, so let's consolidate them in this
repository.
"""
from collections import namedtuple

TripFee = namedtuple('TripFee', ('Type', 'Amount'))

ICE_TRIP = TripFee('Ice Climbing', 20)
SKI_TRIP = TripFee('Ski', 15)
WS_TRIP = TripFee('Winter School', 5)
