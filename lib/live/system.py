import os
from lib import api
from lib.api import bcolors


def sysInfo(outp, eID):
    fName = "1.SystemInfomation_" + eID + ".txt"
    try:
        sysInfoTxt = open(os.path.join(outp, fName), "w")

        # Date and time information
        sysInfoTxt.write("--- Date and time information: \n")
        try:
            sysInfoTxt.write(api.exeCmd("date"))
        except:
            sysInfoTxt.write("Error! Can't get datetime information!")

        # User currently logged in
        sysInfoTxt.write("\n\n--- User currently logged in: \n")
        try:
            sysInfoTxt.write(api.exeCmd("w"))
        except:
            sysInfoTxt.write("Error! The logged in user cannot be identified!")

        # Operating system version
        sysInfoTxt.write("\n\n--- Operating system version: ")
        sysInfoTxt.write("\n- Kernel name: ")
        try:
            sysInfoTxt.write(api.exeCmd("uname"))
        except:
            sysInfoTxt.write("Unknown")

        sysInfoTxt.write("\n- Network hostname: ")
        try:
            sysInfoTxt.write(api.exeCmd("uname -n"))
        except:
            sysInfoTxt.write("Unknown")

        sysInfoTxt.write("\n- Kernel version: ")
        try:
            sysInfoTxt.write(api.exeCmd("uname -v"))
        except:
            sysInfoTxt.write("Unknown")

        sysInfoTxt.write("\n- Kernel release: ")
        try:
            sysInfoTxt.write(api.exeCmd("uname -r"))
        except:
            sysInfoTxt.write("Unknown")

        sysInfoTxt.write("\n- Machine hardware name: ")
        try:
            sysInfoTxt.write(api.exeCmd("uname -m"))
        except:
            sysInfoTxt.write("Unknown")

        # System hardware infomation
        #     sysInfoTxt.write("\n\n--- System hardware infomation: \n")
        #     try:
        #         sysInfoTxt.write(api.exeCmd("sudo lshw"))
        #     except:
        #         sysInfoTxt.write("Error! Can't get system hardware information!")

        sysInfoTxt.close()
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


# def USBInformation(outp, eID):
#     fName = "2.USBControllersInformation_" + eID + ".txt"
#     try:
#         api.exeCmd("lsusb -v" + ">" + os.path.join(outp, fName))
#         print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
#     except Exception as e:
#         print(bcolors.FAIL + fName + " export failed!")
#         print("NameError: " + str(e) + bcolors.ENDC)


def openFiles(outp, eID):
    # See which programs are opening certain files
    fName = "2.OpenFilesByPrograms_" + eID + ".txt"
    try:
        api.exeCmd("sudo lsof -V" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def runningProcesses(outp, eID):
    fName = "3.RunningProcesses_" + eID + ".txt"
    try:
        api.exeCmd("ps -ef" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def freeDisk(outp, eID):
    fName = "4.FreeDisk_" + eID + ".txt"
    try:
        api.exeCmd("df" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def mountedDisk(outp, eID):
    fName = "5.MountedDisk_" + eID + ".txt"
    try:
        api.exeCmd("mount" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def kernelModules(outp, eID):
    fName = "6.LoadedKernelModules_" + eID + ".txt"
    try:
        api.exeCmd("lsmod" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getFileMetadata(outp, eID):
    fName = "7.FileMetadata_" + eID + ".csv"
    try:
        fileMetadata = open(os.path.join(outp, fName), "w")
        fileMetadata.write(
            "Access Date=Access Time=Modify Date=Modify Time=Create Date=Create Time=Permissions=UID=Username=GID=Groupname=Size=File\n"
        )
        fileMetadata.write(
            api.exeCmd(
                "cd / ; sudo find $1 -printf %Ax=%AT=%Tx=%TT=%Cx=%CT=%m=%U=%u=%G=%g=%s=%p\\\\n"
            )
        )
        fileMetadata.close()
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getFileHashes(outp, eID):
    fName = "8.FileHashes_" + eID + ".txt"
    try:
        api.exeCmd(
            "cd / ; sudo find $1 -xdev -type f -exec sha1sum -b {} \;"
            + ">"
            + os.path.join(outp, fName)
        )
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)
