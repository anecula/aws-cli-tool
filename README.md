## aws-cli-tool
# Simple tool to get AWS S3 details

## Pre-requisites:
  1. Python should be available
  2. Python libraries: boto3, botocore and PrettyTable should be installed.
  	(These may be also installed during the installation of the tool - can be enabled in the installation script)
	
	PrettyTable	: https://pypi.org/project/PrettyTable/
	Boto3		: https://boto3.readthedocs.io/en/latest/
	Botocore	: https://botocore.readthedocs.io/en/latest/

## Basic Configuration

We will need to setup AWS security credentials before tool is able
to connect to AWS. We can do this by creating a file named "credentials" at ~/.aws/ 
and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

Also, we can use a specific region by creating a file named "config" at ~/.aws/ 
and saving the following lines in the file:
 
    [default]
    region = <your region >


## Installation:
  1. Once the code is downloaded, run the installation script(installscript)
           
	[user@hostname]# ./installscript
	Where do you want to install(For example: /opt/aws-tool): /opt/aws-tool
    	Installing the packages...
	Creating symlink...
    	Installation completed!
	
            
  2. On installation, we can run the tool from any directory. Below is a demonstration of the command that can be run.
    
  	
	[user@hostname]# aws-s3-cli -h
	
	usage: aws-s3-cli [-h] [-g] [-d] [-c]
	Python tool to get AWS S3 details
	
	optional arguments:
		-h, --help        show this help message and exit
		-g, --getdetails  Get AWS S3 details
		-d, --delete      Delete an S3 bucket
		-c, --cost        Display the cost report
		
		
		
  3. NOT DONE - Unit tests and additional exception handling
