import requests
from cache import Cache


class Fetcher:
    def __init(self, zws_id, location):
        self.api_key = zws_id
        self._header = {}
        self._cache = Cache()

