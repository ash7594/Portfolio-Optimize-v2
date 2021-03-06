# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
from dotenv import load_dotenv
import json
import argparse
#from dotenv import load_dotenv
import os
import datetime
'''
#Initalize Investment Portfolio Service credentials to find on Bluemix otherwise from .env file
if 'VCAP_SERVICES' in os.environ:
    vcap_servicesData = json.loads(os.environ['VCAP_SERVICES'])
    # Log the fact that we successfully found some service information.
    print("Got vcap_servicesData\n")
    #print(vcap_servicesData)
    # Look for the IP service instance.
    uri=vcap_servicesData['fss-financial-optimization-service'][0]['credentials']['uri']
    accessToken=vcap_servicesData['fss-financial-optimization-service'][0]['credentials']['accessToken']
    # Log the fact that we successfully found credentials
    print("Got IP credentials\n")
else:
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    uri=os.environ.get("CRED_OPTIMIZER_uri")
    accessToken=os.environ.get("CRED_OPTIMIZER_accessToken")
'''
uri = "https://fss-analytics.mybluemix.net/"
accessToken="21124b48cae21fc9c02fb0d48399c79cbfb86afc61c2d673c3a3348b57cb4a1cb8090a92eea0766d71b7ecb20e78b06456e9b9c646facd40693ec4c45e4bbedd96ad2cdb33c084e7c1d8e53c97090b7c5aa8fa5f2ec8b040e90e30e2c184c17c3a077963799bb66f1a398fb32a53a05ab217588ba0468d5bc38d6819e0e5886e"
def Optimize(payload):
    """
    Optimizes a portfolio based on a payload with the following information:
    1) Objective
    2) Portfolios including universe, benchmarks, and subportfolios based on asset categorizations
    3) Constraints based on the above subportfolios or other hard-coded type constraints
    """
    print ("Optimizing Portfolio")
    #construct the url
    BASEURL = uri + "api/v1/optimization/portfolio/construct"
    headers = {
        'content-type': "application/json",
        'accept': "application/json",
        'X-IBM-Access-Token': accessToken
        }
    optimized_portfolio = requests.post(BASEURL,headers=headers, data=json.dumps(payload))

    #print the status and returned json
    status =optimized_portfolio.status_code
    print("Portfolio Optimization status: " + str(status))

    if status != 200:
        print(optimized_portfolio.text)
        return optimized_portfolio.text
    else:
        data = optimized_portfolio.json()
        return data
