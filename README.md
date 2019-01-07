# Akamai Extend Credential period
This script allows you to extend API credential expiration date more than 2 years(2 years is the limitation from LUNA UI)

# How to use

1.Download credential file form LUNA portal

2.Rename the file to credential.txt

3.Edit extend_credential.py 
-----------------------
"expiresOn": "2018-02-24T22:43:12.000Z",
headers = {'Content-Type':'application/json'}
data = {
     "status": "ACTIVE",
   **"expiresOn": "2032-02-24T22:43:12.000Z",**  <== Edit this portion
     "description": "Test extention"
}
-----------------------

4.execute "python extend_credential.py"
