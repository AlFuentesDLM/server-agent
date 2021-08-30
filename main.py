
import psutil
import json
import os
import platform
import subprocess
from cpuinfo import get_cpu_info



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

def getCpuInfo():
    cpuinfo = get_cpu_info()
    obj = {
             "architecture": cpuinfo["brand_raw"],
             "cpu_logical_core":psutil.cpu_count(logical=True),
             "cpu_fisic_core":psutil.cpu_count(logical=False),
             "brand":cpuinfo["brand_raw"],
    }
    return obj


listOfprocess = []
for proc in psutil.process_iter(['pid', 'name', "ppid", "username"]):
    listOfprocess.append(proc.info)

print(json.dumps({"users":parseUsers(),"process":listOfprocess,"osname":getOsName(),"osversion":getOsVersion(),"cpu":getCpuInfo()}))
