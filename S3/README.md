#S3 Recent Code Fetch 

##Purpose: 
          When an Ec2 instance is stopped ,autoscaling will trigger another instance from the AMI Created ,which contains the old code .
To get updated code from instance during launch we use 'UserData' to pass the script.

##Requirements:
  1. ASG associated with Instance.
  2. And ELB running on top of ASG.
  3. S3 Bucket for storing the code.
  4. Jenkins to deploy the code and send to S3 Release area.
