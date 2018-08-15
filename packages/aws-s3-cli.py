#!/usr/bin/python
import argparse
import sys
import getalls3details as gs3
import deletebucket as ds3
import costreport as cr

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
    
    if args.getdetails:
	gs3.getdetails()
    elif args.delete:
	ds3.delbucket()
    elif args.cost:
	cr.costusage()

if __name__ == '__main__':
    main()
