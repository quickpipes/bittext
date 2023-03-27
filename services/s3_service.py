import boto3
from botocore.exceptions import ClientError
import os


class S3Service:
    """A class to implement s3 capabilities"""

    def __init__(self) -> None:
        # Defining bucket from environment variables
        self.bucket = os.getenv("BUCKET_NAME")
        region_name = os.getenv("REGION")
        endpoint_url = os.getenv("S3_ENDPOINT_URL")
        scaleway_access_key_id = os.getenv("ACCESS_KEY_ID")
        scaleway_secret_access_key = os.getenv("ACCESS_KEY")
        self.s3 = boto3.resource(
            "s3",
            region_name=region_name,
            use_ssl=True,
            endpoint_url=endpoint_url,
            aws_access_key_id=scaleway_access_key_id,
            aws_secret_access_key=scaleway_secret_access_key
        )
        pass

    def s3_read(self, file: str) -> str:
        # Get object from S3
        obj = self.s3.Object(self.bucket, file)

        # Read object content
        # be careful to choose the right encoding
        return obj.get()["Body"].read().decode("utf-8")

    def s3_write(self, file: str, content: str) -> bool:
        try:
            obj = self.s3.Object(self.bucket, file)
            obj.put(Body=content)
        except ClientError as e:
            print("Error while writing file: ", e)
