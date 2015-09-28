# python-yumpu-sdk

This is an SDK for working with Yumpu.com. It's usefull for converting
pdf documents to web optimized e-Papers.

For start working you need to register on Yumpu.com and get the token by
accessing https://www.yumpu.com/en/account/profile/api.

If you have a free account, then you will have some limitations. To look at the current limitations, you can access this address: http://developers.yumpu.com/api/limits/.

# Install

The most simple way is by using pypi:

    pip install yumpu-sdk


Requierments
------------

* python >= 2.7 or python 3
* requests


Implemented features
--------------------

* Documents
    * Get all documents
    * Get a particular document
    * Post a document from file, or from url
    * Get info about progress of uploading acction
    * Edit a document
    * Delete document
* Hotspots
    * Get all hotspots in a document
    * Get a particular hotspot
    * Delete a hotspot
* Get list of available countries
* Get list of available languages
* Get list of available categories
* Collections
    * Get all your collections
    * Get a particular collection
    * Create a new collection
    * Modify a particular collection
    * Delete collection
* Sections
    * Create a section in collection
    * Get a section
    * Update section
    * Delete section
    * Assign document(s) to section
    * Remove document(s) from section
* Search


Documentation
-------------

The full documentation for this project is on http://python-yumpu-sdk.readthedocs.org/
