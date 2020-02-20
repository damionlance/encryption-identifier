import boto3
import os
import glob
import classifyDirectory


def detect_from_aws():
    s3 = boto3.client('s3')
    s3_buck = boto3.resource('s3')

    response = s3.list_buckets()
    train_data = r"train_data.csv"

    for bucket in response['Buckets']:
        my_bucket = s3_buck.Bucket(bucket["Name"])
        for bucket_object in my_bucket.objects.all():
            if "." in bucket_object.key:
                s3.download_file(my_bucket.name, bucket_object.key, "./temp")
                classifyDirectory.classify_directory("temp", train_data)
                files_in_temp = glob.glob("temp/*")
                for f in files_in_temp:
                    os.remove(f)
