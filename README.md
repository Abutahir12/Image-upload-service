# Image-upload-service

- Architecture
- Documentation
- IMPORTANT NOTE

## Architecture

In the AWS console, there are the following resources:

1. A Source S3 Bucket that will be used for the input.
2. A Destination S3 Bucket that will be store as a destination bucket.
3. A SQS queue that will be triggered when an object is put into s3.
4. A SQS queue that will be a dead-letter queue that will hold failure events.
5. A Lambda that processes the image to thumbnail and stores in destination S3 bucket.
6. An API that can be used to upload the file.
7. An API to download the original image.
8. An API to download the thumbnail image.


## Documentation

This project contains 3 APIs and a lambda function

**Upload an image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/upload` -> The images are present inside a folder called input so you can directly make use of the same, since there's no UI to specifically select an image.

**download the image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/image?user_id=ab11ed09-03da-4d77-9b8d-6d07b5db1e5e&image_id=cat`

**download the thumbnail** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/thumbnail?user_id=ab11ed09-03da-4d77-9b8d-6d07b5db1e5e&image_id=cat`
A lambda which will convert the image to URL

**The SQS and S3 resources are available in my personal AWS Account.**

**Fixed this issue:** _There was an issue with an external dependency in lambda W.R.T thumbnail generation, the code worked fine in local, however, in the provided time I was not able to resolve the underlying cause for the same, I have fixed this now_

To run these APIs you can provide the following inputs:

**Upload API:**

```
{
    "file_name": "cat.jpg",
    "user_id": "eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3"
}
```

**Download images APIs**: The Query parameter is already provided

## IMPORTANT NOTE
Please use only any of these User Ids and Use either `dog` or `cat` as Image id, since it doesn't have a database these images are stored along with the code:
```
USER_IDS = [
    "eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3",
    "ebe7b1c9-951b-4f92-aa42-9d65c19a8fc5",
    "ab11ed09-03da-4d77-9b8d-6d07b5db1e5e",
    "b92a45f3-147d-4829-a362-d798282a041e",
    "6edc5e55-2c2a-4e3e-8d1c-5044f6c68d09",
]
```
