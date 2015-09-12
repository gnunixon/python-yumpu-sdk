.. yumpu-sdk documentation master file, created by
   sphinx-quickstart on Fri Sep  4 17:41:36 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to yumpu-sdk's documentation!
=====================================

This SDK will help you to upload and manage your publications on Yumpu - a service for converting PDFs in web optimized e-Papers. 
For begin working with this SDK you will need to register on Yumpu and obtain the access token in your profile (https://www.yumpu.com/en/account/profile/api).

Install
-------

The simplest way to install this SDK is by using PyPi.

.. code-block:: bash

    pip install yumpu-sdk

or you can clone and install the version from our repo on github:

.. code-block:: bash

    git clone https://github.com/gnunixon/python-yumpu-sdk.git

    cd python-yumpu-sdk

    python setup.py install

Using
-----

.. code-block:: python

    from yumpu_sdk.api import Yumpu

    yumpu = Yumpu('YOUR_TOKEN_HERE')

    new_document = yumpu.document_post_file(
                    'My new document',
                    '/home/user/Documents/doc.pdf'
                    )

Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: yumpu_sdk.api
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

