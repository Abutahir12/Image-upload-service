import boto3
from reuse_methods.constants import BUCKET_DOMAIN
from reuse_methods.http_methods import (
    ok_response,
    bad_request_response,
    internal_server_error_response,
)

s3 = boto3.client("s3")

def download_thumbnail(event, context):
    print("Input to lambda", event)

    query = event.get("queryStringParameters")
    user_id = query["user_id"]

    if not len(query) and "user_id" not in query:
        return bad_request_response("Missing user id")

    key = f"{user_id}/thumbnail/cat_thumbnail.jpg"
    url = f"{BUCKET_DOMAIN}/{key}" # We can also use pre-signed URL, but since it's a public bucket we can construct the URL

    return ok_response({"download_url": url})