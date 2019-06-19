from __future__ import print_function
from troposphere import ec2
from troposphere import Tags, ImportValue
from troposphere import Template
# create the object that will generate our template
t = Template()
ec2_learncf_1a = ec2.Instance("MyInstance")
ec2_learncf_1a.ImageId = "ami-035b3c7efe6d061d5" # ADJUST IF NEEDED
ec2_learncf_1a.InstanceType = "t2.micro"
ec2_learncf_1a.SubnetId = ImportValue("MyStack-MySubnet1b")
ec2_learncf_1a.Tags = Tags(
Name="learncf",
Comment="Learning CloudFormation and Troposphere")


t.add_resource(ec2_learncf_1a)
# Finally, write the template to a file
with open('learncf-ec2.json', 'w') as f:
    f.write(t.to_json())