# coding:utf-8
import urllib

import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = requests.get(url, allow_redirects=False)

        if response.status_code != 200:
            return None

        return response.content