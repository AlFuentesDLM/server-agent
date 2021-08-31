
import psutil
import json
import platform
from cpuinfo import get_cpu_info
import time


def parseUsers():
    users = psutil.users()
    arrayParsedUsers = []
    for user in users:
        arrayParsedUsers.append(
            {"name": user.name, "terminal": user.terminal, "host": user.host, "pid": user.pid})
    return arrayParsedUsers


def getOsName():
    return platform.system()


def getOsVersion():
    return platform.release()



def processList():
    listOfprocess = []
    for proc in psutil.process_iter(['pid', 'name', "ppid", "username"]):
        listOfprocess.append(proc.info)
    return listOfprocess

cpuinfo = get_cpu_info()

# send api request
print(json.dumps({"users": parseUsers(), "process": processList(
), "os_name": getOsName(), "os_version": getOsVersion(),  "architecture": cpuinfo["brand_raw"],
        "cpu_logical_cores": psutil.cpu_count(logical=True),
        "cpu_physical_cores": psutil.cpu_count(logical=False),
        "brand": cpuinfo["brand_raw"],
        "timestamp":int(round(time.time()*1000,1))}))
