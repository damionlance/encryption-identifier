import boto3
import os

s3 = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIAW7OJN743EUSIMKV6',
    aws_secret_access_key='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'
)

s3_resource = boto3.resource(
   's3',
   aws_access_key_id='AKIAW7OJN743EUSIMKV6',
   aws_secret_access_key='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')

for bucket in s3_resource.buckets.all():
    print(bucket.name)

BUCKET = 'sc-bucket2'
KEY = os.urandom(32)

print("Put object...")
s3.put_object(Bucket=BUCKET,
              Key='f1', Body=b'foobar',
              SSECustomerKey=KEY,
              SSECustomerAlgorithm='AES256')
print("Done")
# Make sure to save the KEY!

# Getting the object:
print("Getting object...")
response = s3.get_object(Bucket=BUCKET,
                         Key='f1',
                         SSECustomerKey=KEY,
                         SSECustomerAlgorithm='AES256')
print("Done, response body:")
print(response['Body'].read())