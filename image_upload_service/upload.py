import boto3
import os
import json
from reuse_methods.constants import USER_IDS, BUCKET_NAME
from reuse_methods.http_methods import (
    create_response,
    forbidden_response,
    bad_request_response,
    internal_server_error_response,
)

s3 = boto3.client("s3")

def upload_image_to_s3(bucket_name, file_path, object_name):
    """_summary_

    Args:
        bucket_name (string): The bucket name where the file will be uploaded
        file_path (string): The path to file that needs to be uploaded
        object_name (string): The path where the file will be stored in S3

    Returns:
        Bool: Returns boolean if the file is successfully uploaded
    """
    try:
       
        s3.upload_file(file_path, bucket_name, object_name)
        return True
    except Exception as e:
        print(f"Error uploading image: {e}")
        return False


def handler(event, context):
    print("Input to lambda", event)

    if "body" not in event:
        return bad_request_response("Request body not available")

    body = json.loads(event["body"])

    if "file_name" not in body or "user_id" not in body:
        return bad_request_response("Mandatory fields not provided")

    filename = body["file_name"]
    user_id = body["user_id"]

    if (
        user_id not in USER_IDS
    ):  # These hard-coded UUIDs just simulate the authorized users flow
        return forbidden_response("The user is un-authorized to access this resource")

    try:
        file_path = os.path.join("inputdata", filename)
        object_name = f"{user_id}/images/{filename}"

        upload_successful = upload_image_to_s3(BUCKET_NAME, file_path, object_name)
        if upload_successful:
            return create_response("Image uploaded successfully")
        return bad_request_response("Image upload not successful")
    except Exception as e:
        return internal_server_error_response(e)
