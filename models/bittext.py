from datetime import datetime


class Bittext:
    """A class to represente Bittexts"""

    def init(self):
        self._content = str
        self._hash = str
        self._creation_date = datetime

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, date: datetime):
        self._creation_date = date

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str):
        self._content = content

    @property
    def hash(self) -> str:
        return self._hash

    @hash.setter
    def hash(self, hash: str):
        self._hash = hash
