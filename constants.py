import sys

DEFAULT_SIZE = 3
ASPECT_RATIO = 1.7
if sys.platform == "linux":
    OVERBAR = u'\u203E'
elif sys.platform == 'mac':
    OVERBAR = u'\u0305'