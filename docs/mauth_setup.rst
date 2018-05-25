Setting Up a MAuth Application
==============================
.. _create_a_mauth_app:
1. Create a keyset::

    $ mkdir keypair_dir
    $ cd keypair_dir
    $ openssl genrsa -out yourname_mauth.priv.key 2048
    $ chmod 0600 yourname_mauth.priv.key
    $ openssl rsa -in yourname_mauth.priv.key -pubout -out yourname_mauth.pub.key

2. Register the Public Key with Medidata

Provide PUBLIC key to DevOps via Zendesk_ ticket with settings:

+----------------+---------------------------+
| Attribute      | Value                     |
+================+===========================+
|Form            | OPS - Service Request     |
+----------------+---------------------------+
|Assignee        | OPS-Devops Cloud Team     |
+----------------+---------------------------+
|Service Catalog | Application support       |
+----------------+---------------------------+

You will need to specify the stage (eg `Production`, `Innovate`, etc)

3. You will recieve an `APP_UUID` - this is what you use in the requests.

.. _Zendesk: https://mdsolsupport.zendesk.com/
