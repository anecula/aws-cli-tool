#!/usr/bin/python
import argparse
import sys
import getalls3details as gs3
import deletebucket as ds3
import costreport as cr

# Main function to get all the details and run the tool
def main():
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Python tool to get AWS S3 details')
    # Add arguments
    parser.add_argument(
        '-g', '--getdetails', action='store_true', help='Get AWS S3 details')
    parser.add_argument(
        '-d', '--delete', action='store_true', help='Delete an S3 bucket')
    parser.add_argument(
        '-c', '--cost', action='store_true', help='Display the cost report')
    
    # Array for all arguments passed to script
    args = parser.parse_args()
    
    if args.getdetails:         # If true, get S3 details
	gs3.getdetails()
    elif args.delete:           # If true, delete a bucket
	ds3.delbucket()
    elif args.cost:             # if true, get the cost report
	cr.costusage()

if __name__ == '__main__':
    main()
