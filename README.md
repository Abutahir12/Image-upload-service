# Image-upload-service

This project contains 3 APIs and a lambda function

**Upload an image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/upload` -> The images are present inside a folder called input so you can directly make use of the same, since there's no UI to specifically select an image.

**download the image** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/image?user_id=eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3`

**download the thumbnail** -> `https://eor05gw58j.execute-api.ap-south-1.amazonaws.com/dev/download/thumbnail?user_id=eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3`
A lambda which will convert the image to URL

**The SQS and S3 resources are available in my personal AWS Account.**

_There is an issue with an external dependency in lambda W.R.T thumbnail generation, the code works fine in local, however, in the provided time I was not able to debug the underlying cause for the same, but I am sure I'll be able to debug it_

To run these APIs you can provide the following inputs:

**Upload API: **
```
{
    "file_name": "dog.jpg",
    "user_id": "eb2128f2-5c0a-4dd1-90a5-2f0e39db7aa3"
}
```
**Download images APIs**: The Query parameter is already provided


