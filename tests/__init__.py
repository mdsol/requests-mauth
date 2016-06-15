# -*- coding: utf-8 -*-
__author__ = 'isparks'

import unittest
from . import client_test

def requests_mauth_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(client_test)
    return suite