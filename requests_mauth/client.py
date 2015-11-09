# -*- coding: UTF-8 -*-
__author__ = 'isparks'

import requests
import time
from rsa_sign import RSARawSigner
from urlparse import urlparse

class MAuth(requests.auth.AuthBase):
    """Custom requests authorizer for MAuth"""
    def __init__(self, app_uuid, private_key_data):
        self.app_uuid = app_uuid
        self.signer = RSARawSigner(private_key_data)

    def __call__(self, r):
        """Call override, the entrypoint for a custom auth object"""
        r.headers.update(self.make_headers(r))
        return r

    def make_headers(self, r):
        """Make headers for the request."""
        # Split the path from the scheme, query string etc
        url_path = urlparse(r.url).path
        signature, secs = self.make_signature_string(r.method, url_path, r.body)
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

        vals = dict(verb=verb,
                    url_path=url_path,
                    body=body or '',
                    app_uid=self.app_uuid,
                    seconds_since_epoch=seconds_since_epoch)

        string_to_sign = '{verb}\n{url_path}\n{body}\n{app_uid}\n{seconds_since_epoch!s}'.format(**vals)
        return string_to_sign, seconds_since_epoch


