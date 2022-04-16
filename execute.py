from lib import api, integrity
import os
from lib.api import bcolors
from lib.live.moduleManager import manage
from lib.live import interface

os.system("clear")

print(bcolors.HEADER + bcolors.BOLD + "**********")
print("**********")
print("***")
print("**********")
print(
    "**********   *******    ******   *******  *      *   ******  *   ******   ******"
)
print("***         *       *  *        *         * *    *  *        *  *        *")
print(
    "***         *       *  *         ******   *   *  *   *****   *  *         ***** "
)
print(
    "***         *       *  *        *         *    * *        *  *  *              *"
)
print(
    "***          *******   *         *******  *      *  ******   *   ******  ****** "
)
print("\n")
print(
    "                           ---Linux Forensics---                                 \n"
    + bcolors.ENDC
)

print(bcolors.WARNING + "Enter the path to the resulting directory: ")
checkOutp = True
while checkOutp == True:
    rawOutp = input(">>> " + bcolors.ENDC)
    try:
        if not os.path.exists(rawOutp):
            os.makedirs(rawOutp)
        checkOutp = False
    except Exception as e:
        print(bcolors.FAIL + "Error! Please try again.")
        print("NameError: " + str(e) + bcolors.ENDC)

try:
    computerName = api.exeCmd("hostname")
except:
    computerName = "UnknownComputer"

# Evidence ID includes computer name and
# converted seconds since the epoch (1970-01-01 UTC) to a date
eID = computerName + "_" + api.exeCmd('date +"%s"')

folderName = eID + "_" + api.exeCmd('date +"%d-%m-%y_%T"')

outp = os.path.join(rawOutp, folderName)
os.makedirs(outp)

sysFolder = "A.System_" + eID
sysFolder = os.path.join(outp, sysFolder)

nwFolder = "B.Network_" + eID
nwFolder = os.path.join(outp, nwFolder)

evtFolder = "C.Event_" + eID
evtFolder = os.path.join(outp, evtFolder)

usrFolder = "D.User_" + eID
usrFolder = os.path.join(outp, usrFolder)

while True:
    options = interface.getOptions()
    options.split()
    manage(folderName, rawOutp, options, sysFolder, nwFolder, evtFolder, usrFolder, eID)
    if "E" in options:
        api.exeCmd("sudo chmod 777 -R " + outp)
        print(bcolors.WARNING + "\nExit...")
        break
    print(
        bcolors.WARNING
        + "\nDo you want to do further forensics? If you choose NO, the system will compress the forensic results and terminate the program. (y/n)"
    )
    ask = input(">>> " + bcolors.ENDC)
    if ask == "n" or ask == "no":
        print(bcolors.OKCYAN + "\nCompressing files..." + bcolors.ENDC)
        integrity.integrityResult(folderName, rawOutp)

        api.exeCmd("sudo chmod 777 -R " + outp)
        print(bcolors.WARNING + "\nExit...")
        break
