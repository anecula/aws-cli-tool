#!/usr/bin/env python

import boto3
import datetime
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["TimePeriod", "LinkedAccount, Service", "Amount", "Unit" , "Estimated"]
#x.field_names = ["TimePeriod", "LinkedAccount", "Service", "Amount", "Unit" , "Estimated"]


now = datetime.datetime.utcnow()
start = (now - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
end = now.strftime('%Y-%m-%d')

#cd = boto3.client('ce', 'ap-south-1')
cd = boto3.client('ce')

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

	#print data
	#print results
	#print token

	#print('\t'.join(['TimePeriod', 'LinkedAccount', 'Service', 'Amount', 'Unit', 'Estimated']))
	for result_by_time in results:
	    for group in result_by_time['Groups']:
		timeperiod = result_by_time['TimePeriod']['Start']
		account = group['Keys']
		#service = group['SERVICE']
	        amount = group['Metrics']['UnblendedCost']['Amount']
	        unit = group['Metrics']['UnblendedCost']['Unit']
		estimated = result_by_time['Estimated']
		x.add_row([timeperiod, account, amount, unit, estimated])
		#x.add_row([timeperiod, account, service, amount , unit, estimated])
	        #print(result_by_time['TimePeriod']['Start'], '\t', '\t'.join(group['Keys']), '\t', amount, '\t', unit, '\t', result_by_time['Estimated'])
		#print group['Keys']
	print(x)

