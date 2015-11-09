# -*- coding: UTF-8 -*-
__author__ = 'isparks'

import requests
import datetime
import time
import hmac
import hashlib
import base64
from rsa_sign import RSARawSigner

SECONDS_IN_24_HOURS = 24 * 60 * 60

def isodatetime(dt):
    """Takes a date, returns ISO8601 date/time format"""
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

def isodate(dt):
    """Takes a date, returns ISO8601 date format"""
    return dt.strftime('%Y-%m-%d')


class MAuth(requests.auth.AuthBase):
    """Custom requests authorizer for MAuth"""
    def __init__(self, base_url, app_uuid, private_key_data):
        self.base_url = base_url
        self.app_uuid = app_uuid
        self.signer = RSARawSigner(private_key_data)

    def __call__(self, r):
        """Call is made like:
           requests.get(url, auth=MyAuth())
        """
        r.headers.update(self.make_headers(r))
        return r

    def make_url(self, resource_url):
        """
        Return full URL
        """
        url = u"%s%s" % (self.base_url, resource_url,)
        return url

    def make_headers(self, r):
        """Make headers for the request."""

        signature, secs = self.make_signature_string(r.method, r.url, r.body)
        signed = self.signer.sign(signature)
        headers = self.make_authentication_headers(signed, secs)
        return headers

    def make_authentication_headers(self, signed_string, seconds_since_epoch):
        """Makes headers of the form

            x-mws-authentication: MWS {app_id}:{signed_string}
            x-mws-time: {time_since_epoch}
        """
        return {'X-MWS-Authentication' : 'MWS %s:%s' % (self.app_uuid,signed_string,),
                'X-MWS-Time' : str(seconds_since_epoch),
                'Content-Type': 'application/json;charset=utf-8',
                }
        return headers

    def make_signature_string(self,  verb, url_path, body, seconds_since_epoch=None):
        """Makes a signature string for signing of the form:

            string_to_sign =
                Http_Verb + "\n" +
                Resource URL path (no host, port or query string; first "/" is included) + "\n" +
                message_body_string + "\n" +
                app_uuid + "\n" +
                Current_Seconds_Since_Epoch

           Returns the encoded string and the seconds-since-epoch used in request.
           Providing the seconds_since_epoch is helpful for testing, especially in checking
           against the output of the ruby mauth command-line client.

        """
        if seconds_since_epoch is None:
            seconds_since_epoch = int(time.time())

        vals = dict(verb=verb, url_path=url_path, body=body, app_uid=self.app_uuid, seconds_since_epoch=seconds_since_epoch)
        string_to_sign = '{verb}\n{url_path}\n{body}\n{app_uid}\n{seconds_since_epoch!s}'.format(**vals)
        return string_to_sign, seconds_since_epoch



