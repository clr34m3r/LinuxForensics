import os
from lib import api
from lib.api import bcolors


def nwInterfaces(outp, eID):
    # Network Interfaces
    fName = "9.NetworkInterfaces_" + eID + ".txt"
    try:
        api.exeCmd("ifconfig -a" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def nwConnections(outp, eID):
    # Network connections, open ports. program associated with various ports
    fName = "10.NetworkConnections_" + eID + ".txt"
    try:
        api.exeCmd("sudo netstat -anp" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def routingTables(outp, eID):
    fName = "11.RoutingTables_" + eID + ".txt"
    try:
        try:
            api.exeCmd("netstat -rn" + ">" + os.path.join(outp, fName))
            print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
        except:
            api.exeCmd("route" + ">" + os.path.join(outp, fName))
            print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)
