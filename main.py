
import requests
import psutil
import json
import platform
from cpuinfo import get_cpu_info
import time
import os


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


def getUrl():
    try:
        return os.environ['AUDIT_URL']
    except:
        print("set the audit url in the enviroment 'export AUDIT_URL=https....'")


def makePostRequest(url,jsonData):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=jsonData,headers=headers)
    if(response.status_code == 201):
        print("the request was successfully sent to the audit server")
        re = json.loads(response.content.decode())
        id = re["audit_id"]
        print("make a get request to our api to see the results")
        print(getUrl()+"/"+str(id))
        print(getUrl()+"/"+str(id)+"/process")
        print(getUrl()+"/"+str(id)+"/users")
    else:
        print("something went wrong")


def generateJson():
    return json.dumps({"users": parseUsers(), "process": processList(
    ), "os_name": getOsName(), "os_version": getOsVersion(),  "architecture": cpuinfo["arch"],
        "cpu_logical_cores": psutil.cpu_count(logical=True),
        "cpu_physical_cores": psutil.cpu_count(logical=False),
        "brand": cpuinfo["brand_raw"],
        "timestamp": int(round(time.time()*1000, 1))})
# send api request
makePostRequest(getUrl(),generateJson())