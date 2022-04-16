import os
from lib import api
from lib.api import bcolors


def getOptions():
    print(
        bcolors.WARNING
        + "\n\nSelect one or more of the options below to launch the program by choosing the number before it and entering into the area below:"
    )
    print("*Options are separated by spaces." + bcolors.ENDC)
    print(bcolors.OKCYAN + "00 - Select all\n")
    print(bcolors.UNDERLINE + "A. System Data" + bcolors.ENDC)
    print(bcolors.OKCYAN + "01 - Collect system information")
    print("02 - Collect list of open files")
    print("03 - Collect process status")
    print("04 - Collect disk filesystems information")
    print("05 - Collect list of mounted filesystems")
    print("06 - Collect loaded kernel modules information")
    print("07 - Collect file metadata")
    print("08 - Collect file hashes\n")

    print(bcolors.UNDERLINE + "B. Network Data" + bcolors.ENDC)
    print(bcolors.OKCYAN + "09 - Collect network interfaces")
    print("10 - Collect network statistics")
    print("11 - Collect network routing tables\n")

    print(bcolors.UNDERLINE + "C. Event Data" + bcolors.ENDC)
    print(bcolors.OKCYAN + "12 - Collect list of last logged-in users")
    print("13 - Collect list of failed logins")
    print("14 - Collect bash history")
    print("15 - Collect log files")
    print("16 - Collect browser history\n")

    print(bcolors.UNDERLINE + "D. User Data" + bcolors.ENDC)
    print(bcolors.OKCYAN + "17 - Collect local users information")
    print("18 - Check the integrity of local user credentials\n")

    print(
        "E. Compress files, export encrypted SHA256 signature for integrity check and exit\n"
        + bcolors.ENDC
    )

    print(bcolors.WARNING + "Enter your options:")
    options = input(">>> " + bcolors.ENDC)
    return options
