# -*- coding: utf-8 -*-
import requests


BASE_URL = 'http://api.yumpu.com/2.0'
SEARCH_URL = 'http://search.yumpu.com/2.0'


class Yumpu():
    """
    This is an SDK for working with Yumpu.com. It's usefull for converting
    pdf documents to web optimized e-Papers.

    For start working you need to register on Yumpu.com and get the token by
    accessing https://www.yumpu.com/en/account/profile/api.

    If you have a free account, then you will have some limitations. The most
    important of them is that you can upload only one PDF every 15 minutes.
    """

    def __init__(self, token):
        """
        For begin working with Yumpu you need to specify your token.

        :params str token: the token for working with API. You can obtain it on https://www.yumpu.com/en/account/profile/api

        :Example:

            from yumpu_sdk import Yumpu


            yumpu = Yumpu('YOUR_TOKEN_HERE')
        """
        self.token = token
        self.headers = {'X-ACCESS-TOKEN': self.token}

    def do_get(self, entry_point, params={}, uri=BASE_URL):
        """
        This function is for getting information from API. It's a general
        function and you can use it for make strange things like send very
        customized requests to API, but in general case you don't need
        to use this method ever.

        :param str entry_point: relative url for sending request
        :param dict params: a dict with GET params to send
        :returns: the result of request
        :rtype: json
        """
        url = "%s%s" % (uri, entry_point)
        r = requests.get(url, headers=self.headers, params=params)
        return r.json()

    def do_post(self, entry_point, params={}, filename=None, uri=BASE_URL):
        """
        This is a general function for post something to Yumpu API.
        It's a very general function, and is better to use somthing more
        specific.

        :param str entry_point: the URL where we will send the datas
        :param dict params: a dict of fields and values for sending
        :param str filename: an absolute path to file for sending
        :returns: a response with detailed data of resulted action
        :rtype: json
        """
        url = "%s%s" % (uri, entry_point)
        files = None
        if filename:
            files = {'file': open(filename, 'rb')}
        r = requests.post(url, headers=self.headers, data=params, files=files)
        return r.json()

    def do_delete(self, entry_point, id, uri=BASE_URL):
        """
        This is a general function for deleting things on Yumpu.

        :param str entry_point: the relative url for send request to delete items
        :param str id: the id of deleting item
        :returns: the result of deleting action
        :rtype: json
        """
        url = "%s%s" % (uri, entry_point)
        params = {'id': id}
        r = requests.delete(url, headers=self.headers, data=params)
        return r.json()

    def do_put(self, entry_point, params={}, uri=BASE_URL):
        """
        This is a general function for send PUT requests to Yumpu API.
        Is used by other functions for update things on Yumpu.

        :param str entry_point: the relative path where to send datas
        :param dict params: the params to send
        :returns: the result of request
        :rtype: json
        """
        url = "%s%s" % (uri, entry_point)
        r = requests.put(url, headers=self.headers, data=params)
        return r.json()

    def documents_get(self, offset=0, limit=10, sort='desc', return_fields=[]):
        """
        Retrieve a list of your documents.

        :param int offset: Retrieve rows at position X (min. 0). Default is 0.
        :param int limit: Retrieve X rows (min. 0 and max. 100). Default is 10.
        :param str sort: Sort results ascending or descendening (asc or desc). Default is desc.
        :param list return_fields: Customize the responses by setting the return fields (id, create_date, update_date, url, short_url, image_small, image_medium, image_big, language, title, description, tags, embed_code, settings)
        :returns: list of documents
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.documents_get()
        {
            u'completed_in': u'0.0584',
            u'state': u'success',
            u'total': u'2',
            u'documents': [
                {
                    u'embed_code': u'<iframe width="512px" height="384px" src="https://www.yumpu.com/en/embed/view/lgjvMHH2ugIUSzdL" frameborder="0" allowfullscreen="true" allowtransparency="true"></iframe>',
                    u'description': u'',
                    u'language': u'en',
                    u'title': u'Test file',
                    u'url': u'http://www.yumpu.com/en/document/view/53486950/test-file',
                    u'short_url': u'http://www.yumpu.com/s/jl0EutaH0Z7UI3KP',
                    u'image': {
                        u'small': u'http://img.yumpu.com/53486950/1/117x156/test-file.jpg',
                        u'big': u'http://img.yumpu.com/53486950/1/1200x1600/test-file.jpg',
                        u'medium': u'http://img.yumpu.com/53486950/1/480x640/test-file.jpg'
                    },
                    u'tags': False,
                    u'id': u'53486950'
                },
                {
                    u'embed_code': u'<iframe width="512px" height="384px" src="https://www.yumpu.com/en/embed/view/0XDrujBssWG7uUQN" frameborder="0" allowfullscreen="true" allowtransparency="true"></iframe>',
                    u'description': u'',
                    u'language': u'en',
                    u'title': u'ACTIV-rom-22(78)-tipar.pdf',
                    u'url': u'http://www.yumpu.com/en/document/view/53312964/activ-rom-2278-tiparpdf',
                    u'short_url': u'http://www.yumpu.com/s/KAZWUpZLoZxNQZd0',
                    u'image': {
                        u'small': u'http://img.yumpu.com/53312964/1/115x163/activ-rom-2278-tiparpdf.jpg',
                        u'big': u'http://img.yumpu.com/53312964/1/1129x1600/activ-rom-2278-tiparpdf.jpg',
                        u'medium': u'http://img.yumpu.com/53312964/1/452x640/activ-rom-2278-tiparpdf.jpg'
                    },
                    u'tags': False,
                    u'id': u'53312964'
                }
            ]
        }
        """
        entry_point = '/documents.json'
        params = {
            'offset': offset,
            'limit': limit,
            'sort': sort
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def document_get(self, id, return_fields=[]):
        """
        Retrieve one document.

        :param int id: id of one of your documents
        :param list return_fields: Customize the responses by setting the return fields (id, create_date, update_date, url, short_url, image_small, image_medium, image_big, language, title, description, tags, embed_code, settings)
        :returns: datas about one specific document
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.document_get(53312964)
        {
            u'completed_in': u'0.0771',
            u'state': u'success',
            u'document': [
                {
                    u'update_date': u'2015-08-30 19:02:16',
                    u'embed_code': u'<iframe width="512px" height="384px" src="https://www.yumpu.com/en/embed/view/0XDrujBssWG7uUQN" frameborder="0" allowfullscreen="true" allowtransparency="true"></iframe>',
                    u'create_date': u'2015-08-30 19:01:11',
                    u'description': u'',
                    u'language': u'en',
                    u'title': u'ACTIV-rom-22(78)-tipar.pdf',
                    u'url': u'http://www.yumpu.com/en/document/view/53312964/activ-rom-2278-tiparpdf',
                    u'short_url': u'http://www.yumpu.com/s/KAZWUpZLoZxNQZd0',
                    u'image': {
                        u'small': u'http://img.yumpu.com/53312964/1/115x163/activ-rom-2278-tiparpdf.jpg',
                        u'big': u'http://img.yumpu.com/53312964/1/1129x1600/activ-rom-2278-tiparpdf.jpg',
                        u'medium': u'http://img.yumpu.com/53312964/1/452x640/activ-rom-2278-tiparpdf.jpg'
                    },
                    u'tags': False,
                    u'access_tags': False,
                    u'subscriptions': False,
                    u'pages': u'1',
                    u'width': u'452',
                    u'height': u'640',
                    u'id': u'53312964',
                    u'settings': {
                        u'magazine_page_teaser_url': u'',
                        u'privacy_mode': u'public',
                        u'player_branding': True,
                        u'site_recommended_magazines': True,
                        u'site_download_pdf': False,
                        u'player_download_pdf': False,
                        u'player_google_analytics_code': u'',
                        u'player_inner_shadow': True,
                        u'appkiosk_iap_sale_item': False,
                        u'appkiosk_itc_product_id': u'',
                        u'player_outer_shadow': True,
                        u'player_social_sharing': True,
                        u'magazine_page_teaser': False,
                        u'player_html5_c2r': True,
                        u'date_validity_until': u'',
                        u'magazine_premium_blurred_page_range': u'',
                        u'site_social_sharing': True,
                        u'player_sidebar': False,
                        u'player_print_page': False,
                        u'date_validity_from': u'',
                        u'magazine_premium_blurred': False,
                        u'magazine_page_teaser_page_range': u'',
                        u'magazine_page_teaser_image_url': u''
                    }
                }
            ]
        }
        """
        entry_point = '/document.json'
        params = {
            'id': id,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def document_post_file(self, **kwargs):
        """
        Create a new document from PDF.

        :param str title: A title for your document. Min. length 5 characters, max. length 255 characters
        :param str file: The full path to pdf for converting
        :param str description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :param int category: 1, 2 or … (A list of valid category ids: Document categories)
        :param str language: en, de or … (A list of valid languages: Document languages)
        :param str tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :param str visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :param str domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :param str validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :param str blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :param str page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :param str downloadable: Allow users to download your source pdf file. y or n
        :param str detect_elements: Detect elements automatically? y or n
        :param str recommended_magazines: Show recommended magazines on Yumpu? y or n
        :param str social_sharing: Show social sharing buttons on Yumpu. y or n
        :param str player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :param str player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :param str player_print_page: Show button „print page“ in Yumpu Player. y or n
        :param str player_branding: Show Yumpu branding in Yumpu Player. y or n
        :param str player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :param str player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :param str player_outer_shadow: Drop shadow in Yumpu player. y or n
        :param str player_inner_shadow: Shadow effects on pages. y or n
        :param str player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :param str access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :param str subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :param str iap: Enable In-App Purchase (y or n)
        :param str itc_product_id: iTunes Product ID
        """
        entry_point = '/document/file.json'
        filename = kwargs.get('filename', None)
        kwargs.pop('filename')
        return self.do_post(entry_point, kwargs, filename)

    def document_post_url(self, **kwargs):
        """
        Create a new document from PDF placed on given URL.

        :param str title: A title for your document. Min. length 5 characters, max. length 255 characters
        :param str url: The URL of PDF
        :param str description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :param int category: 1, 2 or … (A list of valid category ids: Document categories)
        :param str language: en, de or … (A list of valid languages: Document languages)
        :param str tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :param str visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :param str domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :param str validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :param str blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :param str page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :param str downloadable: Allow users to download your source pdf file. y or n
        :param str detect_elements: Detect elements automatically? y or n
        :param str recommended_magazines: Show recommended magazines on Yumpu? y or n
        :param str social_sharing: Show social sharing buttons on Yumpu. y or n
        :param str player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :param str player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :param str player_print_page: Show button „print page“ in Yumpu Player. y or n
        :param str player_branding: Show Yumpu branding in Yumpu Player. y or n
        :param str player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :param str player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :param str player_outer_shadow: Drop shadow in Yumpu player. y or n
        :param str player_inner_shadow: Shadow effects on pages. y or n
        :param str player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :param str access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :param str subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :param str iap: Enable In-App Purchase (y or n)
        :param str itc_product_id: iTunes Product ID
        """
        entry_point = '/document/url.json'
        return self.do_post(entry_point, kwargs)

    def document_put(self, **kwargs):
        """
        Update document on Yumpu.

        :param int id: The id of document to update.
        :param str title: A title for your document. Min. length 5 characters, max. length 255 characters
        :param str description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :param int category: 1, 2 or … (A list of valid category ids: Document categories)
        :param str language: en, de or … (A list of valid languages: Document languages)
        :param str tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :param str visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :param str domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :param str validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :param str blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :param str page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :param str page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :param str downloadable: Allow users to download your source pdf file. y or n
        :param str detect_elements: Detect elements automatically? y or n
        :param str recommended_magazines: Show recommended magazines on Yumpu? y or n
        :param str social_sharing: Show social sharing buttons on Yumpu. y or n
        :param str player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :param str player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :param str player_print_page: Show button „print page“ in Yumpu Player. y or n
        :param str player_branding: Show Yumpu branding in Yumpu Player. y or n
        :param str player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :param str player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :param str player_outer_shadow: Drop shadow in Yumpu player. y or n
        :param str player_inner_shadow: Shadow effects on pages. y or n
        :param str player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :param str access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :param str subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :param str iap: Enable In-App Purchase (y or n)
        :param str itc_product_id: iTunes Product ID
        """
        entry_point = '/document.json'
        return self.do_put(entry_point, kwargs)

    def document_delete(self, id):
        """
        This function will delete the document on Yumpu.

        :param int id: the id of document to delete
        :returns: the result of deleting action
        :rtype: json
        """
        entry_point = '/document.json'
        return self.do_delete(entry_point, id)

    def progess_get(self, id):
        """
        Show the progress of uploading and converting of document.

        :param str id: id of progress object
        :returns: the details of uploading and coverting process
        :rtype: json
        """
        entry_point = '/document/progess.json'
        params = {
            'id': id
        }
        return self.do_get(entry_point, params)

    def document_hotspots_get(self, id, page=None, offset=0, limit=10,
                              sort='page_asc',
                              return_fields=[]):
        """
        Retrieve a list of your document hotspots.

        :param int id: the id of one of your documents
        :param int page: filter the results by page number (1-X)
        :param int offset: Retrieve rows at position X (min. 0)
        :param int limit: Retrieve X rows (min. 0 and max. 100)
        :param str sort: Sort results by create_date_desc, create_date_asc, page_desc, page_asc
        :param list return_fields: Customize the responses by setting the return fields (id, page, type, settings, create_date, update_date)
        :rtype: json
        """
        entry_point = '/document/hotspots.json'
        params = {
            'id': id,
            'page': page,
            'offset': offset,
            'limit': limit,
            'sort': sort
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def document_hotspot_get(self, id,
                             return_fields=[
                                 'id', 'document_id', 'page', 'type',
                                 'settings', 'create_date', 'update_date'
                             ]):
        """
        Retrieve a document hotspot

        :param str id: One of your document hotspot ids
        :param list return_fields: Customize the responses by setting the return fields (id, document_id, page, type, settings, create_date, update_date)Customize the responses by setting the return fields (id, document_id, page, type, settings, create_date, update_date)
        :rtype: json
        """
        entry_point = '/document/hotspot.json'
        params = {
            'id': id
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def __document_hotspot_post(self, document_id, page, type_, sx, sy, sw, sh,
                                sname, stooltip, slink=None, ssource=None,
                                ssource_id=None, ssource_url=None, sautoplay='n'):
        """
        Create a new document hotspot.

        :param int document_id: One of your document ids
        :param str page: Page number (1-X)
        :param str type: Type can be link, video, audio or slideshow
        :param int sx: x position of the document hotspot
        :param int sy: y position of the document hotspot
        :param int sw: width of the document hotspot
        :param int sh: height of the document hotspot
        :param str sname: a name for the document hotspot (min. length 5, max. length 50)
        :param str stooltip: a tooltip for the document hotspot (min. length 5, max. length 50)
        :param str slink: a url (valid URL)
        :param str ssource: youtube, vimeo, flickr, soundcloud
        :param str ssource_id: youtube: a valid youtube video id vimeo: a valid vimeo video id flickr: a valid flickr id
        :param str ssource_url: soundcloud: a valid soundcloud url
        :param str sautoplay: y or n
        :rtype: json
        """
        entry_point = '/document/hotspot.json'
        params = {
            'document_id': document_id,
            'page': page,
            'type': type_,
            'settings[x]': sx,
            'settings[y]': sy,
            'settings[w]': sw,
            'settings[h]': sh,
            'settings[name]': sname,
            'settings[tooltip]': stooltip,
            'settings[link]': slink,
            'settings[source]': ssource,
            'settings[source_id]': ssource_id,
            'settings[source_url]': ssource_url,
            'settings[autoplay]': sautoplay
        }
        return self.do_post(entry_point, params)

    def __document_hotspot_put(self, id, page, type, sx, sy, sw, sh,
                             sname, stooltip, slink, ssource, ssource_id=None,
                             ssource_url=None, sautoplay=None):
        """
        Update a document hotspot.

        :param str id: One of your document hotspot ids
        :param str type: Type can be link, video, audio or slideshow
        :param int sx: x position of the document hotspot
        :param int sy: y position of the document hotspot
        :param int sw: width of the document hotspot
        :param int sh: height of the document hotspot
        :param str sname: a name for the document hotspot (min. length 5, max. length 50)
        :param str stooltip: a tooltip for the document hotspot (min. length 5, max. length 50)
        :param str slink: a url (valid URL)
        :param str ssource: youtube, vimeo, flickr, soundcloud
        :param str ssource_id: youtube: a valid youtube video id vimeo: a valid vimeo video id flickr: a valid flickr id
        :param str ssource_url: soundcloud: a valid soundcloud url
        :param str sautoplay: y or n
        :rtype: json
        """
        entry_point = '/document/hotspot.json'
        params = {
            'id': id,
            'type': type,
            'settings[x]': sx,
            'settings[y]': sy,
            'settings[w]': sw,
            'settings[h]': sh,
            'settings[name]': sname,
            'settings[tooltip]': stooltip,
            'settings[link]': slink,
            'settings[source]': ssource,
            'settings[source_id]': ssource_id,
            'settings[source_url]': ssource_url,
            'settings[autoplay]': sautoplay
        }
        return self.do_put(entry_point, params)

    def document_hotspot_delete(self, id):
        """
        Delete one document hotspot.

        :param str id: One of your document hotspot ids
        :rtype: json
        """
        entry_point = '/document/hotspot.json'
        return self.do_delete(entry_point, id)

    def categories_get(self):
        """
        Get the list of categories.

        :returns: a list of categories with their details
        :rtype: json
        """
        entry_point = '/document/categories.json'
        return self.do_get(entry_point)

    def languages_get(self):
        """
        Get list of supporting languages.

        :returns: a list of languages
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.documents_get()
        {u'completed_in': u'0.0104',
          u'languages': [
                {u'iso': u'en', u'name': u'english'},
                {u'iso': u'de', u'name': u'german'},
                {u'iso': u'fr', u'name': u'french'},
                {u'iso': u'it', u'name': u'italian'},
                {u'iso': u'es', u'name': u'spanish'},
                {u'iso': u'nl', u'name': u'dutch'},
                {u'iso': u'pt', u'name': u'portuguese'},
                {u'iso': u'sv', u'name': u'swedish'},
                {u'iso': u'da', u'name': u'danish'},
                {u'iso': u'no', u'name': u'norwegian'},
                {u'iso': u'gl', u'name': u'galician'},
                {u'iso': u'ro', u'name': u'romanian'},
                {u'iso': u'ca', u'name': u'catalan'},
                {u'iso': u'pl', u'name': u'polish'},
                {u'iso': u'id', u'name': u'indonesian'},
                {u'iso': u'af', u'name': u'afrikaans'},
                {u'iso': u'ru', u'name': u'russian'},
                {u'iso': u'cs', u'name': u'czech'},
                {u'iso': u'hu', u'name': u'hungarian'},
                {u'iso': u'sl', u'name': u'slovene'},
                {u'iso': u'et', u'name': u'estonian'},
                {u'iso': u'tr', u'name': u'turkish'},
                {u'iso': u'eo', u'name': u'esperanto'},
                {u'iso': u'ht', u'name': u'haitian'},
                {u'iso': u'eu', u'name': u'basque'},
                {u'iso': u'cy', u'name': u'welsh'},
                {u'iso': u'mt', u'name': u'maltese'},
                {u'iso': u'sk', u'name': u'slovak'},
                {u'iso': u'bs', u'name': u'bosnian'},
                {u'iso': u'el', u'name': u'greek'},
                {u'iso': u'tl', u'name': u'tagalog'},
                {u'iso': u'hr', u'name': u'croatian'},
                {u'iso': u'fi', u'name': u'finnish'},
                {u'iso': u'xx', u'name': u'unknown'},
                {u'iso': u'sw', u'name': u'swahili'},
                {u'iso': u'lt', u'name': u'lithuanian'},
                {u'iso': u'lv', u'name': u'latvian'},
                {u'iso': u'zh', u'name': u'chinese'},
                {u'iso': u'ga', u'name': u'irish'},
                {u'iso': u'is', u'name': u'icelandic'},
                {u'iso': u'th', u'name': u'thai'},
                {u'iso': u'sq', u'name': u'albanian'},
                {u'iso': u'ja', u'name': u'japanese'},
                {u'iso': u'ms', u'name': u'malay'},
                {u'iso': u'la', u'name': u'latin'},
                {u'iso': u'ko', u'name': u'korean'},
                {u'iso': u'mk', u'name': u'macedonian'},
                {u'iso': u'ar', u'name': u'arabic'},
                {u'iso': u'vi', u'name': u'vietnamese'},
                {u'iso': u'mn', u'name': u'mongolian'},
                {u'iso': u'uk', u'name': u'ukrainian'},
                {u'iso': u'iw', u'name': u'hebrew'},
                {u'iso': u'wa', u'name': u'walloon'},
                {u'iso': u'sr', u'name': u'serbian'},
                {u'iso': u'be', u'name': u'belarusian'},
                {u'iso': u'ta', u'name': u'tamil'},
                {u'iso': u'fa', u'name': u'persian'},
                {u'iso': u'bn', u'name': u'bengali'},
                {u'iso': u'ka', u'name': u'georgian'},
                {u'iso': u'te', u'name': u'telugu'},
                {u'iso': u'hy', u'name': u'armenian'},
                {u'iso': u'ps', u'name': u'pashto'},
                {u'iso': u'kn', u'name': u'kannada'},
                {u'iso': u'aa', u'name': u'afar'},
                {u'iso': u'ab', u'name': u'abkhaz'},
                {u'iso': u'am', u'name': u'amharic'},
                {u'iso': u'dz', u'name': u'dzongkha'},
                {u'iso': u'gn', u'name': u'guarani'},
                {u'iso': u'gu', u'name': u'gujarati'},
                {u'iso': u'ha', u'name': u'hausa'},
                {u'iso': u'hb', u'name': u'hb'},
                {u'iso': u'az', u'name': u'azerbaijani'},
                {u'iso': u'bg', u'name': u'bulgarian'},
                {u'iso': u'hi', u'name': u'hindi'},
                {u'iso': u'kk', u'name': u'kazakh'},
                {u'iso': u'kl', u'name': u'kalaallisut'},
                {u'iso': u'ku', u'name': u'kurdish'},
                {u'iso': u'ky', u'name': u'kyrgyz'},
                {u'iso': u'ml', u'name': u'malayalam'},
                {u'iso': u'mr', u'name': u'marathi'},
                {u'iso': u'my', u'name': u'burmese'},
                {u'iso': u'ne', u'name': u'nepali'},
                {u'iso': u'pa', u'name': u'panjabi'},
                {u'iso': u'sh', u'name': u'serbo-croatian'},
                {u'iso': u'si', u'name': u'sinhala'},
                {u'iso': u'so', u'name': u'somali'},
                {u'iso': u'su', u'name': u'sundanese'},
                {u'iso': u'tk', u'name': u'turkmen'},
                {u'iso': u'tt', u'name': u'tatar'},
                {u'iso': u'ur', u'name': u'urdu'},
                {u'iso': u'uz', u'name': u'uzbek'},
                {u'iso': u'yi', u'name': u'yiddish'},
                {u'iso': u'zu', u'name': u'zulu'}
            ],
            u'state': u'success',
            u'total': 93}

        """
        entry_point = '/document/languages.json'
        return self.do_get(entry_point)

    def countries_get(self):
        """
        Get the list of countries.

        :returns: a list of supporting countries
        :rtype: json
        """
        entry_point = '/document/countries.json'
        return self.do_get(entry_point)

    def collections_get(self, offset=0, limit=10, return_fields=[]):
        """
        Retrieve a list of your collections.

        :param int offset: Retrieve rows at position X (min. 0)
        :param int limit: Retrieve X rows (min. 0 and max. 100)
        :param list return_fields: Customize the responses by setting the return fields (id, create_date, update_date, name, order, sections)
        """
        entry_point = '/collections.json'
        params = {
            'offset': offset,
            'limit': limit,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def collection_get(self, id, return_fields=[]):
        """
        Retrieve one collection.

        :param str id: One of your collection ids
        :param list return_fields: Customize the responses by setting the return fields (id, create_date, update_date, name, order, sections)
        """
        entry_point = '/collection.json'
        params = {
            'id': id,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def collection_post(self, name):
        """
        Create a collection.

        :param str name: the name of new collection
        :returns: the details of new created collection
        :rtype: json
        """
        entry_point = '/collection.json'
        params = {
            'name': name,
        }
        return self.do_post(entry_point, params=params)

    def collection_put(self, id, name):
        """
        Update a collection with given id.

        :param str id: the id of collection to update
        :param str name: the name for update
        :returns: the status of operation and the edited collection
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.collection_put('omkYGduXowlyx9WF', 'Holidays 2013')
        {
            "collection": [
                {
                    "id": "omkYGduXowlyx9WF",
                    "create_date": "2013-09-23 09:05:47",
                    "update_date": "2013-09-23 09:11:45",
                    "name": "Holidays 2013",
                    "order": 0,
                    "sections": [
                        {
                            "id": "omkYGduXowlyx9WF_stVFPUYW3kHX07B6",
                            "name": "",
                            "description": "",
                            "sorting": "manually",
                            "order": 0
                        }
                    ]
                }
            ],
            "state": "success"
        }
        """
        entry_point = '/collection.json'
        params = {
            'id': id,
            'name': name,
        }
        return self.do_put(entry_point, params)

    def collection_delete(self, id):
        """
        This method will delete a collection with given id.

        :param str id: the id of collection to delete
        :returns: the state of operation
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.collection_delete('omkYGduXowlyx9WF')
        {"state":"success"}
        """
        entry_point = '/collection.json'
        return self.do_delete(entry_point, id)

    def section_get(self, id, return_fields=[]):
        """
        Retrieve one section.

        :param str id: One of your section ids
        :param return_fields: Customize the responses by setting the return fields (id, create_date, update_date, name, description, sorting, order, documents)
        :type return_fields: list
        """
        entry_point = '/collection/section.json'
        params = {
            'id': id,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def section_post(self, id, name, description=None, sorting='manually'):
        """
        Create a new section for given category.

        :param str id: One of your collection ids
        :param str name: The name of section
        :param str description: Description of this section
        :param str sorting: Sort documents in section manually or automatically (by create_date_desc, create_date_asc, title_desc, title_asc)

        :returns: the datas of new created section
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.section_post('iMWWKoMS76pjqMoO', 'Sports', 'Sports')
        {
            "section": [
                {
                    "id": "F54wo1ijuIzhbSfK",
                    "create_date": "2013-09-23 10:46:53",
                    "update_date": "0000-00-00 00:00:00",
                    "name": "Sports",
                    "description": "Sports",
                    "sorting": "manually",
                    "order": 2,
                    "documents": ""
                }
            ],
            "state": "success"
        }
        """
        entry_point = '/collection/section.json'
        params = {
            'id': id,
            'name': name,
            'description': description,
            'sorting': sorting
        }
        return self.do_post(entry_point, params)

    def section_put(self, id, name, description=None, sorting='manually'):
        """
        Create a new section for given category.

        :param str id: One of your section ids
        :param str name: The name of section
        :param str description: Description of this section
        :param str sorting: Sort documents in section manually or automatically (by create_date_desc, create_date_asc, title_desc, title_asc)

        :returns: the datas of new created section
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.section_put('F54wo1ijuIzhbSfK', 'Sports 2013')
        {
            "section": [
                {
                    "id": "F54wo1ijuIzhbSfK",
                    "create_date": "2013-09-23 10:46:53",
                    "update_date": "2013-09-23 11:11:35",
                    "name": "Sports 2013",
                    "description": "Sports",
                    "sorting": "create_date_desc",
                    "order": 2,
                    "documents": ""
                }
            ],
            "state": "success"
        }
        """
        entry_point = '/collection/section.json'
        params = {
            'id': id,
            'name': name,
            'sorting': sorting
        }
        if description:
            params['description'] = description
        return self.do_put(entry_point, params)

    def section_delete(self, id):
        """
        Delete one of your sections

        :param str id: The id of one of your sections
        :returns: the status of operation
        :rtype: json

        >>> from yumpu_sdk.api import Yumpu
        >>> yumpu = Yumpu('YOUR_TOKEN_HERE')
        >>> yumpu.section_delete('omkYGduXowlyx9WF')
        {"state":"success"}
        """
        entry_point = '/collection/section.json'
        return self.do_delete(entry_point, id)

    def section_document_post(self, id, documents):
        """
        Create a new document in section.

        :param str id: one of your section ids
        :param list documents: a list of your documents ids for add to this section
        :returns: the content of section object
        """
        entry_point = '/collection/section/document.json'
        params = {
            'id': id,
            'documents': ','.join(documents)
        }
        return self.do_post(entry_point, params)

    def section_document_delete(self, id, documents):
        """
        Remove documents from section.

        :param str id: one of your section ids
        :param list documents: a list of your documents ids
        :returns: the content of section object
        """
        entry_point = '/collection/section/document.json'
        params = {
            'id': id,
            'documents': ','.join(documents)
        }
        url = "%s%s" % (BASE_URL, entry_point)
        r = requests.delete(url, headers=self.headers, data=params)
        return r.json()

    def search(self, q, in_=['author', 'title', 'description', 'tags'],
               op='or', offset=0, limit=10,
               return_fields=[
                   'id', 'url', 'short_url', 'image_small', 'image_medium',
                   'image_big', 'language', 'title', 'description', 'tags',
                   'embed_code'
               ],
               sort=None, language=None, pages=None, heat_rank=None,
               views=None, create_date=None, category=None):
        """
        Search documents

        :param str q: A keyword to search for
        :param list in_: Search keyword in fields author, title, description or tags
        :param str op: Search keyword with „and“ or „or“ operator
        :param int offset: Retrieve rows at position X (min. 0)
        :param int limit: Retrieve X rows (min. 0 and max. 100)
        :param list return_fields: Customize the responses by setting the return fields (id, url, short_url, image_small, image_medium, image_big, language, title, description, tags, embed_code)
        :param str sort: Sort results (views_desc, views_asc, create_date_desc, create_date_asc, heat_rank_desc, heat_rank_asc, pages_desc, pages_asc)
        :param str language: Filter result (de, en, …)
        :param str pages: Filter result from 10 to 20 pages (10-20) or exact 30 pages (30)
        :param str heat_rank: Filter result from 50 to 100 heat_rank (50-100) or exact 80 heat_rank (80)
        :param str views: Filter result with 500 to 1000 views (500-1000) or exact 800 views (800)
        :param str create_date: Filter result which got created from 2013-09-01 between 2013-09-30 (2013-09-01-2013-09-30) or on an exact date 2013-09-01 (2013-09-01)
        :param int category: Filter result (1, 2, …)
        :rtype: json
        """
        entry_point = '/search.json'
        params = {
            'q': q,
            'op': op,
            'sort': sort,
            'language': language,
            'pages': pages,
            'heat_rank': heat_rank,
            'views': views,
            'create_date': create_date,
            'category': category
        }
        if in_:
            params['in'] = ','.join(in_)
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params, SEARCH_URL)

    def user_get(self, return_fields=[]):
        """
        Retrieve your user profile data.

        :param list return_fields: Customize the responses by setting the return fields (id, create_date, activate_date, last_login_date, username, email, gender, name, firstname, lastname, birth_date, address, zip_code, city, country, description, website, blog, language)
        :rtype: json
        """
        entry_point = '/user.json'
        params = {}
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def user_put(self, **kwargs):
        """
        Update your profile.

        :param str gender: Your gender (male or female)
        :param str firstname: Your firstname (min. length 2 characters, max. length 100 characters)
        :param str lastname: Your lastname (min. length 2 characters, max. length 100 characters)
        :param str birth_date: Your birth_date (YYYY-MM-DD)
        :param str address: Your address (max. length 255 characters)
        :param str zip_code: Your zip code (max. length 10 characters)
        :param str city: Your city (max. length 50 characters)
        :param str country: Your country (DE, GB, FR, …)
        :param str description: Your address (max. length 255 characters)
        :param str website: Your website (max. length 255 characters, valid URL)
        :param str blog: Your blog (max. length 255 characters, valid URL)
        :param str language: Your language (de, en, fr, …)
        :rtype: json
        """
        entry_point = '/user.json'
        return self.do_put(entry_point, kwargs)

    def user_post(self, **kwargs):
        """
        Create a new user profile.

        :param str email: Your email address (valid email address)
        :param str username: Your username (Allowed characters a-z, A-Z, 0-9 and a dot, min. length 5 characters, max. length 30 characters)
        :param str password: Your password (min. length 6 characters)
        :param str gender: Your gender (male or female)
        :param str firstname: Your firstname (min. length 2 characters, max. length 100 characters)
        :param str lastname: Your lastname (min. length 2 characters, max. length 100 characters)
        :param str birth_date: Your birth_date (YYYY-MM-DD)
        :param str address: Your address (max. length 255 characters)
        :param str zip_code: Your zip code (max. length 10 characters)
        :param str city: Your city (max. length 50 characters)
        :param str country: Your country (DE, GB, FR, …)
        :param str description: Your address (max. length 255 characters)
        :param str website: Your website (max. length 255 characters, valid URL)
        :param str blog: Your blog (max. length 255 characters, valid URL)
        :param str language: Your language (de, en, fr, …)
        :rtype: json
        """
        entry_point = '/user.json'
        return self.do_post(entry_point, kwargs)
