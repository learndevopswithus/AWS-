#instancecreation_tr.py
#Creating Basic Infrastrcture with Troposphere
from troposphere import Ref, Template
import troposphere.ec2 as ec2
 
t = Template()
instance = ec2.Instance("myinstance")
instance.ImageId = "ami-0cc96feef8c6bbff3"
instance.InstanceType = "t2.micro"
t.add_resource(instance)
print(t.to_yaml())


