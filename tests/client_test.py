# -*- coding: UTF-8 -*-
__author__ = 'isparks'

import unittest
from requests_mauth.client import MAuth
import time
from requests import Request
import os
import json


class RequestMock(object):
    """Simple mock for a request object"""
    def __init__(self, method, url, body):
        self.method = method
        self.url = url
        self.body = body


class MAuthBaseTest(unittest.TestCase):
    def setUp(self):
        self.app_id = "5ff4257e-9c16-11e0-b048-0026bbfffe5e"

        # Note, private key used here is just a dummy. Not registered to anythiung, cannot sign live requests.
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, "test_mauth.priv.key"),'r') as f:
            example_private_key = f.read()
        self.client = MAuth(self.app_id, example_private_key)


class TestStringToSign(MAuthBaseTest):
    def test_string_to_sign(self):
        expected = "GET" + "\n" \
            + "/studies/123/users" + "\n" \
            +"\n" \
            + self.app_id \
            + "\n" \
            +  "1309891855"

        epoch = 1309891855
        mr = RequestMock("GET","/studies/123/users","")
        tested = self.client.make_signature_string(mr.method, mr.url, mr.body, seconds_since_epoch=epoch)
        self.assertEqual(tested[0], expected)

        # Test we got the epoch we put in, back again
        self.assertEqual(tested[1],epoch)

    def test_string_to_sign_binary_body(self):
        expected = "GET" + "\n" \
            + "/studies/123/users" + "\n" \
            +'{"key": "data"}\n' \
            + self.app_id \
            + "\n" \
            +  "1309891855"

        epoch = 1309891855
        mr = RequestMock("GET","/studies/123/users",json.dumps( { 'key': 'data' } ).encode('utf8'))
        tested = self.client.make_signature_string(mr.method, mr.url, mr.body, seconds_since_epoch=epoch)
        self.assertEqual(tested[0], expected)

    def test_string_to_sign_no_epoch(self):
        """Test that epoch is supplied for us if we don't"""

        # Get time before
        expected = int(time.time())

        # Don't provide epoch
        mr = RequestMock("GET","/studies/123/users","")
        tested = self.client.make_signature_string(mr.method, mr.url, mr.body)[0]
        tested_epoch = int(tested.split('\n')[4])

        # Generated epoch should be after or equal to the time before the call
        self.assertGreaterEqual(tested_epoch, expected)


class TestSign(MAuthBaseTest):
    def test_sign(self):
        """
        Test that signing a string doesn't throw an error and signature correct
        """
        tested = self.client.signer.sign("Hello world")
        self.assertEqual(tested, 'F/GAuGYEykrtrmIE/XtETSi0QUoKxUwwTXljT1tUiqNHmyH2NRhKQ1flqusaB7H6bwPBb+FzXzfmiO32lJs6SxMjltqM/FjwucVNhn1BW+KXFnZniPh3M0+FwwspksX9xc/KcWEPebtIIEM5cX2rBl43xlvwYtS/+D+obo1AVPv2l5qd+Gwl9b61kYF/aoPGx+bVnmWZK8e8BZxZOjjGjmQAOYRYgGWzolLLnzIZ6xy6efY3D9jPXXDqgnqWQvwLStkKJIydrkXUTd0m36X6mD00qHgI7xoYSLgqxNSg1EgO8yuette8BKl9D+YbIEJ3xFnaZmCfVGks0M9tmZ2PXg==')

    def test_sign_unicode(self):
        """
        Test that signing a string with non-ASCII characters doesn't throw an error and signature correct
        """
        tested = self.client.signer.sign("こんにちはÆ")
        self.assertEqual(tested, 'cHrT3G7zCA2aRcY5jtvNlm0orafBOn924rQ9aSQS1lvNCwbg/LMnTsV+jHZUtOyDFSvErBwd9ga1FrsjOQDfhNoU1K+pVQ11nHU23cHQi0bsYByKPIDh1jMW4wNtP+A7Z/Xh0CIESBc+SaeIjPznMunocwci34kN4AXWudkZ2+xZxqfZiX6TVrwmREppsgoZD2ODVt6FtnBvcGd0sRAa9A3Iy+EaB8wOM5kaUyusfGcxeCYuCGN1FHjd1AkBkm2I4wbsxQInKDyYQXjMv3fA5oMw4nxhL/AJzUx3xWWCG5pub1/YB3jWwQgtGjpxvb5LhHT9S/JtuT8RU01JukC8dQ==')

class TestMakeAuthHeaders(MAuthBaseTest):
    def test_headers(self):
        """Test making of auth headers"""
        signed_string = 'SomeSignedString'
        etime = 999
        expected = {'X-MWS-Authentication': '', 'X-MWS-Time': etime }

        tested = self.client.make_authentication_headers(signed_string, etime)
        self.assertTrue(tested['X-MWS-Authentication'], 'MWS %s:%s' % (self.app_id, signed_string) )
        self.assertTrue(tested['X-MWS-Time'], str(etime) )


class TestCall(MAuthBaseTest):
    """Ensure that the __call__ method is being properly exercised"""
    def test_get(self):
        user_uuid = '10ac3b0e-9fe2-11df-a531-12313900d531'
        url = "https://innovate.imedidata.com/api/v2/users/%s/studies.json" % user_uuid
        r = Request('GET', url, auth=self.client).prepare()
        authentication_header = r.headers['X-MWS-Authentication']
        header_app_id = authentication_header.split(':')[0]
        self.assertEqual('MWS ' + self.app_id, header_app_id)
