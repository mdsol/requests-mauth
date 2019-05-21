Example Usage
=============

Accessing an iMedidata User Endpoint
------------------------------------

This sample shows the code to make a call to the `iMedidata API <http://developer.imedidata.com/desktop/homepage.htm>`_.
In this case we retrieve the user details using the `Listing User Account Details <http://developer.imedidata.com/desktop/ActionTopics/Users/Listing_User_Account_Details.htm>`_ API call.

Note the extracted method `generate_signer` for creating a MAuth Request signer using either the key text or a reference to a Private Key file.


.. code-block:: python

    import requests

    from requests_mauth import MAuth

    def generate_signer(app_uuid, private_key_file=None, private_key_string=None):
        """
        Generate a MAUTH instance
        :param str app_uuid: Application UUID
        :param str private_key_file: name of the Private Key File
        :param str private_key_string: content of the Private Key String
        :return:
        """
        if not private_key_string:
            auth = MAuth(app_uuid, open(private_key_file, "r").read())
        else:
            auth = MAuth(app_uuid, private_key_string)
        return auth

    def get_user_details(configuration, user_uuid):
        """
        Get the User details from the iMedidata API
        :param dict configuration: Configuration Set
        :param str user_uuid: UUID for user
        """
        mauth_signer = generate_signer(**configuration)
        base_url = "https://www.imedidata.com"
        api_path = f"api/v2/users/{user_uuid}.json"
        full_url = base_url + "/" + api_path
        response = requests.get(full_url, auth=mauth_signer)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Looking up {user_uuid} failed with code {response.status_code}")
            return {}

Using the API Gateway
---------------------

In this example we use the MAuth signer to access the underlying Countries API endpoint

.. code-block:: python

    import requests

    from requests_mauth import MAuth

    def generate_signer(app_uuid, private_key_file=None, private_key_string=None):
        """
        Generate a MAUTH instance
        :param str app_uuid: Application UUID
        :param str private_key_file: name of the Private Key File
        :param str private_key_string: content of the Private Key String
        :return:
        """
        if not private_key_string:
            auth = MAuth(app_uuid, open(private_key_file, "r").read())
        else:
            auth = MAuth(app_uuid, private_key_string)
        return auth

    def get_countries(configuration):
        """
        Get the list of countries from the API GW for a specific API version
        :param dict configuration: a configuration dictionary
        """
        full_url = "https://api.mdsol.com/countries"
        headers = {"Accept": "application/json", "Mcc-Version": "v2019-03-22"}
        mauth_signer = generate_signer(**configuration)

        session = requests.Session()
        session.auth = mauth_signer
        session.headers = headers

        response = session.get(full_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Accessing the countries endpoint failed with error: {response.status_code}")
            return {}

