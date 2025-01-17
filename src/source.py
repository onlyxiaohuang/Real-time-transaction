import okx_api as okx
import json

import os

configdest = "./Rtt/json/config.json"
def ReadJson():
    with open(configdest) as f:
        return json.load(f)    


def GetMarketData():
    config = ReadJson()
    #print(config)
    for item in config["instId"].items():
        print(item)

    return okx.Market()

#if __name__ == 'main':
#print(os.getcwd())
data = GetMarketData()

#print(data) 


print("Hello World!")