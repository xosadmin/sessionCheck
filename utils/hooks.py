import re, requests

def composeURL(origURL,msg,ifUp):
    tempURL = origURL.split("?")[0]
    if ifUp:
        if "." in msg:
            msg = msg.split(".")[0]  # Remove .123 from 01:01:01.123
        if " " in msg:
            msg = re.sub(" ", "_", msg)
        newURL = tempURL + "?status=up&msg=Established_since_" + msg + "&ping="
    else:
        if re.match("[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{1,}",msg):
            msg = msg.replace("_DUE_TO_","_ON_")
        if "BGP Error:" in msg:
            msg = msg.replace("BGP Error: ", "")
            msg = msg.upper()
        if " " in msg:
            msg = re.sub("[ :]+", "_", msg)
            msg = msg.upper()
        newURL = tempURL + "?status=down&msg=" + msg + "&ping="
    return newURL

def sendHook(url, msg, ifUp=False):
    try:
        newURL = composeURL(url, msg, ifUp)
        response = requests.get(newURL)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error while sending hook: {e}")
        return False
