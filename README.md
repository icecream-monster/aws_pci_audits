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

### Firewall scripts

- `find_pci_sgs.py` will generate all security groups for all ec2 instances that have PCI tags
- `pci_sg_rulesets.py` will generate all ingress and egress rules for each security group you need

### Access Control Review scripts
- `sso_permission_set.py` will generate a detailed acccess review report based on each Group/User, Roles associated with each principal, and the Permission set ARN associated with each Role
