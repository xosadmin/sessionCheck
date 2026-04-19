import re, requests

def composeURL(origURL,msg):
    tempURL = origURL.split("?")[0]
    if " " in msg:
        msg = msg.split(".")[0] # Remove .123 from 01:01:01.123
        msg = re.sub(" ", "_", msg)
    newURL = tempURL + "?status=Established&msg=" + msg + "&ping="
    return newURL

def sendHook(url, msg):
    try:
        newURL = composeURL(url,msg)
        response = requests.get(newURL)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error while sending hook: {e}")
        return False
