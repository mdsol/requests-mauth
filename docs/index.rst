.. Mauth Authenticator for Requests documentation master file, created by
   sphinx-quickstart on Tue May 22 15:22:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Mauth Authenticator for Requests's documentation!
============================================================

*requests-mauth* is a python library that provides an authentication library for MAuth Authentication on top of the excellent Requests_ library.

What is MAuth?
--------------
The MAuth protocol provides a fault-tolerant, service-to-service authentication scheme for Medidata and third-party applications that use web services to communicate. The Authentication Service and integrity algorithm is based on digital signatures encrypted and decrypted with a private/public key pair.

The Authentication Service has two responsibilities. It provides message integrity and provenance validation by verifying a message sender's signature; its other task is to manage public keys. Each public key is associated with an application and is used to authenticate message signatures. The private key corresponding to the public key in the Authentication Service is stored by the application making a signed request; the request is encrypted with this private key. The Authentication Service has no knowledge of the application's private key, only its public key.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   mauth_setup
   examples
   faq

.. _Requests: http://docs.python-requests.org/en/master/

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
