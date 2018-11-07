# coding:utf-8
import urllib

import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        header = {"User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        response = requests.get(url, headers=header, )

        if response.status_code != 200:
            return None

        return response.content.decode('utf-8')