import sys

DEFAULT_SIZE = 3

if sys.platform == "linux":
    OVERBAR = u'\u203E'
elif sys.platform == 'mac':
    OVERBAR = u'\u0305'