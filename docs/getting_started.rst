Getting Started
***************

Below you can find some information and examples on getting started using the framework.

Installation
------------
Install using `pip` in the usual way

Install with pip::

    $ pip install requests-mauth

Or directly from github with::

    $ pip install git+https://github.com/mdsol/requests_mauth.git


Simple signing of Requests
--------------------------

In order to be able to utilise this you will need to have setup your MAuth Credentials.  To do so:

1. Generate and register an Application (see :doc:`mauth_setup` for instructions)

2. Create a `MAuth` instance using the `requests_mauth.MAuth` class::

    from requests_mauth import MAuth

    mauth = MAuth(app_uuid='your_app_uuid', private_key_data='your_private_key_data')
3. Add the `MAuth` instance to your request; this can be done inline with the `requests.verb` action or by using a `requests.Session`::

    # Using the request authentication request signer inline
    response = requests.get('/some/url.json', auth=mauth)

    # Using a requests.Session
    client = requests.Session()
    client.auth = mauth
    response = client.get('/some/url.json')

See :doc:`examples` for more examples.

Configuration
-------------
The module expects to have the following variables passed (both as strings)
  *  Application UUID - `app_uuid`
  *  Private Key Data - `private_key_data`

These are supplied as 12-factor environment variables.

Authenticating Incoming Requests
--------------------------------
This module is purely for signing requests to MAuth enabled services - it is not a fully fledged middleware module.

This module does not attempt to authenticate incoming requests.

For an example of an application that does this see:
  * Flask-MAuth_ (Python)

Other Client Libraries that include middleware capabilities:
  * mauth-client-dotnet_ (DotNet)
  * mauth-client-ruby_ (Ruby)

.. _Flask-MAuth: http://github.com/mdsol/flask-mauth
.. _mauth-client-dotnet: https://github.com/mdsol/mauth-client-dotnet
.. _mauth-client-ruby: https://github.com/mdsol/mauth-client-ruby