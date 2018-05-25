# -*- coding: utf-8 -*-
__author__ = 'isparks'

# This module exists to reproduce, with the rsa library, the raw signature required by MAuth
# which in OpenSSL is created with private_encrypt(hash). It provides an RSA sign class built from
# code that came from https://www.dlitz.net/software/pycrypto/api/current/ no copyright of that original
# code is claimed.

from hashlib import sha512
from rsa import common, core, transform, PrivateKey
import base64


def make_bytes(val):
    """Ensure in python 2/3 we are working with bytes when we need to

    :param str val: The supplied value (string-like)
    """
    try:
        if isinstance(val, unicode):
            return val.encode('utf-8')
    except NameError:
        if isinstance(val, bytes):
            return val
        elif isinstance(val, str):
            return val.encode('utf-8')
    return val


class RSARawSigner(object):
    """
    Implements the equivalent of the OpenSSL private_encrypt method
    """
    def __init__(self, private_key_data):
        """

        :param private_key_data:
        """
        self.private_key_data = private_key_data
        self.pk = PrivateKey.load_pkcs1(private_key_data, 'PEM')

    def sign(self, string_to_sign):
        """Sign the data in a emulation of the OpenSSL private_encrypt method

        :param str string_to_sign: The string to Sign using the RSA private_encrypt method
        :rtype: str
        """
        string_to_sign = make_bytes(string_to_sign)
        hashed = sha512(string_to_sign).hexdigest().encode('US-ASCII')
        keylength = common.byte_size(self.pk.n)
        padded = self.pad_for_signing(hashed, keylength)
        padded = make_bytes(padded)
        payload = transform.bytes2int(padded)
        encrypted = core.encrypt_int(payload, self.pk.d, self.pk.n)
        signature = transform.int2bytes(encrypted, keylength)
        signature = base64.b64encode(signature).decode('US-ASCII').replace('\n', '')
        return signature

    def pad_for_signing(self, message, target_length):
        """Pulled from rsa pkcs1.py,

        Pads the message for signing, returning the padded message.

        The padding is always a repetition of FF bytes::

            00 01 PADDING 00 MESSAGE

        Sample code::

            >>> block = RSARawSigner.pad_for_signing('hello', 16)
            >>> len(block)
            16
            >>> block[0:2]
            '\x00\x01'
            >>> block[-6:]
            '\x00hello'
            >>> block[2:-6]
            '\xff\xff\xff\xff\xff\xff\xff\xff'

        :param message: message to pad in readiness for signing
        :type message: str
        :param target_length: target length for padded string
        :type target_length: int

        :rtype: str
        :return: suitably padded string
        """

        max_msglength = target_length - 11
        msglength = len(message)

        if msglength > max_msglength:  # pragma: no cover
            raise OverflowError('%i bytes needed for message, but there is only'
                                ' space for %i' % (msglength, max_msglength))

        padding_length = target_length - msglength - 3

        return b''.join([b'\x00\x01',
                         padding_length * b'\xff',
                         b'\x00',
                         message])
