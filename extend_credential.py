# ----------------------------------------------------------
# Name: extend_credential.py
# Perpose: Extend expiration date of APLI client
# 2019/01/08 : yuhki initial release
# ----------------------------------------------------------
import requests
import json
import os
from akamai.edgegrid import EdgeGridAuth 
# from urlparse import urljoin # for Python 2.x
# from urllib.parse import urljoin # for Python 3.x

# -----------------------
# Debug: Request Dump
# -----------------------
def httpdump():
    print(request_url) # Dump Request URL
    print(result.request.headers) # Dump HTTP Request Header
    print(result.request.body) # Dump HTTP Requset body


# ----------------------------------------
# Open a credential file
# It is assumed that you use a credential file dwonloaded from LUNA portal as is.
# When you download the credntial file from LUNA. The format is like below. (space separated)
# ------- (These values are dummy) -------
# Please insert space as a sperator
# client_secret = 1Ul0WtarfadfgfgafgPo2XRmAsbPbzjw=
# host = akab-jza67c2hm2atagfasfgsafgurr67wf.luna.akamaiapis.net
# access_token = akab-ape6fgagfayrafa-532hlfdttj2sxxq6
# client_token = akab-ruu3utadfasrfdn-elmvfqhpi5l6oezf
# ----------------------------------------

# Check if a credential file exists
credential_file = "./credential.txt"
if os.path.exists(credential_file):
    file = open('credential.txt','r')
    lines = file.readlines()
    file.close
else:
    print("[ERROR]Please download a credential file from LUNA and name it credential.txt and place it in the same directory")
    exit()

file = open('credential.txt','r')
lines = file.readlines()
file.close

# Read the credential.txt
for line in lines:
    if line.find("client_secret") >=0:
       client_secret = line[:-1].split(" ")[2]
       # sclient_secret='client_secret=' + client_secret
       # print(sclient_secret)
    if line.find("host") >=0:
       host = line[:-1].split(" ")[2]
       # shost='host=' + host
       # print(shost)
    if line.find("access_token") >=0:
       access_token = line[:-1].split(" ")[2]
       # saccess_token = "access_token=" + access_token
       # print(saccess_token)
    if line.find("client_token") >=0:
       client_token = line[:-1].split(" ")[2]
       # sclient_token = "client_token=" + client_token
       # print (sclient_token)

# -----------------------
# Set values to EdgeGridAuth 
# -----------------------
baseurl = 'https://' + host
s = requests.Session()
s.auth = EdgeGridAuth(
client_token,
client_secret,
access_token
)

# -----------------------
# OpenIdentityId 
# This is visible from LUNA
# -----------------------
openIdentityId = "44gduvabyknvb2hf"

# -----------------------
# List credential ID 
# This will return all credential IDs under the same openIdentiyId.
# So, need to screen by client_token in the credential file.
# -----------------------
request_url = 'https://' + host + "/identity-management/v1/open-identities/" + openIdentityId + "/credentials"
result = s.get(request_url) 

data = result.json() # Response to JSON 

for key in data:
    if key['clientToken'] == client_token:
        credentialId = str(key['credentialId']) # Find out credentialId. int to str
        # ----- For Debug ----- 
        # print(key['credentialId']) 
        # print(key['clientToken']) 
    

# -----------------------
# Prpare JSON object to set Expiration date
# -----------------------
#  expiration date formati is like below
# "expiresOn": "2018-02-24T22:43:12.000Z",

headers = {'Content-Type':'application/json'}
data = {
     "status": "ACTIVE",
     "expiresOn": "2022-02-24T22:43:12.000Z",
     "description": "Extend expiresOn time"
}


# -----------------------
# Set Expiration date
# -----------------------
request_url = 'https://' + host + '/identity-management/v1/open-identities/' + openIdentityId + '/credentials/' + credentialId
result = s.put(request_url,data=json.dumps(data), headers=headers)  

# print(result.status_code) # HTTP Reponse Code 


# -----------------------
# Get the credential to confirm the change
# -----------------------
request_url = 'https://' + host + '/identity-management/v1/open-identities/' + openIdentityId + '/credentials/' + credentialId + "?actions"
result = s.get(request_url)  

print(result.status_code) # HTTP Reponse Code 
print(json.dumps(result.json(),indent=2))


