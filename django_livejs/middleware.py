# -*- encoding: utf-8 -*-

"""
livejs middleware. Insert live.js in each template in order to update assets 
when are changed. Read live.js documentation for more information.

usage:
    - add livejs_middleware.LivejsMiddleware to MIDDLEWARE_CLASSES 
    - add LIVEJS = True to your development settings.

this middlware only works when DEBUG is True, reponse is pass thorugh when is False

available settings:
    LIVEJS = False # enable/disable live updating
    LIVEJS_URL = 'http://livejs.com/live.js' # url to live.js file

code has been created using debug toolbar middleware as start point, thanks to authors

"""

import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.encoding import smart_unicode


_HTML_TYPES = ('text/html', 'application/xhtml+xml')

def replace_insensitive(string, target, replacement):
    """
    Similar to string.replace() but is case insensitive
    Code borrowed from: http://forums.devshed.com/python-programming-11/case-insensitive-string-replace-490921.html
    """
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else: # no results so return the original string
        return string

class LivejsMiddleware(object):
    """
    Middleware add live.js library to update assets when are changed
    """
    def __init__(self):
        self.tag= u'</body>'
        livejs_url = getattr(settings, 'LIVEJS_URL', 'http://livejs.com/live.js')
        self.live_js = u'<script src="%s"></script>' % livejs_url

    def process_response(self, request, response):
        """
        get content from response and insert after </body> live.js script
        only works when DEBUG is active
        """
        livejs_active = getattr(settings, 'LIVEJS', False)
        if not settings.DEBUG or not livejs_active:
            return response

        if not isinstance(response, HttpResponseRedirect) and response.status_code == 200:
            if response['Content-Type'].split(';')[0] in _HTML_TYPES:
                response.content = replace_insensitive(
                    smart_unicode(response.content),
                    self.tag,
                    smart_unicode(self.live_js))
            # update response length
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)
        return response
