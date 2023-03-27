from datetime import datetime
import hashlib
from models.bittext import Bittext
from services.s3_service import S3Service


class BittextService:
    """A class to manage Bittexts."""

    def __init__(self) -> None:
        self.s3Service = S3Service()
        pass

    def create_bittext(self, content: str) -> Bittext:
        bittext = Bittext()
        bittext.content = content
        bittext.creation_date = datetime.now()

        bittext.hash = hashlib.md5(
            f"{bittext.creation_date.timestamp()}-{bittext.content}".encode('UTF-8')).hexdigest()

        self.s3Service.s3_write(file=bittext.hash, content=bittext.content)
        return bittext

    def get_bittext(self, hash: str) -> Bittext:
        content = self.s3Service.s3_read(file=hash)

        bittext = Bittext()
        bittext.content = content
        bittext.hash = hash

        return bittext
