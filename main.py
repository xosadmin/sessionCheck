import os, sys
from utils.yamlworks import readConf
from utils.hooks import sendHook
from utils.bird import getBirdResponse, statToList

configLocation = os.path.abspath("config.yaml")

if not os.path.exists(configLocation):
    print("Cannot find config file.")
    sys.exit(1)

configs = readConf(configLocation)
monitorList = configs.get('monitors',{})

if len(monitorList) == 0:
    print("No monitors configured")
    sys.exit(1)

for key,value in monitorList.items():
    print(f"Getting session {key} status...")
    cmd = ["birdc","show","proto",key]
    response = getBirdResponse(cmd)
    if not response:
        print(f"Error occurred while checking {key}. ")
        continue
    respList = statToList(response)
    if len(respList) == 0:
        print(f"Error when splitting response for {key}.")
        continue
    if "Established" in respList:
        msg = f"Established_Since_{respList[-2]}"
        sendHook(value, msg)
        print(f"{key} is up. Successfully sent hook.")

print("Completed.")