# requests-mauth

requests-mauth is a python requests (http://docs.python-requests.org/en/latest/) Authentication implementation
for Medidata's _MAuth_ authentication system.

## Pre-requisites ##

To use MAuth authentication you will need:

* An MAuth APP ID
* An MAuth private key (with the public key registered with Medidata's MAuth server)


## Using ##

    import requests
    from requests_mauth import MAuth

    APP_UUID = '55dc88ec-c109-11e1-84f6-1231381b7d70'
    private_key = open("private.key","r").read()

    mauth = MAuth(APP_UUID, private_key)

    
    # Call an MAuth protected resource, in this case an iMedidata API 
    # listing the studies for a particular user
    user_uuid = '10ac3b0e-9fe2-11df-a531-12313900d531'
    url = "https://innovate.imedidata.com/api/v2/users/%s/studies.json" % user_uuid

    # Make the requests call, passing the auth client
    result = requests.get(url, auth=mauth)
    
    # Print results
    if result.status_code == 200:
        print([r['uuid'] for r in result.json()['studies']])
    print(result.text)
    
Build Status
------------
* master - [![Build Status](https://travis-ci.org/mdsol/requests-mauth.svg?branch=master)](https://travis-ci.org/mdsol/requests-mauth.svg?branch=master)