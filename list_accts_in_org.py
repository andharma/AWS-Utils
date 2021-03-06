import boto3
import botocore
import os
import sys

#Patrick McBrien
#THIS FINDS ALL REGIONS IN ORG AND LOOPS THROUGH ALL ACCOUNTS IN ORG AND DUMPS NAME

def paginate(method, **kwargs):
    client = method.__self__
    paginator = client.get_paginator(method.__name__)
    for page in paginator.paginate(**kwargs).result_key_iters():
        for result in page:
            yield result

# List all regions
ec2_client = boto3.client('ec2')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
#print(regions)

for region in ec2_client.describe_regions()['Regions']:
    region_name = region['RegionName']
    #
    org_client = boto3.client('organizations')
    for account in paginate(org_client.list_accounts):
        print (" AccountId  " + str(account['Id']))
        print (account['Id'], account['Name'], account['Arn'])
        #if account['Id'] != rootaccount:
        #print (account['Status'])
        #if account['Id'] != '134': #use if you want to leave out ROOT account.

        # use aws credential profile
        #session = boto3.Session(profile_name='takeda')

        #if account['Status'] == 'ACTIVE':

           # sc_client=boto3.client('ec2', region_name=region_name)
           # try:
            #    response = sc_client.describe_vpcs()
             #   resp = response['Vpcs']
             #   if resp:
             #       for rp in resp:
                        #if rp['IsDefault']:

              #          print('\n\n')
              #          print ("AccountId " + str(account['Id']))
              #          print ("Region " + region_name )
              #          print("OwnerId " + rp['OwnerId'])
              #          print("VPCId " + rp['VpcId'])
              #          print (rp['CidrBlock'])

               # else:
               #     print('No vpcs found')
            #except:
            #    print("Error getting")
            #    raise




