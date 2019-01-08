# Akamai Extend Credential period
This script allows you to extend API credential expiration date more than 2 years(2 years is the limitation from LUNA UI)

# Verified
Python 3.6.3 on windows

Python 2.7.14 on windows

# Prereq
You might need to install following modules.

>pip install requests

>pip install edgegrid-python  # provided by Akamai

# How to use

1.Download credential file form LUNA portal

2.Rename the credential file to **credential.txt**

3.Edit extend_credential.py

-----------------------

"expiresOn": "2018-02-24T22:43:12.000Z",

headers = {'Content-Type':'application/json'}

data = {

   "status": "ACTIVE",

   "expiresOn": "**2032-02-24T22:43:12.000Z**",  # **<== Edit this time**

   "description": "Test extention"

}

-----------------------

4.execute "python extend_credential.py"
