from threading import Lock
from textfiles import json_file


class Cache:

    def __init__(self, file_name):
        self._file_name = file_name
        self._content = {}
        self._lock = Lock()

    def __str__(self):
        return self._content

    def __contains__(self, item):
        if item in str(self._content):
            return True
        else:
            return False

    def put(self):
        pass

    def fetch(self):
        pass

