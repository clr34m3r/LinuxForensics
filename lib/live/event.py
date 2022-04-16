from lib import api
import os
from lib.api import bcolors
import sqlite3
import csv


def recentLogin(outp, eID):
    fName = "12.RecentLogin_" + eID + ".txt"
    try:
        api.exeCmd("last -Faiwx" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def failedLogin(outp, eID):
    fName = "13.FailedLoginAttempts_" + eID + ".txt"
    try:
        api.exeCmd("sudo lastb" + ">" + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getBashHistory(outp, eID):
    fName = "14.BashHistory_" + eID + ".txt"
    try:
        api.exeCmd(
            'sudo grep -e "$pattern" /home/*/.bash_history'
            + ">"
            + os.path.join(outp, fName)
        )
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getLogFiles(outp, eID):
    fName = "15.Log_" + eID
    try:
        api.exeCmd("sudo cp -R /var/log " + os.path.join(outp, fName))
        api.exeCmd("sudo chmod 777 -R " + os.path.join(outp, fName))
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getChromeHistory(path, user, profile):
    fName = profile + ".csv"
    try:
        con = sqlite3.connect(
            "/home/" + user + "/.config/google-chrome/" + profile + "/History"
        )

        c = con.cursor()
        c.execute(
            "SELECT datetime(last_visit_time / 1000000 - 11644473600, 'unixepoch', 'localtime'),url,title,visit_count FROM urls ORDER BY last_visit_time DESC"
        )
        results = c.fetchall()

        f = open(os.path.join(path, fName), "w")
        cols = ("Datetime", "URL", "Title", "Visit Count")
        write = csv.writer(f)
        write.writerow(cols)
        write.writerows(results)

        c.close()
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getFirefoxHistory(cmd, path, profile):
    fName = profile + ".csv"
    try:
        c = sqlite3.connect(cmd)

        cursor = c.cursor()
        select_statement = "SELECT datetime(visit_date/1000000,'unixepoch') AS Time,url,title,visit_count FROM moz_historyvisits, moz_places WHERE moz_historyvisits.place_id=moz_places.id ORDER BY Time DESC"
        cursor.execute(select_statement)

        results = cursor.fetchall()

        f = open(os.path.join(path, fName), "w")
        cols = ("Datetime", "URL", "Title", "Visit Count")
        write = csv.writer(f)
        write.writerow(cols)
        write.writerows(results)

        cursor.close()
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)


def getBrowserHistory(outp, eID):
    fName = "16.BrowserHistory_" + eID
    folder = os.path.join(outp, fName)
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:
        users = api.exeCmd("cd /home; ls")
        for user in users.split():
            userFolder = os.path.join(folder, user)

            # Chrome
            userChromeFolder = os.path.join(userFolder, "Chrome")

            if os.path.exists(
                "/home/"
                + user
                + "/.config/google-chrome/"
                + "Guest Profile"
                + "/History"
            ):
                if not os.path.exists(userFolder):
                    os.makedirs(userFolder)
                if not os.path.exists(userChromeFolder):
                    os.makedirs(userChromeFolder)
                getChromeHistory(userChromeFolder, user, "Guest Profile")

            if os.path.exists(
                "/home/" + user + "/.config/google-chrome/" + "Default" + "/History"
            ):
                if not os.path.exists(userFolder):
                    os.makedirs(userFolder)
                if not os.path.exists(userChromeFolder):
                    os.makedirs(userChromeFolder)
                getChromeHistory(userChromeFolder, user, "Default")

            i = 1
            while True:
                cProfile = "Profile " + str(i)
                if os.path.exists(
                    "/home/" + user + "/.config/google-chrome/" + cProfile + "/History"
                ):
                    if not os.path.exists(userFolder):
                        os.makedirs(userFolder)
                    if not os.path.exists(userChromeFolder):
                        os.makedirs(userChromeFolder)
                    getChromeHistory(userChromeFolder, user, cProfile)
                    i = i + 1
                else:
                    break

            # Firefox
            userFirefoxFolder = os.path.join(userFolder, "Firefox")

            if os.path.exists("/home/" + user + "/.mozilla/firefox"):
                fProfiles = api.exeCmd("cd /home/" + user + "/.mozilla/firefox; ls")
                for fProfile in fProfiles.split():
                    fPath = (
                        "/home/"
                        + user
                        + "/.mozilla/firefox/"
                        + fProfile
                        + "/places.sqlite"
                    )

                    if os.path.exists(fPath):
                        if not os.path.exists(userFolder):
                            os.makedirs(userFolder)
                        if not os.path.exists(userFirefoxFolder):
                            os.makedirs(userFirefoxFolder)
                        getFirefoxHistory(fPath, userFirefoxFolder, fProfile[0:8])

        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + fName + " export failed!")
        print("NameError: " + str(e) + bcolors.ENDC)
