import boto3
from reuse_methods.constants import BUCKET_DOMAIN
from reuse_methods.http_methods import (
    ok_response,
    bad_request_response,
    internal_server_error_response,
)

s3 = boto3.client("s3")


def download_image(event, context):
    print("Input to lambda", event)

    query = event.get("queryStringParameters")
    user_id = query["user_id"]

    if not len(query) and "user_id" not in query:
        return bad_request_response("Missing user id")

    key = f"{user_id}/images/cat.jpg"
    url = f"{BUCKET_DOMAIN}/{key}"

    return ok_response({"download_url": url})