
django_livejs
=============

django_livejs contains a middleware that inserts live.js in each response in order to update assets when are updated. Read [live.js documentation](http://livejs.com/) for more information.

**quick start**

 - add django_livejs.middleware.LivejsMiddleware to MIDDLEWARE_CLASSES
 - set LIVEJS = True in your development settings

this middlware *only* works when DEBUG is True, reponse is pass thorugh when is False

**available settings**

    LIVEJS = False # enable/disable live updating
    LIVEJS_URL = 'http://livejs.com/live.js' # url to live.js file

Your application templates can be updated if you enable ETAGS in your settings:

    USE_ETAGS = True

CommonMiddleware must be in MIDDLEWARE_CLASSES in order to use ETAGS (by default it's enabled)


