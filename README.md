# Image-upload-service

This project contains 3 APIs and a lambda function

**Upload an image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/upload` -> The images are present inside a folder called input so you can directly make use of the same, since there's no UI to specifically select an image.

**download the image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/image?user_id=eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3`

**download the thumbnail** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/thumbnail?user_id=eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3`
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

**NOTE**
Please use only any of these User Ids:
```
USER_IDS = [
    "eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3",
    "ebe7b1c9-951b-4f92-aa42-9d65c19a8fc5",
    "ab11ed09-03da-4d77-9b8d-6d07b5db1e5e",
    "b92a45f3-147d-4829-a362-d798282a041e",
    "6edc5e55-2c2a-4e3e-8d1c-5044f6c68d09",
]


