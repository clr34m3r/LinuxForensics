from lib.live import system, network, event, user
from lib import integrity
import os
from lib.api import bcolors


def activeA(sysFolder, eID):
    print(bcolors.OKCYAN + "\nCollecting A. System Data..." + bcolors.ENDC)
    if not os.path.exists(sysFolder):
        os.makedirs(sysFolder)

    print(bcolors.OKCYAN + "- Collecting system information (1)..." + bcolors.ENDC)
    system.sysInfo(sysFolder, eID)

    print(bcolors.OKCYAN + "- Collecting list of open files (2)..." + bcolors.ENDC)
    system.openFiles(sysFolder, eID)

    print(bcolors.OKCYAN + "- Collecting process status (3)..." + bcolors.ENDC)
    system.runningProcesses(sysFolder, eID)

    print(
        bcolors.OKCYAN
        + "- Collecting disk filesystems information (4)..."
        + bcolors.ENDC
    )
    system.freeDisk(sysFolder, eID)

    print(
        bcolors.OKCYAN
        + "- Collecting list of mounted filesystems (5)..."
        + bcolors.ENDC
    )
    system.mountedDisk(sysFolder, eID)

    print(
        bcolors.OKCYAN
        + "- Collecting loaded kernel modules information (6)..."
        + bcolors.ENDC
    )
    system.kernelModules(sysFolder, eID)

    print(bcolors.OKCYAN + "- Collecting file metadata (7)..." + bcolors.ENDC)
    system.getFileMetadata(sysFolder, eID)

    print(bcolors.OKCYAN + "- Collecting file hashes (8)..." + bcolors.ENDC)
    system.getFileHashes(sysFolder, eID)

    print(bcolors.OKGREEN + "All system data collected!" + bcolors.ENDC)


def activeB(nwFolder, eID):
    print(bcolors.OKCYAN + "\nCollecting B. Network Data..." + bcolors.ENDC)
    if not os.path.exists(nwFolder):
        os.makedirs(nwFolder)

    print(bcolors.OKCYAN + "- Collecting network interfaces (9)..." + bcolors.ENDC)
    network.nwInterfaces(nwFolder, eID)

    print(bcolors.OKCYAN + "- Collecting network statistics (10)..." + bcolors.ENDC)
    network.nwConnections(nwFolder, eID)

    print(bcolors.OKCYAN + "- Collecting network routing tables (11)..." + bcolors.ENDC)
    network.routingTables(nwFolder, eID)

    print(bcolors.OKGREEN + "All network data collected!" + bcolors.ENDC)


def activeC(evtFolder, eID):
    print(bcolors.OKCYAN + "\nCollecting C. Event Data..." + bcolors.ENDC)
    if not os.path.exists(evtFolder):
        os.makedirs(evtFolder)

    print(
        bcolors.OKCYAN
        + "- Collecting list of last logged-in users (12)..."
        + bcolors.ENDC
    )
    event.recentLogin(evtFolder, eID)

    print(bcolors.OKCYAN + "- Collecting list of failed logins (13)..." + bcolors.ENDC)
    event.failedLogin(evtFolder, eID)

    print(bcolors.OKCYAN + "- Collecting bash history (14)..." + bcolors.ENDC)
    event.getBashHistory(evtFolder, eID)

    print(bcolors.OKCYAN + "- Collecting log files (15)..." + bcolors.ENDC)
    event.getLogFiles(evtFolder, eID)

    print(bcolors.OKCYAN + "- Collecting browser history (16)..." + bcolors.ENDC)
    event.getBrowserHistory(evtFolder, eID)

    print(bcolors.OKGREEN + "All event data collected!" + bcolors.ENDC)


def activeD(usrFolder, eID):
    print(bcolors.OKCYAN + "\nCollecting D. User Data..." + bcolors.ENDC)
    if not os.path.exists(usrFolder):
        os.makedirs(usrFolder)

    print(
        bcolors.OKCYAN + "- Collecting local users information (17)..." + bcolors.ENDC
    )
    user.getLocalUsers(usrFolder, eID)

    print(
        bcolors.OKCYAN
        + "- Checking the integrity of local user credentials (18)..."
        + bcolors.ENDC
    )
    user.detectAbnormalAccounts(usrFolder, eID)

    print(bcolors.OKGREEN + "All user data collected!" + bcolors.ENDC)


def manage(
    folderName, rawOutp, options, sysFolder, nwFolder, evtFolder, usrFolder, eID
):
    for option in options.split():
        if option == "00" or option == "0":
            activeA(sysFolder, eID)
            activeB(nwFolder, eID)
            activeC(evtFolder, eID)
            activeD(usrFolder, eID)

        elif option == "A":
            activeA(sysFolder, eID)

        elif option == "01" or option == "1":
            print(
                bcolors.OKCYAN + "\nCollecting system information (1)..." + bcolors.ENDC
            )
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.sysInfo(sysFolder, eID)

        elif option == "02" or option == "2":
            print(
                bcolors.OKCYAN + "\nCollecting list of open files (2)..." + bcolors.ENDC
            )
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.openFiles(sysFolder, eID)

        elif option == "03" or option == "3":
            print(bcolors.OKCYAN + "\nCollecting process status (3)..." + bcolors.ENDC)
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.runningProcesses(sysFolder, eID)

        elif option == "04" or option == "4":
            print(
                bcolors.OKCYAN
                + "\nCollecting disk filesystems information (4)..."
                + bcolors.ENDC
            )
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.freeDisk(sysFolder, eID)

        elif option == "05" or option == "5":
            print(
                bcolors.OKCYAN
                + "\nCollecting list of mounted filesystems (5)..."
                + bcolors.ENDC
            )
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.mountedDisk(sysFolder, eID)

        elif option == "06" or option == "6":
            print(
                bcolors.OKCYAN
                + "\nCollecting loaded kernel modules information (6)..."
                + bcolors.ENDC
            )
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.kernelModules(sysFolder, eID)

        elif option == "07" or option == "7":
            print(bcolors.OKCYAN + "\nCollecting file metadata (7)..." + bcolors.ENDC)
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.getFileMetadata(sysFolder, eID)

        elif option == "08" or option == "8":
            print(bcolors.OKCYAN + "\nCollecting file hashes (8)..." + bcolors.ENDC)
            if not os.path.exists(sysFolder):
                os.makedirs(sysFolder)
            system.getFileHashes(sysFolder, eID)

        elif option == "B":
            activeB(nwFolder, eID)

        elif option == "09" or option == "9":
            print(
                bcolors.OKCYAN + "\nCollecting network interfaces (9)..." + bcolors.ENDC
            )
            if not os.path.exists(nwFolder):
                os.makedirs(nwFolder)
            network.nwInterfaces(nwFolder, eID)

        elif option == "10":
            print(
                bcolors.OKCYAN
                + "\nCollecting network statistics (10)..."
                + bcolors.ENDC
            )
            if not os.path.exists(nwFolder):
                os.makedirs(nwFolder)
            network.nwConnections(nwFolder, eID)

        elif option == "11":
            print(
                bcolors.OKCYAN
                + "\nCollecting network routing tables (11)..."
                + bcolors.ENDC
            )
            if not os.path.exists(nwFolder):
                os.makedirs(nwFolder)
            network.routingTables(nwFolder, eID)

        elif option == "C":
            activeC(evtFolder, eID)

        elif option == "12":
            print(
                bcolors.OKCYAN
                + "\nCollecting list of last logged-in users (12)..."
                + bcolors.ENDC
            )
            if not os.path.exists(evtFolder):
                os.makedirs(evtFolder)
            event.recentLogin(evtFolder, eID)

        elif option == "13":
            print(
                bcolors.OKCYAN
                + "\nCollecting list of failed logins (13)..."
                + bcolors.ENDC
            )
            if not os.path.exists(evtFolder):
                os.makedirs(evtFolder)
            event.failedLogin(evtFolder, eID)

        elif option == "14":
            print(bcolors.OKCYAN + "\nCollecting bash history (14)..." + bcolors.ENDC)
            if not os.path.exists(evtFolder):
                os.makedirs(evtFolder)
            event.getBashHistory(evtFolder, eID)

        elif option == "15":
            print(bcolors.OKCYAN + "\nCollecting log files (15)..." + bcolors.ENDC)
            if not os.path.exists(evtFolder):
                os.makedirs(evtFolder)
            event.getLogFiles(evtFolder, eID)

        elif option == "16":
            print(
                bcolors.OKCYAN + "\nCollecting browser history (16)..." + bcolors.ENDC
            )
            if not os.path.exists(evtFolder):
                os.makedirs(evtFolder)
            event.getBrowserHistory(evtFolder, eID)

        elif option == "D":
            activeD(usrFolder, eID)

        elif option == "17":
            print(
                bcolors.OKCYAN
                + "\nCollecting local users information (16)..."
                + bcolors.ENDC
            )
            if not os.path.exists(usrFolder):
                os.makedirs(usrFolder)
            user.getLocalUsers(usrFolder, eID)

        elif option == "18":
            print(
                bcolors.OKCYAN
                + "\nChecking the integrity of local user credentials (17)..."
                + bcolors.ENDC
            )
            if not os.path.exists(usrFolder):
                os.makedirs(usrFolder)
            user.detectAbnormalAccounts(usrFolder, eID)

        elif option == "E":
            print(bcolors.OKCYAN + "\nCompressing files..." + bcolors.ENDC)
            integrity.integrityResult(folderName, rawOutp)

        else:
            print(
                bcolors.WARNING
                + "\nYou have selected "
                + option
                + " but this option does not exist."
                + bcolors.ENDC
            )
