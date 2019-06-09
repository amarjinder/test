#!/bin/env python

import argparse, json, requests

parser = argparse.ArgumentParser("Get Company Name from given mac address using api.macaddress.io REST api")
parser.add_argument("--macaddr", required=True, help="MAC address")
parser.add_argument("--apitoken", required=True, help="api.macaddress.io API token")
args = parser.parse_args()

macaddr = args.macaddr
apitoken = args.apitoken

url = "https://api.macaddress.io/v1?apiKey=" + apitoken + "&output=json&search=" + macaddr 

response = requests.get(url)
data = json.loads(str(response.content))
print "Company Name %s" % (data["vendorDetails"]["companyName"])
