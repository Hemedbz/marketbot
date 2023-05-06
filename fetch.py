import requests
from cache import Cache
from exceptions import *

BASE_URL = "https://api.bridgedataoutput.com/api/v2/rets/dataset_id/search?SearchType=Property&Query=(StandardStatus=Active)"


class Fetcher:
    def __init(self, zws_id, location):
        self.api_key = zws_id
        self._header = {}
        self._cache = Cache()
        self.top = 50
        self.auth_token = ""

    def establish_session(self):
        pass
        # first, establish a session. Output is auth token

    def set_top_listings(self, top: int):
        """
        Change the number of maximal listings per query.
        Default is 50
        """
        if 0 > top < 201:
            self.top = top
            return self.top

        else:
            raise OutOfRange(top)
