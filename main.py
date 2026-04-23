import os, sys
from utils.yamlworks import readConf
from utils.hooks import sendHook
from utils.bird import getBirdResponse, statToList

configLocation = os.path.abspath("config.yaml")
rpkiStats = ["Sync-Start", "Sync-Running"]

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
        msg = f"{respList[-2]}"
        sendHook(value, msg, True)
        print(f"{key} is up. Successfully sent hook.")
    elif "RPKI" in respList[1] and respList[-1] in rpkiStats:
        print(f"RPKI session {key} is refreshing.")
        sendHook(value, f"RPKI_REFRESHING_{respList[-1]}", True)
        continue
    else:
        msg = f"{respList[-2]}_STATE_DUE_TO_{respList[-1]}"
        sendHook(value, msg, False)
        print(f"{key} is down. Successfully sent hook.")

print("Completed.")