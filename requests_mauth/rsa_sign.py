# -*- coding: utf-8 -*-
__author__ = 'isparks'

# This module exists to reproduce, with the rsa library, the raw signature required by MAuth
# which in OpenSSL is created with private_encrypt(hash). It provides an RSA sign class built from
# code that came from https://www.dlitz.net/software/pycrypto/api/current/ no copyright of that original
# code is claimed.

from hashlib import sha512
from rsa import common, core, transform, PrivateKey

#---- Original code from RSA ------------------------------------------------------------------------------------------

def byte_literal(s):
    return s

b = byte_literal

#----------------------------------------------------------------------------------------------------------------------


class RSARawSigner(object):
    def __init__(self, private_key_data):
        self.pk = PrivateKey.load_pkcs1(private_key_data, 'PEM')

    def sign(self, string_to_sign):
        """Sign the data in a emulation of the OpenSSL private_encrypt method"""
        hashed = sha512(string_to_sign.encode('US-ASCII')).hexdigest()
        keylength = common.byte_size(self.pk.n)
        padded = self.pad_for_signing(hashed, keylength)

        payload = transform.bytes2int(padded)
        encrypted = core.encrypt_int(payload, self.pk.d,  self.pk.n)
        signature = transform.int2bytes(encrypted, keylength).encode('base64').replace('\n','')
        return signature

    def pad_for_signing(self, message, target_length):
        r'''Pulled from rsa pkcs1.py,

        Pads the message for signing, returning the padded message.

        The padding is always a repetition of FF bytes.

        :return: 00 01 PADDING 00 MESSAGE

        >>> block = _pad_for_signing('hello', 16)
        >>> len(block)
        16
        >>> block[0:2]
        '\x00\x01'
        >>> block[-6:]
        '\x00hello'
        >>> block[2:-6]
        '\xff\xff\xff\xff\xff\xff\xff\xff'

        '''

        max_msglength = target_length - 11
        msglength = len(message)

        if msglength > max_msglength: #pragma: no cover
            raise OverflowError('%i bytes needed for message, but there is only'
                ' space for %i' % (msglength, max_msglength))

        padding_length = target_length - msglength - 3

        return b('').join([b('\x00\x01'),
                        padding_length * b('\xff'),
                        b('\x00'),
                        message])
