from __future__ import print_function
from troposphere import ec2
from troposphere import Tags, GetAtt, Ref, Sub, Export
from troposphere import Template, Output

# Create the object that will generate our template
t = Template()

#Subnet 1a
subnet_1a = ec2.Subnet("MySubnet1a")
subnet_1a.AvailabilityZone = "us-east-1a"
subnet_1a.CidrBlock = "10.0.2.0/24" # ADJUST THIS VALUE
subnet_1a.VpcId = "vpc-0595e8c0919acd368" # ADJUST THIS VALUE
subnet_1a.Tags = [
{"Key": "Name", "Value": "learncf-1a"},
{"Key": "Comment", "Value": "CloudFormation+Troposphere test"}]
t.add_resource(subnet_1a)

#Subnet 1b
subnet_1b = ec2.Subnet(
"MySubnet1b",
AvailabilityZone="us-east-1b",
CidrBlock="10.0.1.0/24", # ADJUST THIS VALUE
VpcId=GetAtt(subnet_1a, "VpcId"),
Tags=Tags(
Name="learncf-1b",
Comment="CloudFormation+Troposphere test"))
t.add_resource(subnet_1b)

#Subnet 1 Output
out_subnet_1a = Output("outMySubnet1a")
out_subnet_1a.Value = Ref(subnet_1a)
out_subnet_1a.Export = Export(Sub(
"${AWS::StackName}-" + subnet_1a.title))

# Similar output for the second subnet
out_subnet_1b = Output("outMySubnet1b")
out_subnet_1b.Value = Ref(subnet_1b)
out_subnet_1b.Export = Export(Sub(
"${AWS::StackName}-" + subnet_1b.title))

# Add outputs to template
t.add_output(out_subnet_1a)
t.add_output(out_subnet_1b)

# Finally, write the template to a file
with open('learncf-subnet.json', 'w') as f:
    f.write(t.to_json())