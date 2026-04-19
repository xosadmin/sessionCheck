import re, subprocess

def outputLastLine(raw_output):
    last_line = None
    for line in raw_output.splitlines():
        line = line.strip()
        if line:
            last_line = line
    return last_line

def getBirdResponse(cmd):
    if not cmd or not isinstance(cmd, list):
        return False
    try:
        response = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=10)
        return outputLastLine(response)
    except Exception as e:
        print(f"Error while contacting bird: {e}")
        return False

def statToList(orig):
    if not orig or not isinstance(orig, str):
        return []
    replaceSpace = re.sub(" +"," ",orig)
    return replaceSpace.split(" ")