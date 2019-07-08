from __future__ import print_function
import boto3
import json
import datetime


s3 = boto3.resource('s3')
dnow=datetime.datetime.now()
rdate=dnow.strftime("%Y%m%d%I")
f_log= "snslog" + rdate
formattxt=f_log + '.txt'

config = s3.meta.client.get_object(Bucket='snssqslogbuckets',Key="awsconfigwhitelist.txt")['Body'].read().decode('utf-8') 
config_w_list= [line.strip() for line in config.split('\n')]


buckets=[]
for bucket in s3.buckets.all():
    buckets.append(bucket.name)
    
if 'snssqslogbuckets' in buckets:
    print('snssqslogbuckets is already in S3')
else:
    s3.create_bucket(Bucket='snssqslogbuckets',CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

account=['707079114649/','450488471598/']
for x in account:
    try:
 
        s3.meta.client.put_object(Bucket='snssqslogbuckets',Key=x+formattxt)
        print('file created under account')
    except:
        print('already available')



fileobj = s3.meta.client.get_object(Bucket='snssqslogbuckets',Key="707079114649/"+formattxt)['Body'].read().decode('utf-8') 
L1= [line for line in fileobj.split('\n')]

fileobj = s3.meta.client.get_object(Bucket='snssqslogbuckets',Key="450488471598/"+formattxt)['Body'].read().decode('utf-8') 
L2= [line for line in fileobj.split('\n')]
print(L2)

def lambda_handler(event, context):
    print("Received event: ", event)
    try:
        try:
            config_rule_list=[json.loads(a["Sns"]["Message"])["detail"]["additionalEventData"]["configRuleName"] for a in Event["Records"]]
        except:
            config_rule_list = json.loads(event['Records'][0]['Sns']['Message'])['detail']['configRuleNames']
        
        len_config_rule=len(config_rule_list)
        for x in range(len_config_rule):
            print (config_w_list)
            if config_rule_list[x] in config_w_list:
                print('yes')
                try:
                    message = event['Records'][0]['Sns']['Message']
                    c="""{}""".format(message)
                    if 707079114649 == int(json.loads(c)['account']):
                        L1.append(c)
                        x='\n'.join(map(str, L1))
                        k="707079114649/"+formattxt
                        s3.Object('snssqslogbuckets',k ).put(Body=x,ContentType='text')
                    elif 450488471598 == int(json.loads(c)['account']):
                        L2.append(c)
                        x='\n'.join(map(str, L2))
                        k="450488471598/"+formattxt
                        s3.Object('snssqslogbuckets',k ).put(Body=x,ContentType='text')
                    return message
                finally:
                        message = event
                        L1.append(message)
                        x='\n'.join(map(str, L1))
                        k="450488471598/"+formattxt
                        s3.Object('snssqslogbuckets',k ).put(Body=x,ContentType='text')
                        return message
            else:
                print('no')
    except:
        print("check the configRuleNames in event ")

    


