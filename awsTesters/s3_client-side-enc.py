import base64
import boto3
import os

s3 = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIAW7OJN743EUSIMKV6',
    aws_secret_access_key='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'
)

kms = boto3.client('kms')

    # Hard coded strings as credentials, not recommended.
#    aws_access_key_id='AKIAW7OJN743EUSIMKV6',
#    aws_secret_access_key='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'
#)

#s3 = boto3.resource(
#    's3',
#    aws_access_key_id='AKIAW7OJN743EUSIMKV6',
#    aws_secret_access_key='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')

#for bucket in s3.buckets.all():
#	print(bucket.name)

BUCKET = 'sc-bucket2'
KEY = '488af6d1-ae6c-4a63-aef0-d36c55a14b54'

print("encrypt object...")
encrypted = kms.encrypt(KeyId=KEY,
            Plaintext=b'sidechain')

base64EncodedStr = base64.b64encode(encrypted['CiphertextBlob'])

print (base64EncodedStr)




#print("Encrypted data: " + encrypted['CiphertextBlob'].read())

print("data encrypted...")
s3.put_object(Bucket=BUCKET,
              Key='obj1', Body=encrypted['CiphertextBlob'])

print("Done")
# Make sure to save the KEY!

# Getting the object:
print("Getting object...")
response = s3.get_object(Bucket=BUCKET,
                         Key='obj1')

d = response['Body']

#print("Done, encrypted data: " + response['Body'].read())

decrypted = kms.decrypt(CiphertextBlob=d.read(),
                      KeyId=KEY)

print("Decrypted: " + decrypted['Plaintext'].decode('utf-8'))
