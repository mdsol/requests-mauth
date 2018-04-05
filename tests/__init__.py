# -*- coding: utf-8 -*-
__author__ = 'isparks'

import unittest
from . import test_client

def requests_mauth_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_client)
    return suite