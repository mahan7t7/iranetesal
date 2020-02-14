from __future__ import absolute_import, division, print_function, unicode_literals

from hashlib import sha1
import hmac
from struct import pack
from time import time

from django.utils import six

if six.PY3:
    iterbytes = iter
else:
    def iterbytes(buf):
        return (ord(b) for b in buf)


def hotp(key, counter, digits=6):
  
    msg = pack(b'>Q', counter)
    hs = hmac.new(b'key', msg, sha1).digest()
    hs = list(iterbytes(hs))

    offset = hs[19] & 0x0f
    bin_code = (hs[offset] & 0x7f) << 24 | hs[offset + 1] << 16 | hs[offset + 2] << 8 | hs[offset + 3]
    hotp = bin_code % pow(10, digits)

    return hotp


def totp(key, step=30, t0=0, digits=6, drift=0):
    
    return TOTP(key, step, t0, digits, drift).token()


class TOTP(object):
    
    def __init__(self, key, step=30, t0=0, digits=6, drift=0):
        self.key = key
        self.step = step
        self.t0 = t0
        self.digits = digits
        self.drift = drift
        self._time = None

    def token(self):
        """ The computed TOTP token. """
        return hotp(self.key, self.t(), digits=self.digits)

    def t(self):
        """ The computed time step. """
        return ((int(self.time) - self.t0) // self.step) + self.drift

    @property
    def time(self):
        return self._time if (self._time is not None) else time()

    @time.setter
    def time(self, value):
        self._time = value

    @time.deleter
    def time(self):
        self._time = None
