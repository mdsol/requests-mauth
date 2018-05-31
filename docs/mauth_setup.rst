Setting Up a MAuth Application
==============================

.. _create_a_mauth_app:

Creating and registering MAuth Application credentials
-------------------------------------------------------

1. Create a keyset::

    $ mkdir keypair_dir
    $ cd keypair_dir
    $ openssl genrsa -out yourname_mauth.priv.key 2048
    $ chmod 0600 yourname_mauth.priv.key
    $ openssl rsa -in yourname_mauth.priv.key -pubout -out yourname_mauth.pub.key

2. Register the Public Key with Medidata for the correct Environment (eg **Production**, **Innovate**, etc)

Provide PUBLIC key to DevOps via Zendesk_ ticket with the following configuration:

    +----------------+---------------------------+
    | Attribute      | Value                     |
    +================+===========================+
    |Form            | OPS - Service Request     |
    +----------------+---------------------------+
    |Assignee        | OPS-Devops Cloud Team     |
    +----------------+---------------------------+
    |Service Catalog | Application support       |
    +----------------+---------------------------+

3. When the application is registered an **Application UUID** (or *APP_UUID* ) is generated.  The value for the *APP_UUID* will be included in the Ticket response.
   The *APP_UUID* is required for authentication of requests.

.. _Zendesk: https://mdsolsupport.zendesk.com/
