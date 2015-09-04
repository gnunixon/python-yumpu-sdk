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
        headers = {'X-ACCESS-TOKEN': self.token}
        url = "%s%s" % (BASE_URL, entry_point)
        r = requests.get(url, headers=headers, params=params)
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
        headers = {'X-ACCESS-TOKEN': self.token}
        files = None
        if filename:
            files = {'file': open(filename, 'rb')}
        r = requests.post(url, headers=headers, data=params, files=files)
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

        entry_point = '/collections.json'
        params = {
            'offset': offset,
            'limit': limit,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)

    def collection_get(self, id, return_fields=[]):
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
        entry_point = '/collection/section.json'
        params = {
            'id': id,
        }
        if return_fields:
            params['return_fields'] = ','.join(return_fields)
        return self.do_get(entry_point, params)
