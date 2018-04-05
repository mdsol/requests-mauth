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

## User Impersonation ##

A user can be impersonated using the optional `user_uuid` argument to the client instantiation, this will add th

```python

    import requests
    from requests_mauth import MAuth

    APP_UUID = '55dc88ec-c109-11e1-84f6-1231381b7d70'
    private_key = open("private.key","r").read()
    user_uuid = '10ac3b0e-9fe2-11df-a531-12313900d531'
    mauth = MAuth(APP_UUID, private_key, user_uuid=user_uuid)

```

Development
-----------
We use [travis](https://travisci.com) for automated CI of the code (and status checks are required to pass prior to PR merges being accepted).  
We use travis to deploy updated versions to PyPI (only from `master`)

For local development (cross version) we use [tox](http://tox.readthedocs.io/en/latest/) with [pyenv](https://github.com/pyenv/pyenv) to automate the running of unittests against different python versions in virtualised python environments.   

To setup your environment:
1. Install Python
1. Install Pyenv
   ```bash
   $ brew update
   $ brew install pyenv
   ```
1. Install Pyenv versions for the Tox Suite (note that some of these will have changed _ad interim_)
   ```bash
   $ pyenv install 2.7.13 3.4.6 3.5.3 3.6.1
   ```
1. Install Tox 
   ```bash
   $ pip install tox tox-pyenv 
   ```
1. Setup the local project versions (one for each env in the `envlist`)
   ```bash
    $ pyenv local 2.7.13 3.4.6 3.5.3 3.6.1
   ```
1. Make any changes, update the tests and then run tests with `tox`
   ```bash
    Name                         Stmts   Miss  Cover
    ------------------------------------------------
    requests_mauth/__init__.py       3      0   100%
    requests_mauth/client.py        31      0   100%
    requests_mauth/rsa_sign.py      34      0   100%
    ------------------------------------------------
    TOTAL                           68      0   100%
    stats runtests: commands[1] | coverage html
    _________________________________________________________________________________________________________ summary __________________________________________________________________________________________________________
      clean: commands succeeded
      py27: commands succeeded
      py34: commands succeeded
      py35: commands succeeded
      py36: commands succeeded
      stats: commands succeeded
      congratulations :)
   ```
1. Coverage report can be viewed using `open htmlcov/index.html`
1. Push your changes and create a PR to `master`
1. Once the PR is complete, tag the branch and push it to github, this will trigger Travis to deploy to PyPI (make sure the version is consistent)
   ```bash
   $ git checkout master
   $ git pull
   $ git tag -a 1.0.2 -m "Requests MAuth 1.0.2"
   $ git push --tags
   ```

Build Status
------------
* master - [![Build Status](https://travis-ci.org/mdsol/requests-mauth.svg?branch=master)](https://travis-ci.org/mdsol/requests-mauth.svg?branch=master)

