"""
This script generates all PCI instances per account, per region
This script takes 2 commands: aws_account_profile, and region
"""
import boto3
import boto3.session
import sys

aws_account_profile = sys.argv[1]
region = sys.argv[2]

my_session = boto3.session.Session(
    profile_name=aws_account_profile,
    region_name=region)  # Establshing a session with your profile
ec2 = my_session.client("ec2")  # Using ec2 sdk

# Get all ec2 instances with pci tags
response = ec2.describe_instances(
    Filters=[
        {
            "Name":
            "tag:Name",
            "Values": [
                "Application",
                "ndcdms"
            ]
        },
    ], )

# print(response["Reservations"])

pci_instances_list = []
for item in response["Reservations"]:
    for x in item["Instances"]:
        pci_instances_list.append(x["InstanceId"])

print(pci_instances_list)
