from reuse_methods.constants import BUCKET_DOMAIN
from reuse_methods.http_methods import (
    ok_response,
    bad_request_response,
    internal_server_error_response,
    forbidden_response
)
from reuse_methods.constants import USER_IDS

def download_thumbnail(event, context):
    print("Input to lambda", event)

    query = event.get("queryStringParameters")
    user_id = query["user_id"]

    if (
        user_id not in USER_IDS
    ):  # These hard-coded UUIDs just simulate the authorized users flow
        return forbidden_response("The user is un-authorized to access this resource")

    if not len(query) and "user_id" not in query:
        return bad_request_response("Missing user id")

    key = f"{user_id}/thumbnail/cat_thumbnail.jpg"
    url = f"{BUCKET_DOMAIN}/{key}" # We can also use pre-signed URL, but since it's a public bucket we can construct the URL

    return ok_response({"download_url": url})