#!/usr/bin/env python

import boto3
import datetime
from prettytable import PrettyTable

# Used PrettyTable for displaying the results in tabular format
x = PrettyTable()
x.field_names = ["TimePeriod", "LinkedAccount, Service", "Amount", "Unit" , "Estimated"]

# Get the current date, start date(by default 30 days earlier)
now = datetime.datetime.utcnow()
start = (now - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
end = now.strftime('%Y-%m-%d')


cd = boto3.client('ce')

# Function to get the cost usage 
def costusage():
	results = []
	token = None
	while True:
	    if token:
        	kwargs = {'NextPageToken': token}
	    else:
	        kwargs = {}
	    data = cd.get_cost_and_usage(TimePeriod={'Start': start, 'End':  end}, Granularity='DAILY', Metrics=['UnblendedCost'], GroupBy=[{'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'}, {'Type': 'DIMENSION', 'Key': 'SERVICE'}], **kwargs)
	    results += data['ResultsByTime']
	    token = data.get('NextPageToken')
	    if not token:
        	break

	for result_by_time in results:
	    for group in result_by_time['Groups']:
		timeperiod = result_by_time['TimePeriod']['Start']
		account = group['Keys']
	        amount = group['Metrics']['UnblendedCost']['Amount']
	        unit = group['Metrics']['UnblendedCost']['Unit']
		estimated = result_by_time['Estimated']
		x.add_row([timeperiod, account, amount, unit, estimated])
	print(x)

