import boto3
import os
import classifyDirectory

s3 = boto3.client('s3')
s3_buck = boto3.resource('s3')

response = s3.list_buckets()
train_data = r"../train_data.csv"

for bucket in response['Buckets']:
    my_bucket = s3_buck.Bucket(bucket["Name"])
    for bucket_object in my_bucket.objects.all():
        path = rf"../temp/{bucket_object.key}"
        s3.download_file(my_bucket.name, bucket_object.key, path)
        classifyDirectory.classify_directory(path, train_data)
        os.remove(path)
