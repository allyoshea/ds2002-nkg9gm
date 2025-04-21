#!/opt/anaconda3/bin/python
import boto3 
import urllib.request  
import sys
s3=boto3.client('s3', region_name='us-east-1')
url=sys.argv[1]
bucket=sys.argv[2]
file_name=url.split("/")[-1]
urllib.request.urlretrieve(url,file_name) 
s3.upload_file(file_name, bucket, file_name, ExtraArgs={'ACL': 'public-read'})

# Generate a public URL (S3 static website endpoint or direct link)

presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': file_name},
    ExpiresIn=3600  
)
# Output the presigned URL
print(presigned_url)
