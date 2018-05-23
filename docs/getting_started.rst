Getting Started
***************

Installation
------------
Install using `pip` in the usual way

Install with pip::

    $ pip install requests-mauth

Or directly from github with::

    $ pip install git+https://github.com/mdsol/requests_mauth.git

Usage
-----

In order to be able to utilise this you will need to have setup your MAuth Credentials.  To do so:

1. Generate a keyset (see :doc:`mauth_setup`)
2. Create a `MAuth` instance::

    mauth = MAuth(app_uuid='your_app_uuid', private_key_data='your_private_key_data')
3. Add the `MAuth` instance to your request; this can be done inline or by using a requests.Session::

    # Using the request authentication request signer inline
    response = requests.get('/some/url.json', auth=mauth)

    # Using a requests.Session
    client = requests.Session()
    client.auth = mauth
    response = client.get('/some/url.json')



