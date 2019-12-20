from sys import platform
from subprocess import check_output
import hashlib
import os.path

def getCPUsum():
    if platform == "win32":  # wmic csproduct get  UUID
        output = check_output("wmic csproduct get UUID", shell=True).decode()
        hardUUID = output.split("\n")[1]
        output = check_output("wmic csproduct get IdentifyingNumber", shell=True).decode()
        serialNum = output.split("\n")[1]
    elif platform == "linux" or platform == "linux2": #dmidecode | grep -i uuid
        output = check_output("dmidecode -s system-uuid", shell=True).decode()
        hardUUID = output.split(":")[1][1:-1]
        serialNum = check_output("dmidecode -s system-serial-number", shell=True).decode()
    elif platform == "darwin":
        output = check_output("system_profiler SPHardwareDataType | grep UUID", shell=True).decode()
        hardUUID = output.split(":")[1][1:-1]
        output = check_output("system_profiler SPHardwareDataType | grep Serial", shell=True).decode()
        serialNum = output.split(":")[1][1:-1]
    checkStr = hardUUID + " " + serialNum
    return hashlib.sha256(checkStr.encode('utf-8')).hexdigest()

def checkCPUsum(givenChecksum):
    existKey = fromAccessKey()
    if existKey != getCPUsum():
        return False
    else:
        return True

def toAccessKey(checksum):
    with open("access.key", "w") as accFile:
        accFile.write(checksum)

def fromAccessKey():
    if os.path.exists("access.key"):
        with open("access.key", "r") as accFile:
            return accFile.readline()
    else:
        return -1

if __name__ == "__main__":
    toAccessKey(getCPUsum())
    print(fromAccessKey())