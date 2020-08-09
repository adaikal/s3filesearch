#!/usr/bin/python3
import boto3
import re

s3res = boto3.resource('s3')
s3client = boto3.client('s3')
response = s3client.list_buckets()

findfile = input("Enter file to be searched: ")
search_string = '^.*'+findfile+'.*$'

for bucket in response['Buckets']:
    bucket_name = bucket["Name"]
    found_buckets = re.findall("^.*cust.*$",bucket_name, re.IGNORECASE)
    if found_buckets:
        print(f'Found Bucket:  {found_buckets}')
        for found_bucket in found_buckets:
            my_bucket = s3res.Bucket(name=found_bucket)
            for my_bucket in my_bucket.objects.all():
                found_file = re.findall(search_string,my_bucket.key,re.IGNORECASE)
                if found_file:
                    print(f'Found File: {found_file}')
