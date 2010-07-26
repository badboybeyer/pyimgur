#!/bin/env python

__author__ = 'Devon Meunier <devon.meunier@myopicvoid.org>'
__description__ = "A Pythonic interface to the imgur api."
__version__ = '0.7.5'

import urllib
try:
    import simplejson as json
except ImportError:
    import json


class imgurAPIError(Exception):
    pass


class imgur:
    def __init__(self, apikey=None):
        self.apikey = apikey

    def upload(self, image):
        """
        Upload an image to imgur.
        'image' Must be a file-like python object
        Returns the parsed json that imgur returns.
        """
        if self.apikey is None:
            raise imgurAPIError, "API Key is missing."
            return None 
        else:
            postdata = {"key": self.apikey,
                        "image": base64.b64encode(image)}
            data = urllib.urlencode(postdata)
            response = urllib.urlopen("http://imgur.com/api/upload.json", data)
            return json.loads(response.read())

    def upload_from_url(self, image):
        """
        Upload an image to imgur.
        'image' must be a URL
        Returns the parsed json that imgur returns.
        """
        if self.apikey is None:
            raise imgurAPIError, "API Key is missing."
            return None
        else:
            postdata = {"key": self.apikey,
                        "image": image}
            data = urllib.urlencode(postdata)
            response = urllib.urlopen("http://imgur.com/api/upload.json", data)
            return json.loads(response.read())  

    def delete(self, dhash):
        """
        Delete an image from imgur.
        dhash is the delete hash found in the object returned by a call to
         imgur.upload
        Returns the parsed json that imgur returns.
        """
        response = urllib.urlopen("http://imgur.com/api/delete/%s.json" % dhash)
        return json.loads(response.read())

    def istats(self, ihash):
        """
        Returns the image's stats corresponding to its hash, ihash.
        """
        response = urllib.urlopen("http://imgur.com/api/stats/%s.json" % ihash)
        return json.loads(response.read())

    def stats(self, view="all"):
        """
        Returns imgur statistics.
        """
        data = urllib.urlencode({"view": view})
        response = urllib.urlopen("http://imgur.com/api/stats.json", data)
        return json.loads(response.read())

    def gallery(self, sort="latest", view="all", count=20, page=1):
        """
        Returns the stats of several images from the imgur database.
        There is no way to specify which images are returned.
        """
        postdata = {"sort": sort,
                    "view": view,
                    "count": count,
                    "page": page}
        data = urllib.urlencode(postdata)
        response = urllib.urlopen("http://imgur.com/api/stats.json", data)
        return json.loads(response.read())
