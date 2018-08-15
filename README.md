# aws-cli-tool
Simple tool to get AWS S3 details

Pre-requisites:
  1. Python should be available
  2. Python libraries boto3, botocore should be installed.(These may be also installed during the installation of the tool)


Installation:
  1. Once the code is downloaded, run th einstallation script(installscript)
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
