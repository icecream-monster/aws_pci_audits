# My AWS PCI Audit Scripts

My background is PCI compliance and security audits. However, when it comes to aws cloud, you really need a more effective way of calling your resources across multiple accounts and multiple regions.

I have devised the following scripts to automate PCI audits on aws cloud.

## Requirements

Mainly: `boto3` and `openpyxl`

## Usage

Recommending running in the following:

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install boto3
python3 -m pip install openpyxl
```

## Scripts

### Inventory script
- `system_review.py` will generate all ec2 instances that have PCI tags

### Firewall scripts

- `find_pci_sgs.py` will generate all security groups for all ec2 instances that have PCI tags
- `pci_sg_rulesets.py` will generate all ingress and egress rules for each security group you need
- `check_fw_permissions.py` will simulate every SSO role against firewall modification permissions. The roles that can simulate the following permissions will have: `Simulate Policy Decision: allowed`
> "ec2:AuthorizeSecurityGroupEgress", 
"ec2:AuthorizeSecurityGroupIngress", 
"ec2:CreateSecurityGroup", 
"ec2:DeleteSecurityGroup", 
"ec2:RevokeSecurityGroupEgress", 
"ec2:RevokeSecurityGroupIngress", 
"ec2:CreateNetworkAcl", 
"ec2:CreateNetworkAclEntry", 
"ec2:DeleteNetworkAcl", 
"ec2:DeleteNetworkAclEntry", 
"ec2:ModifyNetworkInterfaceAttribute", 
"ec2:ReplaceNetworkAclAssociation", 
"ec2:ReplaceNetworkAclEntry"

### Access Control Review scripts
- `sso_permission_set.py` will generate a detailed acccess review report based on each Group/User, Roles associated with each principal, and the Permission set ARN associated with each Role
