#!/bin/env python

import argparse, json, requests

parser = argparse.ArgumentParser("MAC address lookup")
parser.add_argument("--macaddr", required=True, help="MAC address")
parser.add_argument("--apitoken", required=True, help="API token")
args = parser.parse_args()

macaddr = args.macaddr
apitoken = args.apitoken

url = "https://api.macaddress.io/v1?apiKey=" + apitoken + "&output=json&search=" + macaddr 

response = requests.get(url)
data = json.loads(str(response.content))
print "Company Name %s" % (data["vendorDetails"]["companyName"])
