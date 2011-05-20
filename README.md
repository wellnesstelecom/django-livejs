
django_livejs
=============

django_livejs contains a middleware that inserts live.js in each response in order to update assets when are updated. Read live.js documentation for more information.

**usage**

 - add livejs_middleware.LivejsMiddleware to MIDDLEWARE_CLASSES 
 - set LIVEJS = True in your development settings.

this middlware *only* works when DEBUG is True, reponse is pass thorugh when is False

available settings:

    LIVEJS = False # enable/disable live updating
    LIVEJS_URL = 'http://livejs.com/live.js' # url to live.js file

If you want the templates be updated too activate ETAGS:

    USE_ETAGS = True

CommonMiddleware must be in MIDDLEWARE_CLASSES


