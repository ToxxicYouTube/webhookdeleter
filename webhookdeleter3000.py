# Modules importation
import time
import os
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("py -m pip instamm requests")
    import requests

init()
os.system("title 𝗪𝗘𝗕𝗛𝗢𝗢𝗞 𝗗𝗘𝗟𝗘𝗧𝗘𝗥")
print("webhook deleter")
webhook = input(" [INPUT] ENTER THE WEBHOOK TO DELETE : ")

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n [LOGS] WEBHOOK SUCCESFULLY DELETED")
        os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
    elif check.status_code == 200:
        print("\n [LOGS] FAILED TO DELETE WEBHOOK")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print("\n [LOGS] THE WEBHOOK IS INVALID")
    os.system("pause >nul")
elif test.status_code == 200:
    print("\n [LOGS] THE WEBHOOK IS VALID")
    delete()
