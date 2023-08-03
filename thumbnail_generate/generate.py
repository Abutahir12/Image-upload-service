import boto3
from PIL import Image
from io import BytesIO
import os
import json
from reuse_methods.constants import USER_IDS, BUCKET_NAME
from reuse_methods.http_methods import (
    ok_response,
    forbidden_response,
    bad_request_response,
    internal_server_error_response,
)

s3 = boto3.client("s3")
sqs = boto3.client("sqs")

def create_thumbnail(event, context):
    print("Input to lambda", event)

    sqs_message = json.loads(event['Records'][0]['body'])
    object_key = sqs_message['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    print(obj)
    image = Image.open(BytesIO(obj["Body"].read()))

    thumbnail_size = (100, 100)  # Create the thumbnail of 100 x 100 pixels
    thumbnail = image.copy()
    thumbnail.thumbnail(thumbnail_size)

    thumbnail_key = (
        os.path.splitext(object_key)[0].replace("images", "thumbnail")
        + "_thumbnail.jpg"
    )  # Save the thumbnail to S3

    print(thumbnail_key)
    thumbnail_data = BytesIO()
    thumbnail.save(thumbnail_data, format="JPEG")
    s3.put_object(Bucket=BUCKET_NAME, Key=thumbnail_key, Body=thumbnail_data.getvalue())

    print(object_key)
    
    # Delete the processed message from SQS
    receipt_handle = sqs_message['Records'][0]['receiptHandle']
    sqs.delete_message(QueueUrl="https://sqs.ap-south-1.amazonaws.com/594108745002/images-service-messaging-queue", ReceiptHandle=receipt_handle)
    # return ok_response(object_key)





