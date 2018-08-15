#!/usr/bin/python
import boto3, botocore

conn = boto3.resource('s3')

# Function to delte a bucket and its content
def delbucket():
	bucketName = raw_input("Get the bucket name to delete: ")
	bucket = conn.Bucket(bucketName) #Get the bucket Object
	num = 0
        # Delete all the files in the bucket first
	for file in bucket.objects.all():
		num += 1
		print "Deleting file: " +file.key
		file.delete() #Delete the object
	print "Deleting bucket: " +bucketName
	bucket.delete(bucketName)
