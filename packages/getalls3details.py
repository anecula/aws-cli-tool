import boto3, botocore
from prettytable import PrettyTable

conn = boto3.resource('s3')
buckets=conn.buckets.all()

def getdetails():
	total_bytes=0
	num=0
	last_modified=0
	x = PrettyTable()
	x.field_names = ["Bucket Name", "Creation Date", "No of files", "Total size of all files", "Last modified time"]
	for bucket in buckets:
        	for key in bucket.objects.all():
                	total_bytes += key.size
                	last_modified = key.last_modified
                       	num += 1
                #if num != 0:
		total_size=total_bytes/1024
		x.add_row([bucket.name, bucket.creation_date, num, total_size, last_modified])
			
	print(x)
