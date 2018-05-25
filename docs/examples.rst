Example Usage
=============

Accessing an iMedidata User Endpoint
------------------------------------

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
            auth = MAuth(app_uuid, open(private_key_file, 'r').read())
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
        base_url = "https://innovate.imedidata.com"
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
            auth = MAuth(app_uuid, open(private_key_file, 'r').read())
        else:
            auth = MAuth(app_uuid, private_key_string)
        return auth

    def get_countries(configuration):
        """
        Get the list of countries from the API GW
        """
        full_url = "https://apigw.imedidata.com/v1/countries"
        mauth_signer = generate_signer(**configuration)
        session = requests.Session()
        session.auth = mauth_signer
        response = session.get(full_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Accessing the countries endpoint failed with error: {response.status_code}")
            return {}

