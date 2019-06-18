### All Account Details using AWS Oragnizations

## Consolidated view of Account details , including account type , Account ID etc.


# Script to Find All Account Details and Associated Account Details in the AWS Organizations
from collections import defaultdict
import getpass
import boto3
import csv

#AWS_ACCOUNT_ID = input("Enter Your AWS ACCOUNT ID : ")
getpass.getpass(prompt='AWS_ACCOUNT_ID: ', stream="None")
organizations = boto3.client('organizations')
account_list = organizations.list_accounts()

s_no=1
# Output File Creation 
f=open('AccountDetails.csv','w')
my=csv.writer(f,delimiter=' ',lineterminator='\n')  
head=['S.No','Account id','ARN','Status','Account Type'] 
my.writerow(head)

 
MASTER_ACCOUNT_ID = #provide MASTER ID

"""
encoded = encode(MASTER_ACCOUNT_ID,"password")
print(encoded)
decoded = decode(encoded,"password")
print(decoded)
"""
for y in account_list['Accounts']:
    #if (MASTER_ACCOUNT_ID == int(AWS_ACCOUNT_ID)):
    if (MASTER_ACCOUNT_ID == int(y['Id'])):
        print("This is a Master Account")
        ACCOUNT_TYPE = "Master"
    else:
        print("This is a Consolidated Joined Account")
        ACCOUNT_TYPE = "Joined"
    print(y['Id'])
    print(y['Arn'])
    print(y['Status'])       
    my.writerow([s_no,y['Id'],y['Arn'],y['Status'],ACCOUNT_TYPE])
