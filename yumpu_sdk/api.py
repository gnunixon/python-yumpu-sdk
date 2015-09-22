# -*- coding: utf-8 -*-
import requests


BASE_URL = 'http://api.yumpu.com/2.0'


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

        :params token: the token for working with API. You can obtain it on https://www.yumpu.com/en/account/profile/api
        :type token: str

        :Example:

            from yumpu_sdk import Yumpu


            yumpu = Yumpu('YOUR_TOKEN_HERE')
        """
        self.token = token
        self.headers = {'X-ACCESS-TOKEN': self.token}

    def do_get(self, entry_point, params={}):
        """
        This function is for getting information from API. It's a general
        function and you can use it for make strange things like send very
        customized requests to API, but in general case you don't need
        to use this method ever.

        :param entry_point: relative url for sending request
        :type entry_point: str
        :param params: a dict with GET params to send
        :type params: dict
        :returns: the result of request
        :rtype: json
        """
        url = "%s%s" % (BASE_URL, entry_point)
        r = requests.get(url, headers=self.headers, params=params)
        return r.json()

    def do_post(self, entry_point, params={}, filename=None):
        """
        This is a general function for post something to Yumpu API.
        It's a very general function, and is better to use somthing more
        specific.

        :param entry_point: the URL where we will send the datas
        :type entry_point: str
        :param params: a dict of fields and values for sending
        :type params: dict
        :param filename: an absolute path to file for sending
        :type filename: str
        :returns: a response with detailed data of resulted action
        :rtype: json
        """
        url = "%s%s" % (BASE_URL, entry_point)
        files = None
        if filename:
            files = {'file': open(filename, 'rb')}
        r = requests.post(url, headers=self.headers, data=params, files=files)
        return r.json()

    def do_delete(self, entry_point, id):
        """
        This is a general function for deleting things on Yumpu.

        :param entry_point: the relative url for send request to delete items
        :type entry_point: str
        :param id: the id of deleting item
        :type id: int
        :returns: the result of deleting action
        :rtype: json
        """
        url = "%s%s" % (BASE_URL, entry_point)
        params = {'id': id}
        r = requests.delete(url, headers=self.headers, data=params)
        return r.json()

    def do_put(self, entry_point, params={}):
        """
        This is a general function for send PUT requests to Yumpu API.
        Is used by other functions for update things on Yumpu.

        :param entry_point: the relative path where to send datas
        :type entry_point: str
        :param params: the params to send
        :type params: dict
        :returns: the result of request
        :rtype: json
        """
        url = "%s%s" % (BASE_URL, entry_point)
        r = requests.put(url, headers=self.headers, data=params)
        return r.json()

    def documents_get(self, offset=0, limit=10, sort='desc', return_fields=[]):
        """
        Retrieve a list of your documents.

        :param offset: Retrieve rows at position X (min. 0). Default is 0.
        :type offset: int
        :param limit: Retrieve X rows (min. 0 and max. 100). Default is 10.
        :type limit: int
        :param sort: Sort results ascending or descendening (asc or desc). Default is desc.
        :type sort: str
        :param return_fields: Customize the responses by setting the return fields (id, create_date, update_date, url, short_url, image_small, image_medium, image_big, language, title, description, tags, embed_code, settings)
        :type return_fields: list
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

        :param id: id of one of your documents
        :type id: int
        :param return_fields: Customize the responses by setting the return fields (id, create_date, update_date, url, short_url, image_small, image_medium, image_big, language, title, description, tags, embed_code, settings)
        :type param: list
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

    def document_post_file(
        self, title, filename,
        description=None,
        category=0,
        language='en',
        tags=None,
        visibility='public',
        domains=None,
        validity=None,
        blurred=None,
        page_teaser_image=None,
        page_teaser_page_range=None,
        page_teaser_url=None,
        downloadable='n',
        detect_elements='y',
        recommended_magazines='y',
        social_sharing='y',
        player_social_sharing='y',
        player_download_pdf='n',
        player_print_page='n',
        player_branding='y',
        player_sidebar='n',
        player_html5_c2r='y',
        player_outer_shadow='y',
        player_inner_shadow='y',
        player_ga=None,
        access_tags=None,
        subscriptions=None,
        iap='n',
        itc_product_id=None
    ):
        """
        Create a new document from PDF.

        :param title: A title for your document. Min. length 5 characters, max. length 255 characters
        :type title: str
        :param file: The full path to pdf for converting
        :type file: str
        :param description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :type description: str
        :param category: 1, 2 or … (A list of valid category ids: Document categories)
        :type category: int
        :param language: en, de or … (A list of valid languages: Document languages)
        :type language: str
        :param tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :type tags: str
        :param visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :type visibility: str
        :param domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :type domains: str
        :param validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :type validity: str
        :param blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type blurred: str
        :param page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :type page_teaser_image: str
        :param page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type page_teaser_page_range: str
        :param page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :type page_teaser_url: str
        :param downloadable: Allow users to download your source pdf file. y or n
        :type downloadable: str
        :param detect_elements: Detect elements automatically? y or n
        :type detect_elements: str
        :param recommended_magazines: Show recommended magazines on Yumpu? y or n
        :type recommended_magazines: str
        :param social_sharing: Show social sharing buttons on Yumpu. y or n
        :type social_sharing: str
        :param player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :type player_social_sharing: str
        :param player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :type player_download_pdf: str
        :param player_print_page: Show button „print page“ in Yumpu Player. y or n
        :type player_print_page: str
        :param player_branding: Show Yumpu branding in Yumpu Player. y or n
        :type player_branding: str
        :param player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :type player_sidebar: str
        :param player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :type player_html5_c2r: str
        :param player_outer_shadow: Drop shadow in Yumpu player. y or n
        :type player_outer_shadow: str
        :param player_inner_shadow: Shadow effects on pages. y or n
        :type player_inner_shadow: str
        :param player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :type player_ga: str
        :param access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :type access_tags: str
        :param subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :type subscriptions: str
        :param iap: Enable In-App Purchase (y or n)
        :type iap: str
        :param itc_product_id: iTunes Product ID
        :type itc_product_id: str
        """
        entry_point = '/document/file.json'
        params = {
            'title': title,
            'description': description,
            'category': category,
            'language': language,
            'tags': tags,
            'visibility': visibility,
            'domains': domains,
            'validity': validity,
            'blurred': blurred,
            'page_teaser_image': page_teaser_image,
            'page_teaser_page_range': page_teaser_page_range,
            'page_teaser_url': page_teaser_url,
            'downloadable': downloadable,
            'detect_elements': detect_elements,
            'recommended_magazines': recommended_magazines,
            'social_sharing': social_sharing,
            'player_social_sharing': player_social_sharing,
            'player_download_pdf': player_download_pdf,
            'player_print_page': player_print_page,
            'player_branding': player_branding,
            'player_sidebar': player_sidebar,
            'player_html5_c2r': player_html5_c2r,
            'player_outer_shadow': player_outer_shadow,
            'player_inner_shadow': player_inner_shadow,
            'player_ga': player_ga,
            'access_tags': access_tags,
            'subscriptions': subscriptions,
            'iap': iap,
            'itc_product_id': itc_product_id
        }
        return self.do_post(entry_point, params, filename)

    def document_post_url(
        self, title, url,
        description=None,
        category=0,
        language='en',
        tags=None,
        visibility='public',
        domains=None,
        validity=None,
        blurred=None,
        page_teaser_image=None,
        page_teaser_page_range=None,
        page_teaser_url=None,
        downloadable='n',
        detect_elements='y',
        recommended_magazines='y',
        social_sharing='y',
        player_social_sharing='y',
        player_download_pdf='n',
        player_print_page='n',
        player_branding='y',
        player_sidebar='n',
        player_html5_c2r='y',
        player_outer_shadow='y',
        player_inner_shadow='y',
        player_ga=None,
        access_tags=None,
        subscriptions=None,
        iap='n',
        itc_product_id=None
    ):
        """
        Create a new document from PDF placed on given URL.

        :param title: A title for your document. Min. length 5 characters, max. length 255 characters
        :type title: str
        :param url: The URL of PDF
        :type url: str
        :param description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :type description: str
        :param category: 1, 2 or … (A list of valid category ids: Document categories)
        :type category: int
        :param language: en, de or … (A list of valid languages: Document languages)
        :type language: str
        :param tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :type tags: str
        :param visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :type visibility: str
        :param domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :type domains: str
        :param validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :type validity: str
        :param blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type blurred: str
        :param page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :type page_teaser_image: str
        :param page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type page_teaser_page_range: str
        :param page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :type page_teaser_url: str
        :param downloadable: Allow users to download your source pdf file. y or n
        :type downloadable: str
        :param detect_elements: Detect elements automatically? y or n
        :type detect_elements: str
        :param recommended_magazines: Show recommended magazines on Yumpu? y or n
        :type recommended_magazines: str
        :param social_sharing: Show social sharing buttons on Yumpu. y or n
        :type social_sharing: str
        :param player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :type player_social_sharing: str
        :param player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :type player_download_pdf: str
        :param player_print_page: Show button „print page“ in Yumpu Player. y or n
        :type player_print_page: str
        :param player_branding: Show Yumpu branding in Yumpu Player. y or n
        :type player_branding: str
        :param player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :type player_sidebar: str
        :param player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :type player_html5_c2r: str
        :param player_outer_shadow: Drop shadow in Yumpu player. y or n
        :type player_outer_shadow: str
        :param player_inner_shadow: Shadow effects on pages. y or n
        :type player_inner_shadow: str
        :param player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :type player_ga: str
        :param access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :type access_tags: str
        :param subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :type subscriptions: str
        :param iap: Enable In-App Purchase (y or n)
        :type iap: str
        :param itc_product_id: iTunes Product ID
        :type itc_product_id: str
        """
        entry_point = '/document/url.json'
        params = {
            'title': title,
            'url': url,
            'description': description,
            'category': category,
            'language': language,
            'tags': tags,
            'visibility': visibility,
            'domains': domains,
            'validity': validity,
            'blurred': blurred,
            'page_teaser_image': page_teaser_image,
            'page_teaser_page_range': page_teaser_page_range,
            'page_teaser_url': page_teaser_url,
            'downloadable': downloadable,
            'detect_elements': detect_elements,
            'recommended_magazines': recommended_magazines,
            'social_sharing': social_sharing,
            'player_social_sharing': player_social_sharing,
            'player_download_pdf': player_download_pdf,
            'player_print_page': player_print_page,
            'player_branding': player_branding,
            'player_sidebar': player_sidebar,
            'player_html5_c2r': player_html5_c2r,
            'player_outer_shadow': player_outer_shadow,
            'player_inner_shadow': player_inner_shadow,
            'player_ga': player_ga,
            'access_tags': access_tags,
            'subscriptions': subscriptions,
            'iap': iap,
            'itc_product_id': itc_product_id
        }
        return self.do_post(entry_point, params)

    def document_put_url(
        self, id, title,
        description=None,
        category=0,
        language='en',
        tags=None,
        visibility='public',
        domains=None,
        validity=None,
        blurred=None,
        page_teaser_image=None,
        page_teaser_page_range=None,
        page_teaser_url=None,
        downloadable='n',
        detect_elements='y',
        recommended_magazines='y',
        social_sharing='y',
        player_social_sharing='y',
        player_download_pdf='n',
        player_print_page='n',
        player_branding='y',
        player_sidebar='n',
        player_html5_c2r='y',
        player_outer_shadow='y',
        player_inner_shadow='y',
        player_ga=None,
        access_tags=None,
        subscriptions=None,
        iap='n',
        itc_product_id=None
    ):
        """
        Update document on Yumpu.

        :param id: The id of document to update.
        :type id: int
        :param title: A title for your document. Min. length 5 characters, max. length 255 characters
        :type title: str
        :param description: A description for your document. Min. length 5 characters, max. length 2500 characters
        :type description: str
        :param category: 1, 2 or … (A list of valid category ids: Document categories)
        :type category: int
        :param language: en, de or … (A list of valid languages: Document languages)
        :type language: str
        :param tags: A list of words seperated by comma (house,garden,balcony). Min. length 3 characters, max. length 30 characters. Allowed characters a-z and a space.
        :type tags: str
        :param visibility: public, private, rprotected, pprotected, dprotected, webkiosk, appkiosk or webappkiosk (rprotected = protected by referrer, pprotected = protected by password, dprotected = protected by domain(s))
        :type visibility: str
        :param domains: A list of domains seperated by a comma (Note: Visibility must be set to dprotected) Examples: yumpu.com,blog.yumpu.com,developers.yumpu.com yumpu.com
        :type domains: str
        :param validity: Valid from and / or valid until Examples: 2013-10-01T00:00:00-2013-10-30T23:59:59 (valid from 2013-10-01 00:00:00, valid until 2013-10-30 23:59:59) 2013-10-01T00:00:00- (valid from 2013-10-01 00:00:00-) -2013-10-30T23:59:59 (valid until -2013-10-30 23:59:59)
        :type validity: str
        :param blurred: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type blurred: str
        :param page_teaser_image: Image data The image must be less than 2 MB in size. Allowed mime types are image/gif, image/jpeg, image/pjpeg, image/png and image/x-png. The image will be resized to fit in the page dimensions (of your magazine). Note: If you use page_teaser_image, the parameters page_teaser_page_range and page_teaser_url are required.
        :type page_teaser_image: str
        :param page_teaser_page_range: Page numbers seperated by comma. Examples: 1-2, 5-9, 11-
        :type page_teaser_page_range: str
        :param page_teaser_url: A valid URL. Examples: http://www.yumpu.com/en
        :type page_teaser_url: str
        :param downloadable: Allow users to download your source pdf file. y or n
        :type downloadable: str
        :param detect_elements: Detect elements automatically? y or n
        :type detect_elements: str
        :param recommended_magazines: Show recommended magazines on Yumpu? y or n
        :type recommended_magazines: str
        :param social_sharing: Show social sharing buttons on Yumpu. y or n
        :type social_sharing: str
        :param player_social_sharing: Show social sharing buttons in Yumpu Player. y or n
        :type player_social_sharing: str
        :param player_download_pdf: Show button „download pdf“ in Yumpu Player. y or n
        :type player_download_pdf: str
        :param player_print_page: Show button „print page“ in Yumpu Player. y or n
        :type player_print_page: str
        :param player_branding: Show Yumpu branding in Yumpu Player. y or n
        :type player_branding: str
        :param player_sidebar: Show a list of recommended documents in Yumpu Player. y or n
        :type player_sidebar: str
        :param player_html5_c2r: Activate HTML5 full screen on Yumpu. y or n
        :type player_html5_c2r: str
        :param player_outer_shadow: Drop shadow in Yumpu player. y or n
        :type player_outer_shadow: str
        :param player_inner_shadow: Shadow effects on pages. y or n
        :type player_inner_shadow: str
        :param player_ga: Activate Google Analytics tracking. A valid UA code from Google Analytics.
        :type player_ga: str
        :param access_tags: One or multiple access_tag ids (myid1 or myid1,myid2)
        :type access_tags: str
        :param subscriptions: One or multiple subscription ids (myid1 or myid1,myid2)
        :type subscriptions: str
        :param iap: Enable In-App Purchase (y or n)
        :type iap: str
        :param itc_product_id: iTunes Product ID
        :type itc_product_id: str
        """
        entry_point = '/document.json'
        params = {
            'id': id,
            'title': title,
            'description': description,
            'category': category,
            'language': language,
            'tags': tags,
            'visibility': visibility,
            'domains': domains,
            'validity': validity,
            'blurred': blurred,
            'page_teaser_image': page_teaser_image,
            'page_teaser_page_range': page_teaser_page_range,
            'page_teaser_url': page_teaser_url,
            'downloadable': downloadable,
            'detect_elements': detect_elements,
            'recommended_magazines': recommended_magazines,
            'social_sharing': social_sharing,
            'player_social_sharing': player_social_sharing,
            'player_download_pdf': player_download_pdf,
            'player_print_page': player_print_page,
            'player_branding': player_branding,
            'player_sidebar': player_sidebar,
            'player_html5_c2r': player_html5_c2r,
            'player_outer_shadow': player_outer_shadow,
            'player_inner_shadow': player_inner_shadow,
            'player_ga': player_ga,
            'access_tags': access_tags,
            'subscriptions': subscriptions,
            'iap': iap,
            'itc_product_id': itc_product_id
        }
        return self.do_put(entry_point, params)

    def document_delete(self, id):
        """
        This function will delete the document on Yumpu.

        :param id: the id of document to delete
        :type id: int
        :returns: the result of deleting action
        :rtype: json
        """
        entry_point = '/document.json'
        return self.do_delete(entry_point, id)

    def progess_get(self, id):
        """
        Show the progress of uploading and converting of document.

        :param id: id of document
        :type id: int
        :returns: the details of uploading and coverting process
        :rtype: json
        """
        entry_point = '/document/progess.json'
        params = {
            'id': id
        }
        return self.do_get(entry_point, params)

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

        :param offset: Retrieve rows at position X (min. 0)
        :type offset: int
        :param limit: Retrieve X rows (min. 0 and max. 100)
        :type limit: int
        :param return_fields: Customize the responses by setting the return fields (id, create_date, update_date, name, order, sections)
        :type return_fields: list
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

        :param id: One of your collection ids
        :type id: str
        :param return_fields: Customize the responses by setting the return fields (id, create_date, update_date, name, order, sections)
        :type return_fields: list
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

        :param name: the name of new collection
        :type name: str
        :returns: the details of new created collection
        :rtype: json
        """
        entry_point = '/collection.json'
        params = {
            'name': name,
        }
        return self.do_post(entry_point, params=params)

    def section_get(self, id, return_fields=[]):
        """
        Retrieve one section.

        :param id: One of your section ids
        :type id: str
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
